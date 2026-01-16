#Input number for height of the pyramid
heightNumber = int(input("Enter the height number: ")) 

#Creat pyramid
for i in range(heightNumber):

    #Creat blank space
    print(" "*(heightNumber-i-1),end="")

    #Creat pyramid of each height
    print("*"*(2*i+1),end="")

    #Creat new line of pyramid
    print()