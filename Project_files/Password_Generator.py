#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n <%> Welcome to the PyPassword Generator!")
nr_letters= int(input("\n #> How many letters would you like in your password :>> ")) 
nr_symbols = int(input("\n #> How many symbols would you like :>> "))
nr_numbers = int(input("\n #> How many numbers would you like :>> "))

max_input = max(nr_letters,nr_symbols,nr_numbers)
length = nr_letters + nr_symbols + nr_numbers
password = ""

for x in range(0, max_input):
    if (x < nr_letters):
        rand_index = random.randint(0,len(letters)-1)
        password = password + letters[rand_index]
   
    if (x < nr_symbols):
        rand_index = random.randint(0,len(symbols)-1)
        password = password + symbols[rand_index]
       
    if (x < nr_numbers):
        rand_index = random.randint(0,len(numbers)-1)
        password = password + numbers[rand_index]
     
shuffle_password = "".join(random.sample(password,len(password)))

print(f"\n|>> Your {length} character long password is : {shuffle_password}\n")




