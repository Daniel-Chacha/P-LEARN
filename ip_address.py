import os
import json
import urllib.request as urlib2

#use while loop to continuously prompt the user for the target IP address
while True:
    # prompt the user to input the target IP address
    ip=input('What is your target IP: ')

    #construct the url for the ip+api.com JSON API
    url='https://ip-api.com/json/'

    #send a request to the ip-api.com API to retrieve the  geological information
    response=urlib2.urlopen(url +ip)

    #read the response data
    data=response.read()

    #parse the JSON response data into a python dictionary
    values=json.loads(data)

    #print the geolocation information for the target IP address
    print('IP: ' +values['query'])
    print('City '+values['city'])
    print('ISP: '+values['isp'])
    print('Country: '+values['country'])
    print('Region '+values['region'])
    print('Timezone '+values['timezone'])