# Import the requests library
import requests
from requests.auth import HTTPBasicAuth
from opendtu import OpenDTU_API
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

GET = True
POST = False
get_list = [
    "/api/config/get",
    "/api/config/list",
    "/api/device/config",
    "/api/devinfo/status",
    "/api/dtu/config",
    "/api/inverter/list",
    "/api/limit/status",
    "/api/livedata/status",
    "/api/mqtt/config",
    "/api/mqtt/status",
    "/api/network/config",
    "/api/network/status",
    "/api/ntp/config",
    "/api/ntp/status",
    "/api/ntp/time",
    "/api/power/status",
    "/api/prometheus/metrics",
    "/api/security/config",
    "/api/security/authenticate",
    "/api/system/status",
]
opendtu_ip = "192.168.11.120"
opendtu_user = "admin"
opendtu_password = "admin123"




# Create an instance of the class with the given IP address
api = OpenDTU_API("http://{}".format(opendtu_ip), user="admin", password="admin123")


if GET:
    for item in get_list:
        print("Check for: {}".format(item))
        status = api.get_data(item)
        print(status)

if POST:
    status = api.post_data(
        "/api/ntp/config",
        '{"ntp_server":"pool.ntp.org","ntp_timezone":"CET-1CEST,M3.5.0,M10.5.0/3","ntp_timezone_descr":"Europe/Berlin","longitude":9.209253311,"latitude":49.90994644,"sunsettype":1}',
    )
    print(status)
