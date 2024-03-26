import re
import requests

def extract_domain(url):
    domains = []

    response = requests.get(url)
    lines = response.text.split('\n')

    pattern = re.compile(r'^(?:domain:|full:)?(\S+)$')
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            domains.append(match.group(1))

    return domains

url = 'https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt'
domains = extract_domain(url)
print(domains)
