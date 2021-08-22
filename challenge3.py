from data import challenge_3
import re


for idx, _ in enumerate(challenge_3):
	if idx > len(challenge_3) - 9:
		break
	s = challenge_3[idx: idx + 9]
	if re.match('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', s):
		print(s[4], end='')
