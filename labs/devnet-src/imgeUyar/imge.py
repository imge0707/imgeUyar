import json
dosya=open("imge.json","r",encoding="utf8")
json_dosya=json.load(dosya)
for i in json_dosya["kimlik"]:
    print(json_dosya["kimlik"][i])
	
