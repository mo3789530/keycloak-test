import uuid
import json 
import requests
from requests.api import get
import time

from requests.models import Response

BASE_URL = "http://localhost:8080"

def laod_json(path):
    json_load = open(path, 'r')
    return json.load(json_load)

def get_token():
    url = f"{BASE_URL}/auth/realms/master/protocol/openid-connect/token"

    realm = "e11b4d17-4278-433a-8b36-52abdb8fb0cf"
    username = "admin"
    password ="Pa55w0rd"
    client_id = "test"
    payload=f'client_secret={realm}&username={username}&password={password}&grant_type=password&client_id={client_id}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("token: " + str(response.elapsed.total_seconds()))
    return response.json()['access_token']

def create_new_realm(id, realm, token):
    payload = { "id": id, "realm" : realm, "enabled" : True }
    url = f"{BASE_URL}/auth/admin/realms"
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, data= json.dumps( payload))
    print(response)
    print("realm: " + str(response.elapsed.total_seconds()))

def create_new_user(realm, user, token):
    url = f"{BASE_URL}/auth/admin/realms/" + realm + "/users"
    payload = {"enabled": True, "attributes": {}, "username": user, "emailVerified": ""}
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, data= json.dumps( payload))
    print(response)

# def create_data(id, data):
#     new_data = data
#     new_data["id"] = id
#     new_data["realm"] = id

#     for d in data["clientScopes"]:
#         d["id"] = str(uuid.uuid4())
#         if("protocolMappers" in d):
#            for d2 in d["protocolMappers"]:
#                d2["id"] = str(uuid.uuid4())
#     for d in data["components"]["org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy"]:
#         d["id"] = str(uuid.uuid4())
#     for d in data["components"]["org.keycloak.keys.KeyProvider"]:
#         d["id"] = str(uuid.uuid4())
#     for d in data["authenticationFlows"]:
#         d["id"] = str(uuid.uuid4())
#     for d in data["authenticatorConfig"]:
#         d["id"] = str(uuid.uuid4())
#     return json.dumps( new_data)

def main():
    print("start")

    create_new_user("master", "test", get_token())
    max = 1100
    start = 1
    while start<max:
        token = get_token()
        create_new_realm(str(start), str(start),  token)
        # create_new_user("master", str(start), get_token())
        start = start + 1
        time.sleep(2)



if __name__ == '__main__':
    main()
