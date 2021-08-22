import re
import zipfile

# http://www.pythonchallenge.com/pc/def/channel.zip
code = '90052'
find = True
comments = []

zip_f = zipfile.ZipFile('/Users/apple/Downloads/channel.zip')

while find:
	file_dir = f'/Users/apple/Downloads/channel/{code}.txt'
	with open(file_dir, 'rb') as f:
		comments.append(zip_f.getinfo(f'{code}.txt').comment.decode())
		for s in f.readlines():
			_s = bytes.decode(s)
			print(_s)
			r = re.findall('Next nothing is [0-9]+', _s)
			if bool(r):
				code = r[0].split()[-1]
			else:
				find = False

print(''.join(comments))
