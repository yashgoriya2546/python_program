amount = 240000
def insertbalance(ib):
    if ib>0:
        print("Amount are inserted")
        print("Current balance are:",amount + ib)
    else:
        print("Not succesfully")

def withdraw(*wd):
 for i in wd:
    if amount>i:
        print("withdraw successfully")
        print("Bankbalance your bankaacount current are:",amount - i)
    elif amount == i:
        print("withdraw succesfully")
        print("Your bankaccount is null")
    else:
        print("Not Avalible Balance", wd)


insertbalance(100000)
withdraw(20000,20000,10000)
