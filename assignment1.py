#a program that converts from degrees celicius to fahrenheight and vice versa
# user based program
#it should include if statements

#choice of conversion to make
choice = input(print("which type of conversion, for C TO F, choose A, for F to C, choose B"))
print("your choice is:", choice)

#prompt the user to put in the value
value = float(input(print("Enter the value to convert")))
print("you entered,", value)
#choice of conversion

if choice =='A':
    new_value = value*1.8 + 32
elif choice =='B':
    new_value = (value-32)/1.8
else:
    new_value = 'invalid input'
print("The conversion is:", new_value)