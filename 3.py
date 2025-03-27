#lets make a simple password generator in python

import random 
import string
#def generate_password(length): defining function name generate_password and passing one paramater name length

def generate_password(): #defining function name generate_password 
    '''This finction generates a random password of a given length using 
    combination of uppercase letters, lowercase letters, digits, and special characters'''

    #define a string containing all possible characters
    all_chars=string.ascii_letters + string.digits + string.punctuation  #string.ascii_letters means all upper and lower characters
    #string.digits means all digits from 0 to 9 where string.punction means all special characters like !@#$%^&*

    length=int(input("Enter the length of password: "))
    #Generate a password using a random selection of characters
    password="".join(random.choice(all_chars) for i in range (length))  #here join function helps to join all random data taken from all_chars using for loop
   
    return password   #here it rerurns password to function
    
#test the function by generating a password of length 10

password =generate_password()   #it is used to passing value to the paramater
print(password)
