import requests
import json

class WazirxClient:
    """API-ENDPOINTS-STARTS"""

    BASE_URL = 'https://x.wazirx.com/'
    LOGIN_ENDPOINT = 'wazirx-falcon/api/v1.0/login'
    VERIFY_LOGIN_ENDPOINT = 'wazirx-falcon/api/v1.0/login-verify-2fa'
    GLOBAL_CONIFG_ENDPOINT = 'api/v2/global_configs'

    """API-ENDPOINTS-ENDS"""

    def __init__(self) -> None:
        self.req = requests.Session()

    def get_global_config(self):
        resp = self.req.get(self.BASE_URL+self.GLOBAL_CONIFG_ENDPOINT)
        return resp.json()
