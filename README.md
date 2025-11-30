# AppleBusinessManager-AppleSchoolManager-APIScripts

This repository contains the script files for using the Apple Business Manager/Apple School Manager API.

## Scripts
The apiAssertionGenerator.py and the bearerToken.zsh scripts are based of the scripts made available in Apple's documentation. For more details about this specific script visit: https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-and-business-manager-api

## Dependencies
### Python
You will need to install Python on your Mac. You can download it from here: https://www.python.org/downloads/

### Python libraries
You will need to install ```python authlib``` and ```python Crypto``` libraries. To do that run the following commands in terminal.

```shell
pip3 install authlib

pip3 install PyCryptodome
```

### Running the assertionGenerator

Access the Client ID, Key ID, and Team ID from your Apple Business Manager/Apple School Manager API account details. Place them in the appropriate variables.

```shell
python3 /path/to/abm-asm-apiAssertionGenerator.py
```

This will create and save the file in the current working directory.

### Running the bearer toke script

Copy the client assertion generated from the previous script into the client_assertion variable.

```shell
/bin/zsh /path/to/abm-asm-bearerToken.zsh
```

The bearer token is sent stdout. Copy it and use it in the apiCheck script.

**NOTE**
_*Make sure that you replaces all occurances of 'school' with 'business' or the other way round depending on whether you are accessing Apple School Manager or Apple Business Manager. This is a common cause of errors. This must be done on all the scripts.*_
