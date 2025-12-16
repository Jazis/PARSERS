
# 4307540863247646 - good
# 5335263700655748 - bad
card = raw_input('Input your card: ')
card = card.replace(' ', '')
summa = 0
rev_card = card[::-1]
print rev_card
list_card = list(rev_card)
for i in range(len(list_card)):
    if int(list(rev_card)[i]) %2 == 0:
        print list(rev_card)[i] + ' chet'
        new_chet = list(rev_card)[i] * 2
        if new_chet>9:
            new1_chet = int(new_chet) - 9
            summa = summa + new1_chet
        else:
            summa = summa + new_chet
    else:
        print list(rev_card)[i] + ' nechet'
        summa = summa + int(list(rev_card)[i])

print summa

if summa % 10 == 0:
    print 'Good'
else:
    print 'bad'

