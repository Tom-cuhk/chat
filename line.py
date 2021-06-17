def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	time = []
	name = []
	allen_wordcount = 0
	viki_wordcount = 0	
	allen_sticker = 0
	viki_sticker = 0
	allen_pic = 0
	viki_pic = 0
#	person = None
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker += 1
			elif s[2] == '圖片':
				allen_pic += 1
			else:
				for line in s[2:]:
					allen_wordcount = allen_wordcount + len(line)

		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker += 1
			elif s[2] == '圖片':
				viki_pic += 1
			else:
				for line in s[2:]:
					viki_wordcount = viki_wordcount + len(line)

	print('Allen word count is: ', allen_wordcount)
	print('Viki word count is: ', viki_wordcount)
	print('Allen sticker number is: ', allen_sticker)
	print('Viki sticker number is: ', viki_sticker)
	print('Allen picture number is: ', allen_pic)
	print('Viki picture number is: ', viki_pic)


def main():
	
	lines = read_file('line.txt')
	convert(lines)
	
	
#	write_file('line_output.txt', lines)

main()