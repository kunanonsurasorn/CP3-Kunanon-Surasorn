def vatcalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result

totalprice=float(input("Enter the price (฿): "))
print("Total Price include VAT : ",vatcalculate(totalprice),"฿")