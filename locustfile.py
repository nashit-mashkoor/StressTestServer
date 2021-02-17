import requests
import json
import base64
from timeit import default_timer as timer
import glob
from locust import HttpUser, task

class MyUser(HttpUser):

    @task
    def task1(self):
    
        image_path='./1.jpg'
        # prepare headers for http request
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
    
        # with open("imgs/1.jpg", "rb") as image_file:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        # encode image as jpeg
        response = self.client.post('/', data=encoded_string, headers=headers)
        # self.client.get('/')