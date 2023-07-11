

from itertools import count
import os
import pickle

from ..logger.logger import init_logger


class ReconfigSchedulerStorage(object):
    """
    Key Value Storage Reference Implementation for the Reconfiguration Scheduler.
    """
    nos_scheduled_configs = {}
    in_scheduled_configs = {}
    scheduled_updateActions = {}
    scheduled_deployment_status = {}

    def __str__(self) -> str:
        return {
            "nos_scheduled_configs": self.nos_scheduled_configs, 
            "in_schedulued_configs": self.in_scheduled_configs,
            "scheduled_updateActions": self.scheduled_updateActions,
            "scheduled_deployment_status": self.scheduled_deployment_status        
        }.__str__()

    def add(self, key, updateAction, nos_config, in_config, scheduleStatus):
        """
        Add a new Reconfiguration to schedule. If an option is not provided, any defined options will be updated.
        """
        if updateAction is not None:
            self.scheduled_updateActions.update({key: updateAction})
        if nos_config is not None:
            self.nos_scheduled_configs.update({key: nos_config})
        if in_config is not None:
            self.in_scheduled_configs.update({key: in_config})
        if scheduleStatus is not None:
            self.scheduled_deployment_status.update({key: scheduleStatus})

    def delete(self, key):
        """
        Delete the key in all storages if available.

        Parameters:
        -----------
        key : str
            Tenant CNF ID (ID + Function Name) to be deleted in the storages.
        """
        if key in self.nos_scheduled_configs.keys():
            self.nos_scheduled_configs.pop(key)
        if key in self.in_scheduled_configs.keys():
            self.in_scheduled_configs.pop(key)
        if key in self.scheduled_deployment_status.keys():
            self.scheduled_deployment_status.pop(key)
        if key in self.scheduled_updateActions.keys():
            self.scheduled_updateActions.pop(key)

    def cleanup(self):
        """
        Cleanup all storages.
        """
        self.nos_scheduled_configs.clear()
        self.in_scheduled_configs.clear()
        self.scheduled_deployment_status.clear()
        self.scheduled_updateActions.clear()

    def checkKey(self, key, storage_name=None):
        """
        Check if key is available in one or all storages.

        Parameters:
        -----------
        key : str
            Tenant CNF ID (ID + Function Name) to be deleted in the storages.
        storage_name : str
            Name of the storage where the key should be searched. If it is None, check in all storages.
        """
        if storage_name is None:
            exist_in_scheduled_configs = key in self.in_scheduled_configs.keys() 
            exist_nos_scheduled_configs = key in self.nos_scheduled_configs.keys() 
            exist_scheduled_deployment_status = key in self.scheduled_deployment_status.keys()
            exist_scheduled_updateActions = key in self.scheduled_updateActions.keys()
            exists = [int(exist_in_scheduled_configs), int(exist_nos_scheduled_configs), int(exist_scheduled_deployment_status), int(exist_scheduled_updateActions)]
            if sum(exists) == len(exists) or sum(exists) == 0:
                return any(exists)
            else:
                raise ValueError("Key does not exists in all RSS dicts.")
        elif storage_name == "nos_scheduled_configs":
            return key in self.nos_scheduled_configs.keys()
        elif storage_name == "in_scheduled_configs":
            return key in self.in_scheduled_configs.keys()
        elif storage_name == "scheduled_updateActions":
            return key in self.scheduled_updateActions.keys()
        elif storage_name == "scheduled_deployment_status":
            return key in self.scheduled_deployment_status.keys()
        else:
            raise ValueError("Key not found!")

RSS = ReconfigSchedulerStorage()

class Persistor(object):
    """
    Persistor to save states of a component
    """
    def __init__(self, persistence_path, persistence_file, caller=None) -> None:
        self.persistence_path = persistence_path
        self.persistence_file = persistence_file
        self.persistence = self.persistence_path + "/" + self.persistence_file
    
    def create_persistence_paths(self):
        """
        Create state persistence paths if they are not existing
        """
        if not os.path.exists(os.path.dirname(self.persistence)):
            os.makedirs(os.path.dirname(self.persistence))
            return True
        return False
    
    def store_to_persistence(self, state_data):
        """
        Persist state of component.
        """
        self.logger.debug("Store tenant states to {}".format(self.persistence))
        with open(self.persistence, "wb") as f:
            pickle.dump(state_data, f)

    def read_from_persistence(self, default=dict):
        """
        Read persisted state of component.
        """
        if os.path.exists(self.persistence):
            self.logger.debug("Loading persisted tenants from {}".format(self.persistence))
            with open(self.persistence, "rb") as f:
                try:
                    state_data = pickle.load(f)
                    if state_data is None:
                        return default()
                    return state_data 
                except EOFError:
                    self.logger.warn("Read empty file --> Resetted to empty dict.")
                    return default()
                except TypeError:
                    self.logger.warn("Read empty file --> Resetted to empty dict.")
                    return default()
        else:
            self.logger.warning("Could not open {}: No such file or directory.".format(self.persistence))
            return default()