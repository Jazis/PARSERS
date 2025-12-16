import imaplib
import time
i = 0


mail = imaplib.IMAP4_SSL('Outlook.Office365.com')
mail.login('@@email@@@', '@@@@pass@@@@')
output = open('output_' + str(time.time()) + '.txt', 'w')
mail.list()
mail.select("INBOX")
result, data = mail.search(None, "ALL")
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]
print latest_email_id
for i in range(int(latest_email_id)):
    result, data = mail.fetch(i+1, "(RFC822)")
    raw_email = data[0][1]
    output.write(raw_email)
    print '\t\t' + str(i) + ' / ' + str(latest_email_id)

output.close()
print "Done!"
raw_input()
