import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase #it bring all a_z charactor from the module
    s2 = string.ascii_uppercase  #it bring all a_z charactor from the module
    s3 = string.digits  #it bring all 1,2,3,,charactor from the module
    s4 = string.punctuation # it bring all special character 
    passlength = int(input("Enter password length\n")) #Todo1: Handle Gibberish
    s = []
    s.extend(list(s1))  
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print("Your password is: ")
    print("".join(random.sample(s,passlength )))  
#join will join list of character  into string and 
# sample will take random character 


