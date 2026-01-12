#Created the variables of product price.
cocoa_price = 100
coffee_price = 100
tea_price = 100
milk_price = 150
milktea_price = 150
lemontea_price = 150
matcha_price = 200

#Created the vat variable
vat = 7

usernameInput = input("Enter your username : ")
passwordInput = input("Enter your password : ")

if usernameInput == "Customer" and passwordInput == "12345":

    print(f"Hello {usernameInput} Welcome to the shop. We wish your enjoy the shopping.")
    print("***********************************************************************")
    print("-------------------- List of powder and price. --------------------")
    print(f"--------------- 1. Cocoa ------------------ Price : {cocoa_price} ฿ --------------")
    print(f"--------------- 2. Coffee ----------------- Price : {coffee_price} ฿ --------------")
    print(f"--------------- 3. Tea -------------------- Price : {tea_price} ฿ --------------")
    print(f"--------------- 4. Milk ------------------- Price : {milk_price} ฿ --------------")
    print(f"--------------- 5. Milk tea --------------- Price : {milktea_price} ฿ --------------")
    print(f"--------------- 6. Lemon tea -------------- Price : {lemontea_price} ฿ --------------")
    print(f"--------------- 7. Matcha ----------------- Price : {matcha_price} ฿ --------------")
    print("***********************************************************************")
    print("Select your interested product that you want to buy.")

    #Enter products that you want to buy

    product_buying1 = input("Enter the first product name that you want to buy : ")
    product_buying2 = input("Enter the second product name that you want to buy : ")
    product_buying3 = input("Enter the third product name that you want to buy : ")
    product_buying4 = input("Enter the fourth product name that you want to buy : ")
    product_buying5 = input("Enter the fifth product name that you want to buy : ")
    product_buying6 = input("Enter the sixth product name that you want to buy : ")
    product_buying7 = input("Enter the seventh product name that you want to buy : ")

    if product_buying1 != "" or product_buying2 != "" or product_buying3 != "" or product_buying4 != "" or product_buying5 != "" or product_buying6 != "" or product_buying7 != "":
        
        #Cocoa

        cocoa_quantity = int(input("1. Cocoa powder price : 100 ฿ Quantity : "))
        cocoa_vat_calculation = cocoa_price+(cocoa_price*vat/100)

        #Coffee

        coffee_quantity = int(input("2. Coffee powder price : 100 ฿ Quantity : "))
        coffee_vat_calculation = coffee_price+(coffee_price*vat/100)

        #Tea

        tea_quantity = int(input("3. Tea powder price : 100 ฿ Quantity : "))        
        tea_vat_calculation = tea_price+(tea_price*vat/100)

        #Milk

        milk_quantity = int(input("4. Milk powder price : 150 ฿ Quantity : "))        
        milk_vat_calculation = milk_price+(milk_price*vat/100)

        #Milktea

        milktea_quantity = int(input("5. Milk Tea powder price : 150 ฿ Quantity : "))        
        milktea_vat_calculation = milktea_price+(milktea_price*vat/100)

        #Lemontea

        lemontea_quantity = int(input("6. Lemon Tea powder price : 150 ฿ Quantity : "))        
        lemontea_vat_calculation = lemontea_price+(lemontea_price*vat/100)

        #Matcha

        matcha_quantity = int(input("7. Matcha powder price : 200 ฿ Quantity : "))        
        matcha_vat_calculation = matcha_price+(matcha_price*vat/100)

        #Total of Buying

        total_buying = (cocoa_vat_calculation*cocoa_quantity)+(coffee_vat_calculation*coffee_quantity)+(tea_vat_calculation*tea_quantity)+(milk_vat_calculation*milk_quantity)+(milktea_vat_calculation*milktea_quantity)+(lemontea_vat_calculation*lemontea_quantity)+(matcha_vat_calculation*matcha_quantity)

        print("***********************************************************************") 
        print("----------------------------- Receipt --------------------------------------")

        #Cocoa Calculation

        print(f"--- 1. Cocoa powder --- Price : {cocoa_price} ฿ --- Quantity : {cocoa_quantity} Unit --- Cost : ",cocoa_price*cocoa_quantity,"฿")
        print(f"--- VAT : {cocoa_price*vat/100} ฿ --- VAT with Quantity : {(cocoa_price*vat/100)*cocoa_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Coffee Calculation

        print(f"--- 2. Coffee powder --- Price : {coffee_price} ฿ --- Quantity : {coffee_quantity} Unit --- Cost : ",coffee_price*coffee_quantity,"฿")
        print(f"--- VAT : {coffee_price*vat/100} ฿ --- VAT with Quantity : {(coffee_price*vat/100)*coffee_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Tea Calculation

        print(f"--- 3. Tea powder --- Price : {tea_price} ฿ --- Quantity : {tea_quantity} Unit --- Cost : ",tea_price*tea_quantity,"฿")
        print(f"--- VAT : {tea_price*vat/100} ฿ --- VAT with Quantity : {(tea_price*vat/100)*tea_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Milk Calculation

        print(f"--- 4. Milk powder --- Price : {milk_price} ฿ --- Quantity : {milk_quantity} Unit --- Cost : ",milk_price*milk_quantity,"฿")
        print(f"--- VAT : {milk_price*vat/100} ฿ --- VAT with Quantity : {(milk_price*vat/100)*milk_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Milktea Calculation

        print(f"--- 5. Milk Tea powder --- Price : {milktea_price} ฿ --- Quantity : {milktea_quantity} Unit --- Cost : ",milktea_price*milktea_quantity,"฿")
        print(f"--- VAT : {milktea_price*vat/100} ฿ --- VAT with Quantity : {(milktea_price*vat/100)*milktea_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Lemontea Calculation

        print(f"--- 6. Lemon Tea powder --- Price : {lemontea_price} ฿ --- Quantity : {lemontea_quantity} Unit --- Cost : ",lemontea_price*lemontea_quantity,"฿")
        print(f"--- VAT : {lemontea_price*vat/100} ฿ --- VAT with Quantity : {(lemontea_price*vat/100)*lemontea_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Matcha Calculation

        print(f"--- 7. Matcha powder --- Price : {matcha_price} ฿ --- Quantity : {matcha_quantity} Unit --- Cost : ",matcha_price*matcha_quantity,"฿")
        print(f"--- VAT : {matcha_price*vat/100} ฿ --- VAT with Quantity : {(matcha_price*vat/100)*matcha_quantity} ฿")
        print("------------------------------------------------------------------------")

        #Total Calculation

        print("Total includes VAT : ",total_buying,"฿")
        print("------------------ Thank you for buying and supporting ---------------------")

    else:
        print("--------Error!. Please insert product.-----------")

else:
    print("--------Error!. Please insert correct username and password.-----------")