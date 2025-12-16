import requests

i = 0
save_file0 = open('temp.txt', 'w')

req0 = requests.get('https://forum.redage.net/').text.encode('utf-8')

save_file0.write(req0)
save_file0.close()

save_file1 = open('temp1.txt', 'w')
with open('temp.txt', 'rb') as file:
    for line in file:
        if 'ipsType_break' in line:
            new_line0 = len(line.split("'"))
            new_line1 = line.split("'")
            for i in range(new_line0):
                if 'http' in line.split("'")[i]:
                    print line.split("'")[i]
                    save_file1.write(line.split("'")[i].split("-")[1].split("/")[0] + '\n')

save_file1.close()
raw_input()