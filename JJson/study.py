import json
with open ('librito.json','r') as libros:
    dif_libros = json.load(libros)
    for libr in dif_libros:
        print(libr, '\n')
    

""" jsonData = '{"nombre":"Frank", "edad" : 39}'
jsonToPython = json.loads(jsonData)

#print(jsonToPython["nombre"])

dictionaryToJson = [{'name':'Bob', 'age':44, 'isEmployed':True},{'name':'thomy','age':'25'}]
dictionaryToJson = json.dumps(dictionaryToJson)

#dictionaryToJson.append({'nombre':'josejoas'})

print(dictionaryToJson) """