import os

save = open('output.txt', 'w')

app_words = []

with open('emails.txt') as file:
	for line in file:
		new_line0 = line.split('"')
		for i in range(len(line.split('"'))):
			if '@' in line.split('"')[i]:
				try:
					new_line1 = line.split('"')[i].split(':')[1].split('>')[0]
					if ' ' in new_line1:
						pass
					else:
						if '@' in new_line1 and '.' in new_line1:
							if new_line1 in app_words:
								pass
							else:
								app_words.append(new_line1)
								save.write(new_line1 + '\n')
				except IndexError:
					pass
save.close()
