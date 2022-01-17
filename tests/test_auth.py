from smoothcode_auth import SmoothCodeAuth


class TestSmoothCodeAuth:
    def test_is_dashboard_request_with_correct_data(self):
        client_secret = 'client_secret'
        request_hmac = '60586d133f5f8ad570e377a633a63314b02fe423b93e12ca013b1ab3e8d519ef'
        assert SmoothCodeAuth(request_hmac, client_secret).is_dashboard_request('test.myshopify.com')

    def test_is_dashboard_request_with_incorrect_data(self):
        client_secret = 'client_secret'
        request_hmac = 'request_hmac'
        assert not SmoothCodeAuth(request_hmac, client_secret).is_dashboard_request('test.myshopify_com')

    def test_is_webhook_request_with_correct_data(self):
        client_secret = 'client_secret'
        request_hmac = '656718377faf656ccc037d8607ebfe3434197981aa1362db81210252ce92cd5c'
        assert SmoothCodeAuth(request_hmac, client_secret).is_webhook_request({'request': 'webhook'})

    def test_is_webhook_request_with_incorrect_data(self):
        client_secret = 'client_secret'
        request_hmac = 'request_hmac'
        assert not SmoothCodeAuth(request_hmac, client_secret).is_webhook_request({'request': 'webhook'})
