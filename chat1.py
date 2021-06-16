# read the input file
# write the output file
chat = []
name1 = 'Allen'
name2 = 'Tom'
with open('input.txt', 'r', encoding='utf-8') as f:
	for line in f:
		if name1 or name2 in line:
			chat.append('\n' + line.strip() + ': ') 
		else:
			chat.append(line)


print(chat)

#name1: Allen
#name2: Tom