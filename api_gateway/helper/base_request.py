import json
import requests
from api_gateway.constant.constant import SERVICE_LIST, SERVICE_URL

def request_service(service, user_id, method, params: list=None):
    # validate params
    if service not in SERVICE_LIST:
        return {"status":400, "message":"service not valid"}
    try:
        url = SERVICE_URL[service]
        headers = {'Content-Type': 'application/json'}
        payload = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': user_id
        }
        response = requests.post(url, json=payload, headers=headers)
        string_response = response.content.decode('utf-8')
        data_response = json.loads(string_response)
        return data_response['result']
    except Exception as e:
        return e