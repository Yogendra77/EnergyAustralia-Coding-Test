import requests
import json
from jsonschema import validate


print('\n*****Start of program*****\n')

band_name = ""

response = requests.get("https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals")

assert response.status_code == 200, "Invalid response code returned: {0}".format(response.status_code)

if(response.text == '""'):
    try:
        assert response.text != '""', "No data in the response"
    except:
        print("<<<<<<-------------------------------------------------------------------------------------->>>>>>")
        print("Warning: Server completed the request as expected, however, there is no data in the response!\n")
        print("<<<<<<-------------------------------------------------------------------------------------->>>>>>")

else:
    json_response = response.json()
    for item in json_response:
        print(item)

        try:
            festival_name = item["name"]
            assert festival_name != "", "Empty festival name for the above record"
        except:
            print("\nWarning: This record has no MusicFestival name \n")

        try:
            for band in item["bands"]:
                band_name = band["name"]
                assert band_name != "", "Empty band name"
                band_recordlabel = band["recordLabel"]
                assert band_recordlabel != "", "Empty band recordLabel for band: '{0}'".format(band_name)
            print("<<<<<<-------------------------------------------------------------------------------------->>>>>>")
        except:
            print("\nWarning: This record has missing Band Details Data for " + "(" + band_name + ")\n")
            print("<<<<<<-------------------------------------------------------------------------------------->>>>>>")

print('\n*****End of program*****')
