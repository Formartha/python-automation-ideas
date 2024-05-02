import requests


class ProductApi(object):

    def __init__(self, host):
        self.host = host
        self.session = requests.session()

    def users(self, method):
        return self.session.request(method=method, url=self.host, verify=False)