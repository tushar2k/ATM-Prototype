import sqlite3


def checK(ck):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select * from details where Card_No=" + str(ck)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close
    return profile


def gcd(a, b):
    while(b > 0):
        c = a % b
        a = b
        b = c
    return a


def mulinv(phi, b):
    r1 = phi
    r2 = b
    t1 = 0
    t2 = 1
    while(r2 > 0):
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t
    if(r1 == 1):
        if(t1 < 0):
            t1 = t1 + phi
            return t1
        else:
            return t1


p = 353
q = 281
phi = (p - 1) * (q - 1)
n = p * q
e = 2

while(e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e + 1

d = mulinv(phi, e)


def decrypt(c):
    y = int((c**d) % n)
    return y


def encrypt(msg):
    c = int((msg**e) % n)
    return c


def update(cardNo, pin):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select * from details where Card_No=" + str(cardNo)
    cursor = conn.execute(cmd)
    ifRecordExist = 0
    for row in cursor:
        ifRecordExist = 1
    if(ifRecordExist == 1):
        cmd = "update details SET Pin=" + \
            str(pin) + " where Card_No=" + str(cardNo)
    conn.execute(cmd)
    conn.commit()
    conn.close()


def updateB(cardNo, balance):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select * from details where Card_No=" + str(cardNo)
    cursor = conn.execute(cmd)
    ifRecordExist = 0
    for row in cursor:
        ifRecordExist = 1
    if(ifRecordExist == 1):
        cmd = "update details SET Balance=" + \
            str(balance) + " where Card_No=" + str(cardNo)
    conn.execute(cmd)
    conn.commit()
    conn.close()


def server(cardNo, pin_user):
    pin_user = decrypt(pin_user)
    profile = checK(cardNo)
    if(profile != None):
        pin = profile[5]
        Pin = int(pin)
        balance = int(profile[4])
        if(Pin == 0):
            pin = str(input('Create a new Pin: '))
            if(len(pin) != 4):
                print(('Create a correct Pin'))
                pin = str(input('Enter the Pin: '))
            print('Pin Created Successfully')
            pin = hash(pin)
            update(cardNo, pin)
        else:
            pin_user = str(pin_user)
            pin_user = hash(pin_user)
            if(Pin == pin_user):
                if(balance > Amt):
                    balance = balance - Amt
                    print( 'Transaction Success')
                    print( 'Available Balance', balance)
                    updateB(cardNo, balance)
                else:
                    print(('Not Sufficient Balance'))
            else:
                print(('Enter the correct Pin'))
    if(profile == None):
        print( 'Enter Correct Card No')


def server2(cardNo, pin_user):
    pin_user = decrypt(pin_user)
    profile = checK(cardNo)
    if(profile != None):
        pin = profile[5]
        Pin=int(pin)
        balance = profile[4]
        if(Pin == 0):
            pin = str(input('Create a new Pin: '))
            if(len(pin) != 4):
                print(('Create a correct Pin'))
                pin = str(input('Enter the Pin: '))
            print('Pin Created Successfully')
            pin = hash(pin)
            update(cardNo, pin)
        else:
            pin_user = str(pin_user)
            pin_user = hash(pin_user)
            if(Pin == pin_user):
                print('Available Balance :', balance)
            else:
                print(('Enter the correct Pin'))
    if(profile == None):
        print( 'Enter Correct Card No')


def server3(cardNo, pin_user):
    pin_user = decrypt(pin_user)
    profile = checK(cardNo)
    if(profile != None):
        pin = int(profile[5])
        if(pin == 0):
            pin = str(input('Create a new Pin: '))
            if(len(pin) != 4):
                print(('Create a correct Pin'))
                pin = str(input('Enter the Pin: '))
            print('Pin Created Successfully')
            pin = hash(pin)
            update(cardNo, pin)
        else:
            pin_user = str(input('Enter Old Pin: '))
            pin_user = hash(pin_user)
            if(pin == pin_user):
                newpin = str(input('Create a new Pin: '))
                if(len(newpin) != 4):
                    print(('Create a correct Pin'))
                    newpin = str(input('Enter the Pin: '))
                print('Pin Created Successfully')
                pin = hash(newpin)
                update(cardNo, pin)
            else:
                print( 'Enter the correct pin')
    if(profile == None):
        print( 'Enter Correct Card No')


print( '\n______________________________Welcome___________________________\n')
a = int(input('\n1. Withdrawl \n2. Check Balance \n3. Change Pin \n4. Exit\nEnter the choice: '))
while(a != 4):
    if(a == 1):
        cardNo = str(input('Enter the Card No.: '))
        pin_user = int(input('Enter the pin: '))
        pin_user = encrypt(pin_user)
        amnt = str(input('Enter the Amount to be Withdrawn: '))
        Amt = int(amnt)
        server(cardNo, pin_user)

    if(a == 2):
        cardNo = str(input('Enter the Card No.: '))
        pin_user = int(input('Enter the pin: '))
        pin_user = encrypt(pin_user)
        server2(cardNo, pin_user)

    if(a == 3):
        cardNo = str(input('Enter the Card No.: '))
        pin_user = int(input('Enter the pin: '))
        pin_user = encrypt(pin_user)
        server3(cardNo, pin_user)

    z = int(input('\nDo you want to continue:\n1. Yes\t2.No \nEnter the Choice: '))
    if(z == 1):
        a = int(input(
            '\n1. Withdrawl \n2. Check Balance \n3. Change Pin \n4. Exit\nEnter the choice: '))
    if(z == 2):
        break
if(a == 4 or z == 2):
    print( "Good Bye")
    exit
