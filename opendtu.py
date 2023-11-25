# Import the requests library
import requests
from requests.auth import HTTPBasicAuth

"""
GET/POST 	Auth required 	URL
Get 	yes 	/api/config/get
Post 	yes 	/api/config/delete
Get 	yes 	/api/config/list
Post 	yes 	/api/config/upload
Get+Post 	yes 	/api/device/config
Get 	no 	/api/devinfo/status
Get+Post 	yes 	/api/dtu/config
Get 	no 	/api/eventlog/status?inv=inverter-serialnumber
Post 	yes 	/api/firmware/update
Get 	yes 	/api/inverter/list
Post 	yes 	/api/inverter/add
Post 	yes 	/api/inverter/del
Post 	yes 	/api/inverter/edit
Post 	yes 	/api/limit/config
Get 	no 	/api/limit/status
Get 	no 	/api/livedata/status
Post 	yes 	/api/maintenance/reboot
Get+Post 	yes 	/api/mqtt/config
Get 	no 	/api/mqtt/status
Get+Post 	yes 	/api/network/config
Get 	no 	/api/network/status
Get+Post 	yes 	/api/ntp/config
Get 	no 	/api/ntp/status
Get+Post 	yes 	/api/ntp/time
Get 	no 	/api/power/status
Post 	yes 	/api/power/config
Get 	no 	/api/prometheus/metrics
Get+Post 	yes 	/api/security/config
Get 	yes 	/api/security/authenticate
Get 	no 	/api/system/status
"""


# Define a class for the API
class OpenDTU_API:
    # Initialize the class with the base URL, user and password
    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password

    # Define a method to get the status
    def get_data(self, api_call):
        # Construct the full URL
        url = self.base_url + api_call
        # Send a GET request
        response = requests.get(
            url, stream=True, auth=HTTPBasicAuth(self.user, self.password)
        )
        # Return the response content as a string
        return response.text

    def post_data(self, api_call, todo):
        # Construct the full URL
        url = self.base_url + api_call
        # Set the content type
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        # Construct the data
        data = "data=" + todo
        # Send a Post request
        response = requests.post(
            url,
            stream=True,
            auth=HTTPBasicAuth(self.user, self.password),
            data=data,
            headers=headers,
        )
        # Return the response content as a string
        return response.text


