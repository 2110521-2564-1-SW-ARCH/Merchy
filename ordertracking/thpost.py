import requests


def get_shipping_status_by_barcode():
    my_token = ""
    headers = {
        "Authorization": f"Token {my_token}",
        "Content-type": "application/json"
    }
    body = {
        "status": "all",
        "language": "TH",
        "barcode": [
            "EY145587896TH",
            "RC338848854TH"
        ]
    }
    return requests.post("https://trackapi.thailandpost.co.th/post/api/v1/track", headers=headers, data=body)


def get_token(token):
    headers = {
        "Authorization": f"Token {token}",
        "Content-type": "application/json"
    }
    return requests.post("https://trackapi.thailandpost.co.th/post/api/v1/authenticate/token", headers=headers).json()
