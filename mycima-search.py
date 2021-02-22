import os
import json
import requests



page = requests.get("https://mycima.plus/AjaxCenter/Searching/mm/")

js = json.loads(page.content)

#print(json.dumps(js, indent = 4, sort_keys=True))

print(js["output"],["href"])









