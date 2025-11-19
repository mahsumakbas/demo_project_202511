import requests

from wrapper import *




def test_non_exist_petid():

    resp = make_requests("get", "https://petstore.swagger.io/v2/pet/99999999")

    check_status_code(resp, 404)


def test_create_pet():
        
    url_post = "https://petstore.swagger.io/v2/pet"

    post_data = '''
    {
    "id": 0,
    "category": {
        "id": 0,
        "name": "{name}"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 0,
        "name": "string"
        }
    ],
    "status": "available"
    }
    '''

    data_to_be_use = post_data.replace("{name}", "string")

    resp = requests.post(url_post, data=data_to_be_use, headers={"Content-Type": "application/json"})
    assert resp.status_code == 200

    resp_json =  resp.json()

    print(resp_json)
    assert resp_json["category"]["name"] == "string"
    assert resp_json["status"] == "available"