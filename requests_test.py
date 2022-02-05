import requests

# file = requests.get(r'https://raw.githubusercontent.com/kyaldabomb/Transdirect-API-SCRIPT-2021/main/Picking%20Script%203%20(ALL%20IN%20v3).py?token=GHSAT0AAAAAABPP56A56OIMV337JMSHNGVOYP65AHA')

file = requests.get(r'https://github.com/kyaldabomb/Transdirect-API-SCRIPT-2021.git')

with open (r'https://github.com/kyaldabomb/Transdirect-API-SCRIPT-2021.git', 'wb') as f:
    f.write(file.content)