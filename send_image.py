#!/usr/bin/env python

my_image = 'car.jpg'
my_route = 'http://licence-plate-workshop-git-licence-plate.apps.lab.ilab.science-computing.de'

import base64
import requests
from json import dumps

with open(my_image, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
content = {"image": encoded_image}
json_data = dumps(content)

headers = {"Content-Type" : "application/json"}

r = requests.post(my_route + '/predictions', data=json_data, headers=headers)

print(r.content)
