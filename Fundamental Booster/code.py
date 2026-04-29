print("Personal Data Collector")

name=input("Enter Your Name : ")
age=int(input("Enter a Your Age :  "))
height=float(input("Enter a your Height : "))
fav_num=int(input("Enter a Your Favourite Number : "))

# your age count

birth_year = 2026 - age
print(f"you are born in  {birth_year} year . you are {age} old ")

print("\n--- Summary of Collected Information ---")

print(f"my name is {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"my age is {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"my height is {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"my favourite number is {fav_num} (Type: {type(fav_num)}, Memory Address: {id(fav_num)})")

print("\n")

print("Thank You ! ")
