#!/usr/bin/env python3

my_route = 'http://licence-plate-workshop-git-licence-plate.apps.lab.ilab.science-computing.de'

import argparse
import base64
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("image", nargs="+")
args = parser.parse_args()

for my_image in args.image:
    with open(my_image, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        content = {"image": encoded_image}
        json_data = json.dumps(content)

    headers = {"Content-Type" : "application/json"}

    r = requests.post(my_route + '/predictions', data=json_data, headers=headers)

    print(my_image, json.loads(r.content.decode())['prediction'])

