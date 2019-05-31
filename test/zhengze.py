import re
match = re.search(r'[1-9]\d{5}',"BIT 100081")
if match:
    print(match.group(0))