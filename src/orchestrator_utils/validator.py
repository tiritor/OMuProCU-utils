

import ipaddress
import json
import os
import re
import yaml
import logging

import kubernetes_validate

from .logger.logger import init_logger
from .tools.accelerator_type import AcceleratorType 
from .tools.countermeasure_action import CountermeasureAction

class ValidationException(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "ValidationException with %s" % self.msg


class TDCValidationException(ValidationException):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "TDCValidationException with %s" % self.msg


class INCIngressNameException(TDCValidationException):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "TDCValidationException with %s" % self.msg


class Validator(object):
    """
    General class for validation of different deployment types
    """
    def __init__(self, log_level=logging.INFO):
        self.logger = init_logger(self.__class__.__name__, log_level)
    
    def validate(self, path):
        """
        Abstract method for validating submitted deployments
        """
        raise NotImplementedError
    
    def validate_vnis(self, vnis):
        """
        Helper method to validate VXLAN VNIs
        """
        if isinstance(vnis, list):
            for vni in vnis:
                if isinstance(vni, int):
                    self._validate_vni(vni)
                elif isinstance(vni, str):
                    self._validate_vni(int(vni))
            self.logger.debug("VNIs valid!")
            return True
        elif isinstance(vnis, int):
            self._validate_vni(vnis)
            self.logger.debug("VNIs valid!")
            return True 
        else:
            raise TDCValidationException("VNI {:s} not valid!".format(vnis.__str__()))

    def _validate_vni(self, vni):
        """
        Helper method to validate VXLAN VNI
        """
        if 1 <= vni <= 2 ** 48 - 1:
            self.logger.debug("VNI {:d} is valid".format(vni))
        else:
            self.logger.error("VNI {:d} is invalid".format(vni))
            raise ValueError

    def _validate_port_number(self, port_number):
        """
        Helper method for validate layer 4 port number 
        """
        if 1 <= port_number <= 65535:
            self.logger.debug("{:d} is a VALID port number.".format(port_number))
        else:
            self.logger.error("{:d} is NOT a VALID port number.".format(port_number))
            raise ValidationException("{:d} is NOT a VALID port number.".format(port_number))

    def _validate_ip(self, ip):
        """
        Helper method for validate ip address
        """
        try:
            ip = ipaddress.ip_address(ip)
            self.logger.debug('%s is a correct IP%s address.' % (ip, ip.version))
        except ValueError:
            self.logger.error('address/netmask is invalid: %s' % ip)
            raise ValidationException('address/netmask is invalid: %s' % ip)
        except:
            self.logger.error('Usage : %s  ip' % ip)
            raise ValidationException('Usage : %s  ip' % ip)

    def _validate_ip_proto_number(self, ip_proto):
        """
        Helper method for validate ip protocol number
        """
        if 0 <= ip_proto <= 255:
            self.logger.debug("Proto {:d} is valid".format(ip_proto))
            return True
        else: 
            self.logger.error("IP Proto must be between 0 and 255!")
            raise ValidationException("IP Proto must be between 0 and 255!")
        

class TDCValidator(Validator):
    """
    TDC Validator class
    """
    path = ""
    tdc = None
    tdc_name = ""
    tdc_id = -1
    tcd = None
    til = None
    inc = None
    start_tcaport = 20000

    def __init__(self, start_tcaport=20000, path="", log_level=logging.INFO):
        super().__init__(log_level)
        self.start_tcaport = start_tcaport
        self.path = path
        self.tenant_security_config = None
        with open("conf/tenant_security_config.json", "r") as f:
            self.tenant_security_config = json.load(f)
        self.extern_blacklist = None
        with open("conf/extern_blacklist.json") as f:
            self.extern_blacklist = json.load(f)
    
    def load_tdc(self, raw_tdc):
        """
        Load TDC deployment from file.
        
        Parameters:
        raw_tdc : stream
            Stream to read the TDC manifest. 
            Can be file or string stream.
        """
        tdc = yaml.safe_load(raw_tdc)
        self.tdc = tdc
        self.tdc_id = tdc["id"]
        self.tdc_name = tdc["name"]
        self.tcd = tdc["TCD"]
        self.til = tdc["TIL"]
        self.inc = tdc["INC"]
        self.logger.debug(self.tcd)
        self.logger.debug(self.til)
        self.logger.debug(self.inc)

    def _load_tenant_security_config(self):
        """
        Helper method to load tenant security config.
        """
        with open("conf/tenant_security_config.json", "r") as f:
            self.tenant_security_config = json.load(f)

    def _save_tenant_security_config(self):
        """
        Helper method to save tenant security config.
        """
        with open("conf/tenant_security_config.json", "w") as f:
            f.write("")
            json.dump(self.tenant_security_config, f)

    def validate(self, deployment = None, path = None, update_request = False):
        """
        Validates the TDC parts. 
        If deployment AND path is set, deployment is prefered!

        Parameters:
        -----------
        deployment : str
            TDC deployment which was submitted.
        path : str
            TDC deployment path to read from which was provided
        update_request : bool
            If update_request is true, this indicates that, the deployment should be already existing and it should be updated!
        """
        if deployment is None and path is not None:
            with open(path) as f:
                self.load_tdc(f)
        elif deployment is not None : 
            self.load_tdc(deployment)
        try:
            self._load_tenant_security_config() # Check for updates from the orchestrator
            if self.tdc_id < 1:
                raise TDCValidationException("Invalid ID: ID must be greater than 0!")
            else: 
                self.logger.debug("TDC ID valid!")
            self.validate_tcd(update_request)
            self.validate_til(update_request)
            self.validate_inc(update_request)
        except ValidationException as e:
            self.logger.error(e.__str__())
            return False
        except TypeError as e:
            self.logger.error(e.__str__())
            return False
        self.logger.info("TDC validated!")
        return True

    
    def validate_unique_mainIngressName(self, mainIngressName, update_request = False):
        """
        Check if mainIngressName provided in TDC is unique for the TIF.
        
        Parameters:
        -----------
        mainIngressName : str
            Main Ingress Name provided from INC part in the TDC
        update_request : bool
            If this is true, it can exist for the specified tenant and should be checked, if it is only updating its TDC.
        """
        for tenant_id in self.tenant_security_config.keys():
            for existing_mainIngressName in self.tenant_security_config[tenant_id]["mainIngressNames"]:
                if mainIngressName == existing_mainIngressName:
                    if str(tenant_id) == str(self.tdc_id) and update_request:
                        return True
                    self.logger.error("MainIngressName {} is not unique since it is already used!".format(mainIngressName))
                    return False
        return True


    def validate_tcd(self, update_request = False):
        """
        This function validates the TCD.

        The steps are: 
            1. Validate Kubernetes Deployment
            2. Validate Accelerator Type 
            3. Check if TCAPort is correctly specified
            4. Check the rules when countermeasures rules should be updated 

        Parameters:
        -----------
        update_request : bool
             If this is true, it can exist for the specified tenant and should be checked, if it is only updating its TDC.
        """
        log_prefix = "TCD" + " - "

        def validate_kubernetes_namespace(deployment):
            """
            Check if Kubernetes namespace is for the specified TDC. 

            Parameters:
            -----------
            deployment : dict
                Kubernetes deployment where the namespace should be defined.
            """
            if 'namespace' not in deployment["metadata"]:
                raise TDCValidationException("Namespace is not provided in the kubernetes deployment!")

        def validate_kubernetes(deployment):
            """
            Validate the kubernetes deployment.

            Parameters:
            -----------
            deployment : dict
                Kubernetes deployment from the TDC which should be validated.
            """
            try:
                test = kubernetes_validate.validate(deployment, '1.22', strict=True)
                validate_kubernetes_namespace(deployment)
                self.logger.debug("Kubernetes Deployment valid!")
                return True
            except kubernetes_validate.ValidationError as e:
                self.logger.error(''. join(e.path), e.message)
                return False

        def validate_acceleratorType(acceleratorType : str): 
            """
            Check if the accelerator type is valid and available

            Parameters:
            -----------
            acceleratorType: str
                accelerator specified in the TDC which should be checked.
            """
            try: 
                AcceleratorType(acceleratorType)
                self.logger.debug("AcceleratorType valid!")
                return True
            except ValueError:
                raise TDCValidationException("AcceleratorType not valid")
        
        log_method = ""
        try:
            if "kubernetesDeploymentFile" in self.tcd:
                log_method = log_prefix + "kubernetesDeploymentFile: "
                with open(self.tcd["kubernetesDeploymentFile"]) as f:
                    self.deployment = f.read()
                    validate_kubernetes(self.deployment)
            elif "kubernetesDeployment" in self.tcd:
                log_method = log_prefix + "kubernetesDeployment: "
                validate_kubernetes(self.tcd["kubernetesDeployment"])
            else:
                raise TDCValidationException("Neither kubernetesDeployment nor kubernetesDeploymentFile specified")
            log_method = log_prefix + "acceleratorType: "
            validate_acceleratorType(self.tcd["acceleratorType"])
        except TypeError as e:
            self.logger.error(log_method + e.__str__())
        
        self.logger.info("TCD validated!")
    
    def validate_til(self, update_request = False):
        """
        Validate Tenant Isolation Logic (TIL).

        Parameters:
        -----------
        update_request : bool
             If this is true, it can exist for the specified tenant and should be checked, if it is only updating its TDC.
        """
        log_prefix = "TIL" + " - "

        def validate_vni_access_for_tenant(vnis):
            """
            Validates if VNI access is allowed for this tenant or not

            Parameters:
            -----------
            vnis : int | str | list
                representation of VNIs which should be used to check access violation of this tenant.
            """
            def check_vni_access_violation(vni, tenant_security_config):
                """
                Helper method check for VNI access violation.

                Parameters:
                -----------
                vni : str | int
                    VNI which should be checked for access violation (if tenant is allowed to use this)
                tenant_security_config : dict
                    dictionary with the complete tenant security configuration.
                """
                if isinstance(vni, str):
                        vni = int(vni)
                return vni in tenant_security_config["Allowed_VNIs"]
                    
            if isinstance(vnis, list):
                for vni in vnis:
                    if check_vni_access_violation(vni, self.tenant_security_config[str(self.tdc_id)]):
                        self.logger.debug("VNI {} belongs to ID {}".format(vni, self.tdc_id))
                        continue
                    else: 
                        raise TDCValidationException("Access Violation detected! VNI {} does not belong to Tenant ID {}!".format(vni, self.tdc_id))
                return True
            else:
                if check_vni_access_violation(vnis, self.tenant_security_config[str(self.tdc_id)]):
                    self.logger.debug("VNI {} belongs to ID {}".format(vnis, self.tdc_id))
                    return True
                else: 
                    raise TDCValidationException("Access Violation detected! VNI {} does not belong to Tenant ID {}!".format(vnis, self.tdc_id))


        def validate_accessRules(accessRules):
            """
            Validate Access Rules.

            Parameters
            ----------
            accessRules : dict
                dictionary with access rules which should be checked.
            """
            validate_vni_access_for_tenant(accessRules["VNI"]) # Access Violation Check

        def validate_countermeasureRule(countermeasureRule : dict):
            """
            Validate Countermeasure Rule 

            Parameters:
            -----------
            countermeasureRule : dict
                Countermeasure rule which should be validated.
            """
            self.validate_vnis(countermeasureRule["vni"])
            validate_vni_access_for_tenant(countermeasureRule["vni"])
            self._validate_ip(countermeasureRule["src_ip"])
            self._validate_ip(countermeasureRule["dst_ip"])
            self._validate_port_number(countermeasureRule["src_port"])
            self._validate_port_number(countermeasureRule["dst_port"])
            self._validate_ip_proto_number(countermeasureRule["ip_proto"])
            validate_countermeasureAction(countermeasureRule["action"])
            return True
        
        def validate_defaultAction(defaultAction):
            """
            Validate the default action used for flow filtering.

            Parameters:
            -----------
            defaultAction : str
                Name of the default action which should be used and validated
            """
            try: 
                validate_countermeasureAction(defaultAction)
                self.logger.debug(log_prefix + "Default CountermeasureAction valid!")
                return True
            except ValueError:
                raise TDCValidationException(log_prefix + "Default CountermeasureAction not valid")

        def validate_countermeasureAction(action):
            """
            Validate countermeasure action for flow filtering.

            Parameters:
            -----------
            action : str
                Name of the filtering action which should be used and validated
            """
            try: 
                CountermeasureAction(action)
                self.logger.debug(log_prefix + "CountermeasureAction valid!")
                return True
            except ValueError:
                raise TDCValidationException(log_prefix + "CountermeasureAction not valid")
        
        def validate_countermeasureRules(countermeasureRules):
            """
            Validate countermeasure rules in the submitted TDC.

            Parameters:
            -----------
            countermeasureRules : list
                List of filtering rules which should be validated.
            """
            for rule in countermeasureRules:
                if rule:
                    validate_countermeasureRule(rule)
            self.logger.debug(log_prefix + "rules valid!")
        
        def validate_countermeasureRulesPart(countermeasureRules):
            """
            Validate countermeasure part in the TIL. 

            Parameters:
            -----------
            countermeasureRules : dict
                Contains the filtering rules part which should be validated.
            """
            validate_defaultAction(countermeasureRules["defaultAction"])
            validate_countermeasureRules(countermeasureRules["rules"])

        def validate_runtimeRules(runtimeRules):
            """
            Validate runtime rules which should be applied for the submitted TDC.

            Parameters:
            -----------
            runtimeRules : list
                Contains runtime rules list which should be validated
            """
            for rule in runtimeRules:
                validate_runtimeRule(rule)
            self.logger.debug(log_prefix + "runtimeRules valid!")
        
        def validate_runtimeRule(runtimeRule):
            """
            Validate single runtime rule which is part in the submitted TDC.

            Parameters:
            -----------
            runtimeRule : dict
                Runtime rule which should be validated.
            """
            validate_actionName(runtimeRule["actionName"], self.inc["mainIngressName"])
            validate_tableName(runtimeRule["table"], self.inc["mainIngressName"])
            validate_matchKeys(runtimeRule["match"])
            validate_actionParams(runtimeRule["actionParams"])
        
        def validate_actionName(actionName, mainIngressName):
            """
            Validate action name for access violations in the TIL.

            Parameters:
            -----------
            actionName : str
                Action name used in this rule of this TDC.
            mainIngressName : str
                Main ingress name used in this TDC.
            """
            ingressName = actionName.split(".")[0]
            if ingressName != mainIngressName:
                raise TDCValidationException("Ingress name of action name does not match the specified ingress for the TDC!")
            return True

        def validate_tableName(tableName, mainIngressName):
            """
            Validate table name which should be in the specified main ingress name to prevent access violations.
            
            Parameters:
            -----------
            tableName : str
                table name used in this rule of this TDC.
            mainIngressName : str
                Main ingress name used in this TDC.
            """
            ingressName = tableName.split(".")[0]
            if ingressName != mainIngressName:
                raise TDCValidationException("Ingress name of table does not match the specified ingress for the TDC!")
            return True

        def validate_actionParams(actionParams : str):
            """
            Validate the action param fields for a table to be in the valid format. 

            Parameters:
            -----------
            actionParams : str
                action parameter dictionary in string form
            """
            regex = re.compile("{ .* }")
            actionParams_check = regex.search(actionParams)
            if actionParams_check:
                raise TDCValidationException("actionParams fields is not valid!")
            return True

        def validate_matchKeys(matchKeys : str):
            """
            Validate the match key parameter fields for a table to be in the valid format. 

            Parameters:
            -----------
            matchKeys : str
                match key parameter dictionary in string form for a table
            """
            regex = re.compile("{ .* }")
            matchKeys_check = regex.search(matchKeys)
            if matchKeys_check:
                raise TDCValidationException("matchKeys fields is not valid!")
            return True

        log_method = ""
        try:
            log_method = log_prefix + "accessRules: "
            validate_accessRules(self.til["accessRules"])
            log_method = log_prefix + "countermeasureRules: "
            validate_countermeasureRulesPart(self.til["countermeasureRules"])
            log_method = log_prefix + "runtimeRules: "
            validate_runtimeRules(self.til["runtimeRules"])
        except TypeError as e:
            self.logger.error("TypeError in " + log_method + e.__str__())
        self.logger.info("TIL validated!")

    def generate_blacklist_for_mainIngressNames(self):
        """
        Generate Blacklist for main ingress names for violation checks and to get an unique set which name are not valid for the submitted TDC.
        """
        blockedMainIngressNames = []
        for tenantId, data in self.tenant_security_config.items():
            if int(tenantId) != self.tdc_id:
                blockedMainIngressNames.extend(data["mainIngressNames"])
        return blockedMainIngressNames


    def validate_inc(self, update_request = False):
        """
        Validate In-Network Code which is an Offloaded Tenant Function (OTF)

        Parameters: 
        -----------
        update_request : bool
            If this is true, it can exist for the specified tenant and should be checked, if it is only updating its TDC.
        """
        log_prefix = "INC" + " - "

        def check_register_access_violation(p4Code, tenantMainIngressNames):
            """
            Check for register access violations in the provided OTF p4 code.

            Parameters:
            -----------
            p4Code : str
                String with the whole OTF code which should be checked for access violations.
            tenantMainIngressNames : str
                The main ingress name for this submitted TDC
            """
            if len(tenantMainIngressNames) > 0: 
                # print(tenantMainIngressNames)
                regex_string = "\.|".join(tenantMainIngressNames)
                regex = re.compile(regex_string)
                r_access_violation = regex.search(p4Code)
                if r_access_violation:
                    self.logger.error("Unallowed register access in OTF found!")
                    raise TDCValidationException("Unallowed register access in OTF found!")
            return True

        def check_table_access_violation(p4Code, tenantMainIngressNames):
            """
            Check for table access violations in the provided OTF p4 code.

            Parameters:
            -----------
            p4Code : str
                String with the whole OTF code which should be checked for access violations.
            tenantMainIngressNames : str
                The main ingress name for this submitted TDC
            """
            if len(tenantMainIngressNames) > 0: 
                regex_string = "\.|".join(tenantMainIngressNames)
                regex = re.compile(regex_string)
                t_access_violation = regex.search(p4Code)
                if t_access_violation:
                    self.logger.error("Unallowed table access in OTF found!")
                    raise TDCValidationException("Unallowed table access in OTF found!")
            return True
        
        def check_include_access_violation(p4Code):
            """
            Check for include access violations in the provided OTF p4 code.
            No include statements in the OTF code is allowed in this implementation.

            Parameters:
            -----------
            p4Code : str
                String with the whole OTF code which should be checked for access violations.
            tenantMainIngressNames : str
                The main ingress name for this submitted TDC
            """
            regex = re.compile('#include \w*')
            include_check = regex.search(p4Code)
            if include_check:
                self.logger.error("Unallowed include statement in OTF found!")
                raise TDCValidationException("Unallowed include statement in OTF found!")
            return True

        def check_extern_access_violation(p4Code, extern_blacklist):
            """
            Check for extern access violations in the provided OTF p4 code.
            At the moment, there are no extern statements in the blacklist.

            Parameters:
            -----------
            p4Code : str
                String with the whole OTF code which should be checked for access violations.
            tenantMainIngressNames : str
                The main ingress name for this submitted TDC
            """
            regex_string = "|".join(extern_blacklist)
            if regex_string != "":
                self.logger.debug("Regex_string: " + regex_string)
                regex = re.compile(regex_string)
                extern_check = regex.search(p4Code)
                self.logger.debug("extern_check:" + str(extern_check))
                if extern_check:
                    self.logger.error("Unallowed extern statement in OTF found!")
                    raise TDCValidationException("Unallowed extern statement in OTF found!")
            return True

        try:
            if not self.validate_unique_mainIngressName(self.inc["mainIngressName"], update_request):
                raise INCIngressNameException("Name of Main Ingress is not unique!")
            if self.inc["mainIngressName"] not in self.tenant_security_config[str(self.tdc_id)]["mainIngressNames"]: 
                self.tenant_security_config[str(self.tdc_id)]["mainIngressNames"].append(self.inc["mainIngressName"])
            blockedList = self.generate_blacklist_for_mainIngressNames()
            check_include_access_violation(self.inc["p4Code"])
            check_extern_access_violation(self.inc["p4Code"], self.extern_blacklist[self.tcd["acceleratorType"]])
            check_register_access_violation(self.inc["p4Code"], blockedList)
            check_table_access_violation(self.inc["p4Code"], blockedList)
            self._save_tenant_security_config()
            
        except TypeError as e:
            self.logger.error(log_prefix + e.__str__())
        except Exception as e:
            if self.inc["mainIngressName"] in self.tenant_security_config[str(self.tdc_id)]["mainIngressNames"]:
                self.tenant_security_config[str(self.tdc_id)]["mainIngressNames"].remove(self.inc["mainIngressName"])
                self._save_tenant_security_config()
            raise e
        self.logger.info("INC validated!")


if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    tdcv = TDCValidator()
    logger = logging.getLogger("Tester")
    logger.info("Testing with valid TDC file.")
    tdcv.validate("./test-files/TDC.yaml")