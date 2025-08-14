import requests
def test_apicreate():
    payload = {
        "title": "Learn Api Testing",
        "body": "pytest + requests",
        "userid": 1
              }

    print("Laxmi")
    print("Hello world")
    print("hello world in branch")
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = payload)
    assert response.status_code == 201
    assert response.json()["title"] == "Learn Api Testing"
