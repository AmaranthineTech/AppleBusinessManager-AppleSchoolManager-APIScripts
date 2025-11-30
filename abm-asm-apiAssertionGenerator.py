#!/usr/bin/env python3

# ****************************************************************************************************
# NAME: 	apiAssertionGenerator.py
# DATE: 	7th October 2025
# ****************************************************************************************************

# ****************************************************************************************************
# ********** DISCLAIMER **********
# --------------------------------
# This script has been sourced from Apple's documentation.
# For more details about this specific script visit: https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-and-business-manager-api
# ****************************************************************************************************

# ****************************************************************************************************
# Usage
# --------------------
# This script requires several resources: 

# ** API Account details **
# - Client ID for the API account.
# - Team ID for the API account. This is the same as the client id.
# - Key ID for the API account. 
# - The private key ending with the extension .pem . ** This private key is to be downloaded when the API account has been created.

# ** Python libraries **
# - authlib
# - Crypto

# ** Installing the python libraries if needed **
# pip3 install authlib
# pip3 install PyCryptodome

# To run the script:
# python3 /path/to/apiAssertionGenerator.py

# Copy the output from stdout. This will be used as the access token while making the API calls.

# This script works with both Apple Business Manager as well as Apple School Manager. Replace all occurances of 'school' with 'business' or the other way round depending on which service you are accessing.
# ****************************************************************************************************

# ****************************************************************************************************
# **WARNING**: Please test the script before using it.
# ****************************************************************************************************

# ****************************************************************************************************
# ********** SCRIPT STARTS HERE **********
# ****************************************************************************************************

import os
import authlib
import Crypto
import datetime as dt
import uuid as uuid
from authlib.jose import jwt
from Crypto.PublicKey import ECC

private_key_file = "/path/to/apidemo.pem"
client_id = "BUSINESSAPI.----------"
team_id = "BUSINESSAPI.----------"
key_id = "----------"
audience = "https://account.apple.com/auth/oauth2/v2/token"
alg = "ES256"

# Define the issue timestamp.
issued_at_timestamp = int(dt.datetime.utcnow().timestamp())

# Define the expiration timestamp, which may not exceed 180 days from the issue timestamp.
expiration_timestamp = issued_at_timestamp + 86400*180

# Define the JWT headers.
headers = dict()
headers['alg'] = alg
headers['kid'] = key_id

# Define the JWT payload.
payload = dict()
payload['sub'] = client_id
payload['aud'] = audience
payload['iat'] = issued_at_timestamp
payload['exp'] = expiration_timestamp
payload['jti'] = str(uuid.uuid4())
payload['iss'] = team_id

# Open the private key.
with open(private_key_file, 'rt') as file:
	private_key = ECC.import_key(file.read())
	
# Encode the JWT and sign it with the private key.
client_assertion = jwt.encode(
	header=headers,
	payload=payload,
	key=private_key.export_key(format='PEM')
).decode('UTF-8')

# Save the client assertion to a file.
with open('client_assertion.txt', 'w') as output:
	output.write(client_assertion)
	
# ****************************************************************************************************
# ********** SCRIPT ENDS HERE **********
# ****************************************************************************************************
