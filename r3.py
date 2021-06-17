lines = []
allen = []
word = []
s = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())



for line in lines:
	s = line.split()
	s[0] = s[0][5:]
	for m in s[1:]:
		word.append(s[0] + m)
	
#	if 'Allen' in s[0]:
#		s[0] = 'Allen: '
#		for m in s[1:]:
#			allen.append(s[0] + m)
print(word)