import requests

def make_requests(method, url, data=None, json=None, headers=None):
    resp = requests.request(method, url, data=data, json=json, headers=headers)
    return resp

def check_status_code(resp, expected_status):
    assert resp.status_code == expected_status