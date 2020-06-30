"""
Default python logic to user Django shell
Filling the database with data collected from api
"""
import requests
from datetime import datetime
from co2_france.models import Co2Emission



resp = requests.get('https://api-recrutement.ecoco2.com/v1/data')
# for item in resp.json():
#
#
# print(len(resp.json()))
# print( os.path.abspath(os.path.dirname(__file__)))
#print(Co2Emission.objects.all())
