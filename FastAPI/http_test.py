import requests
"""
result = requests.get('http://127.0.0.1:8000/').json()

for i, (x,y) in enumerate(result['items'].items()):
    print(str(i) + 'Index primario')
    print(str(x) + 'Index secundario')
    print('Nome:'+ y['name']+"\nValor:"+str(y['price']))
"""
"""
result = requests.get("http://127.0.0.1:8000/items/9").json()
print(result)
"""
result =  requests.get("http://127.0.0.1:8000/items?name=Hammer")
print(result.text)