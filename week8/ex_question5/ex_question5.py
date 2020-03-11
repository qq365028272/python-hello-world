import json

buffer = ''
with open('cars_database.json', 'r') as file:
    buffer = file.read()

deserialized = json.loads(buffer)

for i in [0,1,2]:
    print("This",deserialized['make'][i],deserialized['model'][i]," was built in ",deserialized['year'][i],)