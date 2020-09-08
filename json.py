import json
d={'小明':{'sex':'男','addr':'上海','age':26},'小红':{ 'sex':'女','addr':'上海', 'age':24},}
print(json.dumps(d,ensure_ascii=False,indent=4))