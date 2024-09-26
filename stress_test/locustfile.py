from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    @task
    def index(self):
        self.client.get("/index")

    @task
    def predict(self):
        self.client.post("/predict", json={"data": [1, 2, 3, 4]})
