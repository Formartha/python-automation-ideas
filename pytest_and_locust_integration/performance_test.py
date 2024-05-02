from locust import HttpUser, task, between
from api import ProductApi


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def api(self):
        lo_client = ProductApi("https://66333084f7d50bbd9b487735.mockapi.io/api/v1/users")
        lo_client.session = self.client
        print(lo_client.users("GET").status_code)