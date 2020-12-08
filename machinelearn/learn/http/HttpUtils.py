import requests,json

def get(url, data):
    res = requests.get(url, timeout=5)
    result = res.text
    print(result)

# post表单提交
def postJson(url, data=None):
    headers = {"Content-Type" : "application/json"}

    if not data:
        data = {}
    res = requests.post(url,json=data, headers=headers, timeout=5)
    result = res.text
    print(result)

# postJson("http://localhost:9001/bus/bus-refresh")
# postJson("http://localhost:9001/bus/bus-refresh/config-client:**")

data = {"name":"ukar","remark":"aaa"}
postJson("http://localhost:8081/demo/post", data)