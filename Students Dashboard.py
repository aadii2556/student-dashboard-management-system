# pre stored students
stad = {"Roll no": "admin", "Name": "Aditya Saxena", "Class": "Office", "pswd": "?"}
st1 = {"Roll no": "001", "Name": "Sonu Jain", "Class": "10", "pswd": "///"}
st2 = {"Roll no": "002", "Name": "Ayush Sahrma", "Class": "10", "pswd": ">>>"}
st3 = {"Roll no": "003", "Name": "Raj Goyal", "Class": "10", "pswd": "==="}

# space for new students
st4 = {}
st5 = {}
st6 = {}
st7 = {}
st8 = {}
st9 = {}
st10 = {}
# list of data
stroll = ["admin", "001", "002", "003"]
stpswd = ["?", "///", ">>>", "==="]
stname = [stad, st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]


def update(v, u):
    print("Updating...")
    match v:
        case "a":
            vl = u["Roll no"]
            index = stroll.index(vl)
            change = input("Enter New Roll no.: ")
            u["Roll no"] = change
            stroll[index] = change
            print("Roll no updated to", change)

        case "b":
            vl = u["pswd"]
            index = stpswd.index(vl)
            change = input("Enter New Password : ")
            u["Roll no"] = change
            stpswd[index] = change
            print("Password updated to", change)

        case "c":
            vl = u["Name"]
            change = input("Enter New Name : ")
            u["Name"] = change
            print("Name updated to", change)

        case "d":
            vl = u["Class"]
            change = input("Enter New Class : ")
            u["Class"] = change
            print("Class updated to", change)


def search(v, u):
    print("Searching...")
    match v:
        case "a":print("Roll no =", u["Roll no"])
        case "b":print("Password =", u["pswd"])
        case "c":print("Name =", u["Name"])
        case "d":print("Class =", u["Class"])


def delete(u):
    print("Deleting...")
    roll = u["Roll no"]
    pssw = u["pswd"]
    u.clear()
    stroll.remove(roll)
    stpswd.remove(pssw)
    print("Done!")


def login(user):
    # print("Welcome", stname[stroll.index(user)]["Roll no"])
    a = stroll.index(user)          # finding roll no in list Eg: 001
    x = stname[a]                   # finding st(1-7) in list by roll no Ex: st1
    print("Welcome", x["Name"])     # accessing data Eg: st1["Name"]
    opt = input("\t1. Update\n\t"
                  "2. Delete\n\t"
                  "3. Search\n"
                "Press a no.: ")
    opt = opt.lower()
    match opt:
        case "1":
            ch = input("\tA. Roll No.\n\t"
                         "B. Password\n\t"
                         "C. Name\n\t"
                         "D. Class\n"
                         "Press a letter to continue : ")
            ch = ch.lower()
            update(ch, x)
        case "2":
            delete(x)
        case "3":
            ch = input("\tA. Roll No.\n\t"
                       "B. Password\n\t"
                       "C. Name\n\t"
                       "D. Class\n"
                       "Press a letter to continue : ")
            ch = ch.lower()
            search(ch, x)

def signup():
    print("Reg. a New Student :-\n")
    nwuser = input("Enter new Roll no. : ")
    nwname = input("Enter a Name : ")
    nwclass = input("Enter a Class : ")
    nwpswd = input("Enter new password : ")

    # updation
    stroll.append(nwuser)
    stpswd.append(nwpswd)
    b = stroll.index(nwuser)
    y = stname[b]
    y["Roll no"] = nwuser
    y["pswd"] = nwpswd
    y["Name"] = nwname
    y["Class"] = nwclass
    print("Student added as", y["Name"])
    # print(y)
    print("\n\n")


# Student Form
print("Hello !\n\t\tStudent Dashboard".center(5, " ").title())
while True:
    mode = input("\nEnter a mode [Login or Signup] : ")
    if "L" in mode or "l" in mode:
        user = input("Enter the Roll no. : ")
        if user not in stroll:
            print("Roll no. is not correct.")
            continue
        pswd = input("Enter the password : ")
        if pswd not in stpswd:
            print("Passcode is not correct.")
            continue

        i1 = stroll.index(user)
        j1 = stname[i1]
        i2 = stpswd.index(pswd)
        j2 = stname[i2]
        if j2 != j1:
            print("Roll no. and Password does not match!!!")
            continue
        else:
            login(user)

    elif "S" in mode or "s" in mode:
        signup()

    # how to exit
    elif mode == "Exit" or mode == "exit":
        exit()
# Aditya Saxena
