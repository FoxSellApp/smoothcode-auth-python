import json

from .utils import generate_hmac


class SmoothCodeAuth:
    def __init__(self, request_hmac: str, client_secret: str):
        self.hmac = request_hmac
        self.client_secret = client_secret

    def is_dashboard_request(self, shop: str):
        return generate_hmac(self.client_secret, shop) == self.hmac

    def is_webhook_request(self, webhook_data: dict):
        stringfied_webhook_data = json.dumps(webhook_data)
        return generate_hmac(self.client_secret, stringfied_webhook_data) == self.hmac
