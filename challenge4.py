from urllib import request
import re

# code = '12345'
code = '8022'
data = None

while True:
	address = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={code}'
	data = bytes.decode(request.urlopen(address).read())
	code = re.findall('next nothing is [0-9]+', data)
	if not bool(len(code)):
		break
	code = code[0].split()[-1]
	print(code)

print(data)




