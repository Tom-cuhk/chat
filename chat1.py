# read the input file
# write the output file
chat = []

def sort_chat(name1, name2): 
	with open('input.txt', 'r', encoding='utf-8') as f:
		for line in f:
			if name1 in line:
				speaker = name1
			if name2 in line:
				speaker = name2
			if name1 in line:
				continue
			if name2 in line:
				continue
			chat.append(speaker + ': ' + line.strip() ) 	
	return sort_chat

def write_chat():
	with open('output.txt', 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')

sort_chat('Allen', 'Tom')
write_chat()
print(chat)
