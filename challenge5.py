from urllib import request
import pickle

source_url = 'http://www.pythonchallenge.com/pc/def/banner.p'

data = request.urlopen(source_url).read()
data = pickle.loads(data)
for d in data:
	for c in d:
		print(c[0] * c[1], end='')
	print('')
