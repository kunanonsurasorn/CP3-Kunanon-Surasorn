def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(price1,price2):
    vat = 7
    vatprice1 = price1 * vat / 100
    vatprice2 = price2 * vat / 100
    totalprice = (price1 + vatprice1)+(price2 + vatprice2)
    return vatprice1,vatprice2,totalprice

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vatprice1,vatprice2,totalprice = vatCalculator(price1,price2)
    return price1,price2,vatprice1,vatprice2,totalprice

connection = login()
if connection == True:
    showMenu()
    numberSelected = menuSelect()
    if numberSelected == 1:
        price1,price2,vatprice1,vatprice2,totalprice = priceCalculator()
        print("Vat Calculation")
        print("First Product Price :",price1,"฿","VAT :",vatprice1,"฿")
        print("Second Product Price :",price2,"฿","VAT :",vatprice2,"฿")
    elif numberSelected == 2:
        price1,price2,vatprice1,vatprice2,totalprice = priceCalculator()
        print("Price Calculation")
        print("First Product Price with VAT :",price1+vatprice1,"฿")
        print("Second Product Price with VAT :",price2+vatprice2,"฿")
        print("Total cost with VAT :",totalprice,"฿")
    else:
        print("This menu has only two number")
else:
    print("User or password not true.")
    print("Please insert true user and password")        