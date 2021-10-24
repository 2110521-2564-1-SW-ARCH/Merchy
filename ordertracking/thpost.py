import requests
import json
import os

STATIC_TOKEN = os.getenv("THPOST_STATIC_TOKEN")
test_barcodes = ["EY145587896TH", "RC338848854TH"]

def track_by_barcodes(barcodes):
    my_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJzZWN1cmUtYXBpIiwiYXVkIjoic2VjdXJlLWFwcCIsInN1YiI6IkF1dGhvcml6YXRpb24iLCJleHAiOjE2Mzc3NTM4MjEsInJvbCI6WyJST0xFX1VTRVIiXSwiZCpzaWciOnsicCI6InpXNzB4IiwicyI6bnVsbCwidSI6ImI0ZWViZjJiZTYxYTQ3NTMyNDkzOGFmZjQxZWQ2NTllIiwiZiI6InhzeiM5In19.TN7O77JP_U8R2teWN6Jery372zglxP0InnlLU63srRUeR50UHYIjTs-68PVpzZCwtVF35hhbNz_kwzkUROqXKQ"
    headers = {
        "Authorization": f"Token {my_token}",
        "Content-type": "application/json"
    }
    body = json.dumps({
        "status": "all",
        "language": "TH",
        "barcode": barcodes
    })
    r = requests.post("https://trackapi.thailandpost.co.th/post/api/v1/track", headers=headers, data=body).json()
    if r['status'] == False: return Null
    return r


def get_token(static_token):
    """
    Get a token from TH Postman by supplying the static token

    :param static_token: the static token obtained from TH Postman developer account
    :return: dict containing the token
    """
    headers = {
        "Authorization": f"Token {static_token}",
        "Content-type": "application/json"
    }
    return requests.post("https://trackapi.thailandpost.co.th/post/api/v1/authenticate/token", headers=headers).json()

def get_webhook_token(static_token):
    headers = {
        "Authorization": f"Token {static_token}",
        "Content-type": "application/json"
    }
    return requests.post("https://trackwebhook.thailandpost.co.th/post/api/v1/authenticate/token", headers=headers).json()

def subscribe_barcodes(barcodes):
    webhook_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJzZWN1cmUtYXBpIiwiYXVkIjoic2VjdXJlLWFwcCIsInN1YiI6IkF1dGhvcml6YXRpb24iLCJleHAiOjE2Mzc3NjI0NjAsInJvbCI6WyJST0xFX1VTRVIiXSwiZCpzaWciOnsicCI6InpXNzB4IiwicyI6bnVsbCwidSI6ImI0ZWViZjJiZTYxYTQ3NTMyNDkzOGFmZjQxZWQ2NTllIiwiZiI6InhzeiM5In19.FY_NJJWI7BqHdxtVUM7PZSgnhIyKf7TLR8Jh352n3uNu8R1xuWWsEsxbllogLIS8mbtXXASJWtjjMDejcd_HnA"
    headers = {
        "Authorization": f"Token {webhook_token}",
        "Content-type": "application/json"
    }
    body = json.dumps({
        "status": "all",
        "language": "TH",
        "barcode": barcodes,
        "req_previous_status": False
    })
    return requests.post("https://trackwebhook.thailandpost.co.th/post/api/v1/hook", headers=headers, body=body)