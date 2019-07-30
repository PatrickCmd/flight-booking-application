import json
from locust import HttpLocust, TaskSet, task


class FBSAPIUserActions(TaskSet):
    def __init__(self, parent):
        super(FBSAPIUserActions, self).__init__(parent)
        self.email = "locust_user@locust.com"
        self.password = "Locust1234#"
        self.token = None
        self.headers = {}

    def on_start(self):
        self.token = self.login()
        self.headers = {"Authorization": f"JWT-TOKEN {self.token}"}

    def on_stop(self):
        pass

    def login(self):
        # login into the application
        response = self.client.post(
            "/fbs-api/users/login/", {"email": self.email, "password": self.password}
        )
        return json.loads(response._content)["user"]["token"]

    @task(1)
    def show_flights(self):
        self.client.get("/fbs-api/flights/", headers=self.headers)

    @task(2)
    def reserve_flight(self):
        flights_res = self.client.get("/fbs-api/flights/", headers=self.headers)
        flights_data = json.loads(flights_res._content)

        if flights_data:
            flight = flights_data['flights'][0]

            self.client.post(
                f'/fbs-api/flights/{flight["id"]}/reservations',
                {"seat": "A2"},
                headers=self.headers,
            )


class APIUser(HttpLocust):
    task_set = FBSAPIUserActions
    min_wait = 5000
    max_wait = 9000
