import yaml
from pprint import pprint

yml_example = open("yaml_example.yaml").read()
pprint(yml_example)

print("\n")

yaml_python = yaml.load(yml_example)
pprint(yaml_python)

print("\n")

int_name = yaml_python["ietf-interfaces:interface"]["name"]
int_desc = yaml_python["ietf-interfaces:interface"]["description"]
int_ip = yaml_python["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]
pprint(int_name)
pprint(int_desc)
pprint(int_ip)

print("\n")

yml_data = yaml.dump(yaml_python)
pprint(yml_data)

print("\n")

