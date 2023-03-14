import os
import json

# json é comum em configurações e respostas de API

pessoas = [
    {
        "nome": 'maria',
        "sobrenome": 'Vieira',
        "idade": 25,
        "ativo": False,
        "notas": ['A', 'A+'],
        "telefones": {
            "residencial": "00 0000-0000",
            "celular": "00 00000-0000"
        }        
    },
    {
        "nome": 'Joana',
        "sobrenome": 'Moreira',
        "idade": 32,
        "ativo": True,
        "notas": ['B', 'A'],
        "telefones": {
            "residencial": "00 0000-0000",
            "celular": "00 00000-0000"
        }      
    },
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

# escrever um json file
with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)

# escrever em string
print(json.dumps(pessoas, indent=2))

JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

# ler um json file para dict
with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    print(pessoas)

# carregar um json file de uma string
json_string = '''
[{'nome': 'maria', 'sobrenome': 'Vieira', 'idade': 25, 'ativo': False, 'notas': ['A', 'A+'], 'telefones': {'residencial': '00 0000-0000', 'celular': '00 00000-0000'}}, {'nome': 'Joana', 'sobrenome': 'Moreira', 'idade': 32, 'ativo': True, 'notas': ['B', 'A'], 'telefones': {'residencial': '00 0000-0000', 'celular': '00 00000-0000'}}]
'''

pessoas = json.loads(json_string)
