import json
import urllib.request
import urllib.parse
import csv
import os
import pyodbc
from datetime import datetime

tenantId = 'abc123' # Paste your own tenant ID here
appId = 'abc123' # Paste your own app ID here
appSecret = 'abc123' # Paste your own app secret here
date = datetime.now().strftime("%Y_%m_%d")
server = 'tcp:192.168.1.1' # Paste your DB IP address here
database = 'MSDefenderAnalyst' # Paste your DB Name that you created in DB here
username = 'admin' # Paste the account that you will use to login and write date into here
password = '1234567' # Paste the password that you will use to login and write date into here

#DB driver Definition from Python library
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

url = "https://login.microsoftonline.com/%s/oauth2/token" % (tenantId)

resourceAppIdUri = 'https://api.securitycenter.microsoft.com'

body = {
    'resource' : resourceAppIdUri,
    'client_id' : appId,
    'client_secret' : appSecret,
    'grant_type' : 'client_credentials'
}


data = urllib.parse.urlencode(body).encode("utf-8")

req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
jsonResponse = json.loads(response.read())
aadToken = jsonResponse["access_token"]


#print(aadToken) #To Check the raw token value, for Debugging.

queryFile = open(r'C:\...\...\AdvancedHuntingScript.txt') # Absolute Path To Open the AdvancedHunting script. Welcome to modify it to be your parameter.
query = queryFile.read()
queryFile.close()

#print(query)

url = "https://api.securitycenter.microsoft.com/api/advancedqueries/run"

headers = {
    'Content-Type' : 'application/json',
    'Accept' : 'application/json',
    'Authorization' : "Bearer " + aadToken
}

data = json.dumps({ 'Query' : query }).encode("utf-8")

req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
jsonResponse = json.loads(response.read())
schema = jsonResponse["Schema"]
results = jsonResponse["Results"]

#print(results) #To Check the raw data, for Debugging.

#Below starting the code to write the data into your database. You will need to check the table name(s) and the column name(s) to match your instance.
cursor = conn.cursor()

a = [value1['DeviceName'] for value1 in results if 'DeviceName' in value1]
b = [value2['OSPlatform'] for value2 in results if 'OSPlatform' in value2]
c = [value3['CveId'] for value3 in results if 'CveId' in value3]
d = [value4['SoftwareName'] for value4 in results if 'SoftwareName' in value4]
e = [value5['SoftwareVersion'] for value5 in results if 'SoftwareVersion' in value5]
f = [value6['SoftwareVendor'] for value6 in results if 'SoftwareVendor' in value6]
g = [value7['VulnerabilitySeverityLevel'] for value7 in results if 'VulnerabilitySeverityLevel' in value7]
h = [value8['RecommendedSecurityUpdate'] for value8 in results if 'RecommendedSecurityUpdate' in value8]
i = [value9['RecommendedSecurityUpdateId'] for value9 in results if 'RecommendedSecurityUpdateId' in value9]


number_of_c = len(c)
print(number_of_c)
cursor.execute("INSERT INTO _BitFlow_TimeSeries (Total, DT) VALUES (?, GETUTCDATE())", number_of_c)
cursor.execute("DELETE FROM _BitFlow_")

z = -1
for a1 in a:
    z+=1
    b1 = b[z]
    c1 = c[z]
    d1 = d[z]
    e1 = e[z]
    f1 = f[z]
    g1 = g[z]
    h1 = h[z]
    i1 = i[z]
    #Check the table names and column names are matched yours.
    cursor.execute("INSERT INTO _BitFlow_ (DeviceName, OSPlatform, CveID, SoftwareName, SoftwareVersion, SoftwareVendor, VulnerabilitySeverityLevel, RecommendedSecurityUpdate, RecommendedSecurityUpdateId, DT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, GETUTCDATE())", a1, b1, c1, d1, e1, f1, g1, h1, i1)
    
conn.commit()
cursor.close()
#End of the DB Writting Connection