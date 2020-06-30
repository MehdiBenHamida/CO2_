import requests
from datetime import datetime
from .src.co2.co2_france.models import Co2Emission


resp = requests.get('https://api-recrutement.ecoco2.com/v1/data')
if resp.status_code != 200:
    raise Exception("GET: /v1/data returned {}".format())
for item in resp.json():
    Co2Emission.objects.create(
        datetime=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S'),
        co2_rate=item['co2_rate'])

print("{} new entries has been creates.".format(len(resp.json())))
