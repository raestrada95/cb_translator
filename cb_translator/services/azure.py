import requests
import uuid
import json
import os.path


class Azure_auth:
    def __init__(self):
        self.azure_key = "~/azure_key"
        self.path = os.path.expanduser(self.azure_key)

    def save_key(self):
        try:
            key = input("Enter your azure key: ")
            with open(self.path, 'w') as f:
                f.write(key)
            return key
        except IOError:
            return None

    def read_key(self):
        try:
            with open(self.path, 'r') as f:
                self.key = f.read()

            return self.key

        except FileNotFoundError:
            self.key = self.save_key()

            return self.key


def azure_translator(text, lang):
    # Add your key and endpoint
    key = Azure_auth().read_key()
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "northcentralus"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': [lang],
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return (response[0]['translations'][0]['text'])