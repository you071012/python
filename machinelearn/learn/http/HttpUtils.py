import requests

def get(url, data):
    res=requests.get(url)
    result=res.text
    print(result)

# post表单提交
def post(url, data):
    if not data:
        data = {}
    res=requests.post(url,data=data)
    result=res.text
    print(result)

post("http://localhost:9001/refresh", None)