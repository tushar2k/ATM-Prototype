import sqlite3


class birth:
    date = int
    month = str
    year = int


def update(Id):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select * from details where Card_No=" + str(Card)
    cursor = conn.execute(cmd)
    ifRecordExist = 0
    for row in cursor:
        ifRecordExist = 1
    if(ifRecordExist == 1):
        print('Enter the Details')
        name1 = input("Enter the Name: ")
        name1= "'"+name1+"'"
        cmd = "update Details set Name=" + \
            str(name1) + " where Card_No=" + str(Card)
        conn.execute(cmd)
        phone = int(input("Enter the phone number: "))
        cmd = "update Details set Phone_No=" + \
            str(phone) + " where Card_No=" + str(Card)
        conn.execute(cmd)
        conn.commit()
    else:
        print('Enter the Correct Details')
    conn.close()


def insert(accNo):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select * from details where Account_No=" + str(accNo)
    cursor = conn.execute(cmd)
    cmd = "insert into details (Account_No,Name,Card_No,Phone_No,Balance,Pin) values(" + str(accNo) + "," + str(name1) + "," + str(cardNo) + "," + str(phone) + "," + str(bal) + "," + str(pin) + ")"
    conn.execute(cmd)
    conn.commit()
    conn.close()


cursor = 0


def count(cursor):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select count(*) from details"
    cursor = conn.execute(cmd)
    results = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return results


def checK(ck):
    conn = sqlite3.connect("AccountInfo.db")
    cmd = "select * from details where Card_No=" + str(ck)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close
    return profile


cardNo = 632000
print('______________________Welcome______________________')
a = int(input('\n1. Create Profile \n2. Update Profile \n3. Exit\nEnter the choice: '))
while(a != 3):
    if(a == 1):
        i = count(cursor)
        accNo = i + 1
        v = accNo
        accNo = birth()
        print('Enter the Details')
        accNo.date = int(input('Enter the Day of birth: '))
        accNo.month = str(input('Enter the Month of birth: '))
        accNo.year = int(input('Enter the Year of birth: '))
        name1 = input("Enter the Name: ")
        name1= "'"+name1+"'"
        phone = int(input("Enter the phone number: "))
        bal = int(input('Enter the amount deposited: '))
        y = accNo.date
        x = accNo.month
        j = accNo.year
        pin = 0
        cardNo += v
        print('Card No:', cardNo)
        insert(v)
        print('Created')
    if(a == 2):
        Card = int(input('Enter the Card No.: '))
        profile = update(Card)
        print("Updated Succesfully")
    z = int(input('\nDo you want to continue:\n1. Yes\t2. No \nEnter the Choice: '))
    if(z == 1):
        a = int(
            input('\n1. Create Profile \n2. Update Profile \n3. Exit\nEnter the choice: '))
    if(z == 2):
        break
if(a == 3 or z == 2):
    print("Good Bye")
    exit
