import json
from pprint import pprint

json_example = open("json_example.json").read()
pprint(json_example)

print("\n")

json_python = json.loads(json_example)
pprint(json_python)

print("\n")

int_name = json_python["ietf-interfaces:interface"]["name"]
int_ip = json_python["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]
pprint(int_name)
pprint(int_ip)

print("\n")

json_data = json.dumps(json_python)
pprint(json_data)

print("\n")

