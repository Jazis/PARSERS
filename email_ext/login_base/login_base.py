# base = raw_input('Input logins -> ')

output = open('out.txt', 'w')
base ='/home/jazis/Documents/projects/email_ext/output/emails.txt'

with open(base, 'r') as file:
    for line in file:
        # print line.strip()
        # print line.split('@')[0]
        new_line1 = str(line.split('@')[0]) + '@fa.ru:' + str(line.split('@')[0])
        output.write(new_line1 + '\n')

output.close()