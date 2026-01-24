class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kunanon"
customer1.lastName = "Surasorn"
customer1.age = 27
customer1.addCart()

customer2 = Customer()
customer2.name = "Parit"
customer2.lastName = "Surasorn"
customer2.age = 25
customer2.addCart()

customer3 = Customer()
customer3.name = "Thanwarat"
customer3.lastName = "Surasorn"
customer3.age = 26
customer3.addCart()

customer4 = Customer()
customer4.name = "Nongluk"
customer4.lastName = "Surasorn"
customer4.age = 58
customer4.addCart()