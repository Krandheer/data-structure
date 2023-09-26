import os
import requests

base = os.path.expanduser("~")
projects = os.path.join(base, "projects")

url = "https://storageg"

file_path = os.path.join(projects, "_148.json")

files = {"files": open(file_path, "rb")}

response = requests.post(url, files=files)

print(response.text)
