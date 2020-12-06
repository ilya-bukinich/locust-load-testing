import time
from locust import HttpUser, task


class TestUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")

    @task(5)
    def view_book(self):
        for i in range(1, 6):
            self.client.get("/catalog/book/%i" % i, name="/catalog/book/%i" % i)
            time.sleep(1)

    @task(5)
    def view_author(self):
        for i in range(1, 6):
            self.client.get("/catalog/author/%i" % i, name="/catalog/author/%i" % i)
            time.sleep(1)
