print("\nWelcome The Logic Box ! \n")


while True:
    
    print("Select The Option : \n")
    print("1. Pattern Genrate \n")
    print("2. Analyze The Number\n")
    print("3.Exit\n")

    select=input("select any Option : (1,2,3) : ")

    if select=="1":
         pattern=int(input("how much * print ! Please Enter the value  : "))

         if pattern <= 0:
            print("Invalid row count! Stopping pattern generation.")
            break

         for i in range(1):
              for j in range(1,pattern+1):
                print(j * "*")
              
              print("\nyour star is Genrate")
         break       

    elif select=="2":
        start=int(input("Enter The Starting Value : "))
        end=int(input("Enter The Ending Value : "))    
        sum=0

        for i in range(start,end+1):
            if i % 2 == 0:
                print(f"Number {i} Even")
            else:
                print(f"Number {i} odd")


            sum += i

        print(f"\nSum From {start} to {end} Total : {sum}") 
        break  
        

    elif select=="3":
        print("You are Exit ! Good Bye")
        break

    else:
        print("Invalid option, try again.")    


    
