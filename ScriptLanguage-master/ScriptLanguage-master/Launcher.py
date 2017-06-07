loopFlag = 1
from LoadAPI import *
from GUI import *
def printMenu():
    print("========Menu==========")
    print("발행번호 검색:  g")
    print("회사정보 검색:  f")
    print("금융용어 검색:  d")
    print("========Menu==========")

def launcherFunction(menu):
    if menu == 'g':
        name = str(input ('조회할 회사이름을 입력: '))
        ret = getInfoDataFromname(name)
    elif menu == "f":
        name = str(input('조회할 발행번호를 입력 : '))
        getInfoFromNum(name)
        getStockFromNum(name)
    elif menu == 'd':
        name = str(input('검색할 용어를 입력 : '))
        getInfoFromKey(name)
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
start()
while (loopFlag > 0):

    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")