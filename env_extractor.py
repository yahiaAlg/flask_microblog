#!/usr/bin/python3
from pprint import pprint
import re

def find_env():
    env_vars = []
    with open('.env') as env:
        key_value_regex = re.compile("(.*)=(.*)", re.DOTALL)
        env_content = env.read()
    for match in key_value_regex.finditer(env_content):
        env_vars.append((match.group(1),match.group(2)))
    return env_vars

if __name__=="__main__":
    pprint(find_env())