save_ = open('base.txt', 'w') 
with open('/home/jazis/Documents/projects/email_ext/output/emails.txt', 'r') as file:
    for line in file:
        new_line0 = line.split('>')
        for i in range(len(line.split('>'))):
            if 'mailto' in line.split('>')[i]:
                try:
                    print new_line0[i].split('"')[1].replace('mailto:', '') + new_line0[i+2].split(' ')[0].split('<')[0]
                    if ':' in new_line0[i+2].split(' ')[0].split('<')[0]:
                        save_.write(new_line0[i].split('"')[1].replace('mailto:', '') + new_line0[i+2].split(' ')[0].split('<')[0] + '\n')   
                except IndexError:
                    print 'Bad line - ' + new_line0[i].split('"')[1].replace('mailto:', '')