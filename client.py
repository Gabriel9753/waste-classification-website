import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('D:\Studium\OneDrive - Hochschule Karlsruhe\waste-dataset\wertstoff - offer\_20.JPG.jpg','rb')})

print(resp.json())