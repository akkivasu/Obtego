import random
import webbrowser
import datetime
from os import system
from os import remove

print("Obtego - Encryption/Decryption software")
print("© Akshay Vasudeva Rao")
print("_____________________________________________\n")

action = ""
def delete(fName):
    remove(fName)
    
def clear():
    _ = system('cls')

def takeAction():
    global action
    action = input("ObtegoPrompt > ")
    action = action.lower()

def encryptTxt(fName):
    fObjR = open(fName, "r")
    iStr = fObjR.read()

    eKey =  random.randrange(random.randrange(1,10000), random.randrange(10000, 100000))

    iList = list(iStr)
    eList = []

    for i in iList:    
        eList.append(hex(ord(i) + eKey))

    print("Encryption key: ", eKey)
    EfName = "e" + fName

    fObjR.close()

    eStr = str(eList)
    eStr = eStr.replace("[", "")
    eStr = eStr.replace(",", "")
    eStr = eStr.replace("]", "")
    eStr = eStr.replace("'", "")
    eStr = eStr.replace(" ", "")

    fObjW = open(EfName, "w+")
    fObjW.write(eStr)

    fObjW.close()

def decryptTxt(fName):
    fObjR = open(fName, "r")
    eStr = fObjR.read()
    eList = []
    nHex = len(eStr)/6

    i = 0
    n = 0
    while n < nHex:
            eList.append(eStr[i:i+6])
            i+=6
            n+=1
    fObjR.close()

    ueKey = int(input("Enter encryption key > "))

    oStr = ""

    for j in eList:
        if int(j, 0) - ueKey < 127 and int(j, 0) - ueKey > 0:
            oStr += chr(int(j, 0) - ueKey)
        else:
            m = 0
            while m < random.randrange(10, 50):
                oStr += chr(random.randrange(1, 125))
                m += 1

    DfName = "d" + fName.replace("e", "",1)

    fObjW = open(DfName, "w+")
    fObjW.write(oStr)
    fObjW.close()

def encryptBin(fName):
    fObjR = open(fName, "rb")
    istr = fObjR.read()
    elist = []

    eKey =  random.randrange(random.randrange(1,10000), random.randrange(10000, 100000))

    for i in istr:
        elist.append(i+eKey)
        
    fObjR.close()

    fObjW = open("e" + fName, "w+")
    estr = str(elist)
    fObjW.write(estr)

    print("Encryption key : ", eKey)

def decryptBin(fName):
    fObjR = open(fName, "r")
    istr = fObjR.read()
    istr = istr.replace(" ", "")
    istr = istr.replace("[", "")
    istr = istr.replace("]", "")
    istr = istr.replace("[", "")

    ilist = istr.split(",")

    UeKey = int(input("Enter encryption key : "))

    olist = []

    for i in ilist:
        olist.append(int(i) - UeKey)

    fObjW = open("d" + fName.replace("e", "",1), "wb+")
    bArray = bytes(olist)
    fObjW.write(bArray)

def historyAdd(fName, actionperf):
    if actionperf == "e":
        item = fName + " -> " + "e" + fName + " ," + str(datetime.datetime.now())
    elif actionperf == "d":
        item = fName + " -> " + "d" + fName.replace("e", "",1) + " ," + str(datetime.datetime.now())

    fObj = open("history.txt", "a+")
    fObj.write(item)
    fObj.write("\n")    
takeAction()

while action != "close":    
    if action == "help.display":
        fObj = open("help.txt")
        print(fObj.read())
      
    elif "encrypt" in action and action.endswith(".txt"):
        try:
            fTest = open(action.split(" ")[1], "r")
            print("Encrypting a text file ...")
            fName = action.split(" ")[1]
            encryptTxt(fName)
            print(fName, " ->", "e"+fName, " !Simlutaneous existance!\n")
            historyAdd(fName, "e")
            fTest.close()
        except FileNotFoundError:
            print("File not found")
            print()
            
    elif "encrypt" in action and action.endswith(".txt") == False:
        try:
            fTest = open(action.split(" ")[1], "rb")
            print("Encrypting a binary file ...")
            fName = action.split(" ")[1]
            encryptBin(fName)
            print(fName, " ->", "e"+fName, " !Simlutaneous existance!\n")
            historyAdd(fName, "e")
            fTest.close()
        except FileNotFoundError:
            print("File not found")
            print()

    elif "decrypt" in action and action.endswith(".txt"):
        try:
            fTest = open(action.split(" ")[1], "r")
            print("Decrypting a text file ...")
            fName = action.split(" ")[1]
            decryptTxt(fName)
            print(fName, " ->", "d" + fName.replace("e", "",1), " !Simlutaneous existance!\n")
            historyAdd(fName, "d")
            fTest.close()
        except FileNotFoundError:
            print("File not found")
            print()
            
    elif "decrypt" in action and action.endswith(".txt") == False:
        try:
            fTest = open(action.split(" ")[1], "r")
            print("Decrpyting a binary file ...")
            fName = action.split(" ")[1]
            decryptBin(fName)
            print(fName, " ->", "d" + fName.replace("e", "",1), " !Simlutaneous existance!\n")
            historyAdd(fName, "d")
        except FileNotFoundError:
            print("File not found")
            print()
            
    elif action == "history.display":
        fObj = open("history.txt", "r")
        h = fObj.read()
        print(h)
        fObj.close()

    elif action == "session.refresh":
        clear()
        print("Obtego - Encryption/Decryption software")
        print("© Akshay Vasudeva Rao")
        print("_____________________________________________\n")
    
    elif "clear" in action:
        fName = action.split(" ")[1]
        fObj = open(fName, "w")
        fObj.write("")
        fObj.close()
        print(action.split(" ")[1], "'s contents have been cleared")
        print()

    elif "shell" in action:
        try:
            fTest = open(action.split(" ")[1], "rb")
            webbrowser.open(action.split(" ")[1])
            print()
            fTest.close()
        except FileNotFoundError:
            print("File not found")
            print()
            
    elif "show" in action:
        if ".txt" in action:
            try:
                fObj = open(action.split(" ")[1], "r")
                h = fObj.read()
                print(h)
                print()  
                fObj.close()    
            except FileNotFoundError:
                print("File not found")
                print()
        else:
            print("Only text files can be displayed within Obtego. Try using the shell command instead.")
            print()
    
    elif "delete" in action:
        try:
            fTest = open(action.split(" ")[1])
            fTest.close()
            delete(action.split(" ")[1])
            print(action.split(" ")[1], "has been deleted")
            print()
        except FileNotFoundError:
            print("File not found")
            print()
            
    else:
        print("Unrecognized command. Use the help command for information on valid commands.\n")

    takeAction()


