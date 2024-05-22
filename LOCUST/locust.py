from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def view_posts(self):
        self.client.get("/")

    @task(3)
    def submit_post(self):
        self.client.post("/post", {
            "title": "Load Test",
            "content": "This is a test post generated during a load test."
        })
