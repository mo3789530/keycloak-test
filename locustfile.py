from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def token(self):
        payload='client_secret=5b5b6b2f-313f-4663-9409-15f497451cf1&username=user&password=user&grant_type=password&client_id=test'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.client.post("/auth/realms/test/protocol/openid-connect/token", headers=headers, data=payload, verify=False,)

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(0)


