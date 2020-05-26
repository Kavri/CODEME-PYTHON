#Create variable "password".
#The password has letters and numbers, at least 1 capital letter and minimum length of 8 characters.
#If the password is incorrect - display the message.
#Display message depending on the error.

password = input('Enter your password:')

passwordUser = password.isalnum()
if passwordUser is True:
    print('The password has letters and numbers.')
else:
    print('The password should have letters and numbers.')

passwordl = password.islower()
if passwordl is True:
    print('The password doesn\'t have a minimum of 1 capital letter.')
else:
    print('The password has at least 1 capital letter..')

passwordNum = len(password)
if passwordNum >= 8:
    print('The password has a good length.')
else:
    print('The password should have a minimum of 8 characters.')