CURL_CA_BUNDLE = ""
import os
import requests
import certifi
from azureml.core import Workspace
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

proxy = "https://10.52.0.202:8080"
print("setting proxy environment variable ")
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

# Adding custom certificate to certs store**************
# print("Using the following certificate:")
# print(certifi.where())
# # adding defence CA to certificate store
# print('Now adding custom certs to Certifi store...')
# cafile = certifi.where()
# with open('new_cert.pem', 'rb') as infile:
#     customca = infile.read()
# with open(cafile, 'ab') as outfile:
#     outfile.write(customca)
# print(certifi.where())
# print('custom CA now added.')
# *****************************************

r = requests.get("https://xkcd.com/1906/", verify=False)
print(r.status_code)

# connecting to existing workspace through config file
ws = Workspace.from_config("azureml/config.json")
