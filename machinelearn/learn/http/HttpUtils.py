import requests,json

def get(url, data):
    res=requests.get(url)
    result=res.text
    print(result)

# post表单提交
def postJson(url, data=None):
    headers = {"Content-Type" : "application/json"}

    if not data:
        data = {}
    res=requests.post(url,data=json.dumps(data), headers=headers)
    result=res.text
    print(result)

# postJson("http://localhost:9001/bus/bus-refresh")
postJson("http://localhost:9001/bus/bus-refresh/config-client:**")