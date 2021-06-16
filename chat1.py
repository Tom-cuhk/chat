# read the input file
# write the output file


def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

def convert(lines):
	new = []
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ': ' + line)
	return new
	
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


main()


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
	return chat



#sort_chat('Allen', 'Tom')
# write_file()
#print(chat)
