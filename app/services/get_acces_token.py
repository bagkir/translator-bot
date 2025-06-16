import requests

from app.config import settings

from app.config_logger import py_logger

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

authorization_key = settings.AUTH_KEY.get_secret_value()
scope = "GIGACHAT_API_PERS"

payload = {
    'scope': scope
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '38364246-2a3e-401a-941d-a13c9a5a2b7d',
    'Authorization': f'Basic {authorization_key}'
}


def get_token():
    py_logger.debug("Getting access token")

    try:
        return requests.post(url, headers=headers, data=payload, verify=False)
    except Exception as e:
        py_logger.error(f"Getting token error: {e}")
        raise
