from src.Client import Client
import json

with open('data\\config.json') as json_data_file:
    data = json.load(json_data_file)
    token = data['discord']['token']

client = Client()
client.run(token)
