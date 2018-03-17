#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Support Python3 in Python2.
from __future__ import print_function

# All the shared functions are in this package.
from zeservices import ZEServices

import json

# We play with encodings so it's good to check what we are set to support.
import locale

# Load credentials.
in_file = open('credentials.json', 'r')
credentials = json.load(in_file)
in_file.close()

# Get the VIN.
vin = credentials['VIN']

# Create a ZE Services object.
zeServices = ZEServices(credentials['ZEServicesUsername'], credentials['ZEServicesPassword'])

# ZE Services vehicle status.
zeServices_json = zeServices.apiCall('/api/vehicle/' + vin + '/battery')