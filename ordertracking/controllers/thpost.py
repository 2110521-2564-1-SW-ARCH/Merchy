import requests
import json
import os
from models import token as Token

STATIC_TOKEN = os.getenv("THPOST_STATIC_TOKEN")
test_barcodes = ["EY145587896TH", "RC338848854TH"]


def track_by_barcodes(barcodes):
    request_token = Token.get_dynamic_token(Token.Type.THPOST_REQUEST_TOKEN)
    headers = {
        "Authorization": f"Token {request_token}",
        "Content-type": "application/json",
    }
    body = json.dumps({"status": "all", "language": "TH", "barcode": barcodes})
    r = requests.post(
        "https://trackapi.thailandpost.co.th/post/api/v1/track",
        headers=headers,
        data=body,
    ).json()
    if r["status"] == False:
        return None
    return r


def get_token(static_token):
    """
    Get a token from TH Postman by supplying the static token

    :param `static_token`: the static token obtained from TH Postman developer account
    :return: dict containing the token
    """
    headers = {
        "Authorization": f"Token {static_token}",
        "Content-type": "application/json",
    }
    token = requests.post(
        "https://trackapi.thailandpost.co.th/post/api/v1/authenticate/token",
        headers=headers,
    ).json()
    return Token.insert_or_update(Token.Token(**token, type=Token.Type.THPOST_REQUEST_TOKEN))


def get_webhook_token(static_token):
    headers = {
        "Authorization": f"Token {static_token}",
        "Content-type": "application/json",
    }
    token = requests.post(
        "https://trackwebhook.thailandpost.co.th/post/api/v1/authenticate/token",
        headers=headers,
    ).json()
    return Token.insert_or_update(Token.Token(**token, type=Token.Type.THPOST_WEBHOOK_TOKEN))


def subscribe_barcodes(barcodes):
    webhook_token = "test"
    headers = {
        "Authorization": f"Token {webhook_token}",
        "Content-type": "application/json",
    }
    body = json.dumps(
        {
            "status": "all",
            "language": "TH",
            "barcode": barcodes,
            "req_previous_status": False,
        }
    )
    return requests.post(
        "https://trackwebhook.thailandpost.co.th/post/api/v1/hook",
        headers=headers,
        body=body,
    )