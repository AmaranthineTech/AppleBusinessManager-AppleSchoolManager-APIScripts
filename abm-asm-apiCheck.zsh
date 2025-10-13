#!/bin/zsh

# ****************************************************************************************************
# NAME: 	apiCheck.zsh
# AUTHOR:	Arun Patwardhan
# DATE: 	7th October 2025
# CONTACT:	arun@amaranthine.co.in
# ****************************************************************************************************

# ****************************************************************************************************
#MIT License
#
#Copyright (c) 2025 Amaranthine
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
# ****************************************************************************************************

# ****************************************************************************************************
# Usage
# --------------------
# This script requires the access token for authorization. Please run the bearerToken.zsh script first to get that. 
#
# To run the script:
# /bin/zsh /path/to/script/bearerToken.zsh
#
# This script works with both Apple Business Manager as well as Apple School Manager. Replace all occurances of 'school' with 'business' or the other way round depending on which service you are accessing.
# ****************************************************************************************************

# ****************************************************************************************************
# **WARNING**: Please test the script before using it.
# ****************************************************************************************************

# ****************************************************************************************************
# ********** SCRIPT STARTS HERE **********
# ****************************************************************************************************

ACCESS_TOKEN="----------"

#1. Get all devices
# --------------------
/usr/bin/curl -X GET "https://api-school.apple.com/v1/orgDevices" -H "Authorization: Bearer ${ACCESS_TOKEN}"

#2. Get specific device
# --------------------
/usr/bin/curl -X GET "https://api-school.apple.com/v1/orgDevices/----------" -H "Authorization: Bearer ${ACCESS_TOKEN}"

#3. Get MDM servers
# --------------------
/usr/bin/curl -X GET "https://api-school.apple.com/v1/mdmServers" -H "Authorization: Bearer ${ACCESS_TOKEN}"

# ****************************************************************************************************
# ********** SCRIPT ENDS HERE **********
# ****************************************************************************************************