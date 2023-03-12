import requests

r = requests.post('http://localhost:5000/score', data={"text": "this shouldn't be spam"})

print(r.text)
