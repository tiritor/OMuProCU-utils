# OMuProCU utils

This repository contains the python package for OMuProCU utilities which was needed for the paper ```Low Impact Tenant Code Updates on Multi-tenant Programmable Switches```.

The core package can be found [here]() 

The package contains the following modules:

- Protobuf Message Descritions for OMuProCU (including [Open-Tofino BarefootRuntime Protobuf](https://github.com/barefootnetworks/Open-Tofino))
- Validator for TDC
- Persistor for OMuProCU states

Also, a [OMuProCU reference client](src/orchestrator_utils/orchestrator_client.py) is implemented for the API, which can be used for deployment submissions to the proposed OMuProCU.

## Installation/Building

Clone this repository recursively:

```
git clone --recurse-submodules https://github.com/tiritor/OMuProCU-utils.git
```

Afterwards, the recommendation is to use a virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

Then build the package and install it.

```
pip3 install -r requirements.txt
python3 setup.py sdist
pip3 install .
```

## Contributing 

### Protobuf 

After applying change to provided protobuf descriptions, the ```generate_protobufs.sh``` script can be used to generate the python protobuf bindings.