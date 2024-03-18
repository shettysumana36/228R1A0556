ch=input("Enter the character")
if(ch.islower()):
    print(ch,"is lowercase alphabet")
elif(ch.isupper()):
    print(ch, "is uppercase alphabet")
elif(ord(ch)>=48 and ord(ch)<=57):
    print(ch,"is digit")
else:
    print(ch,"is special character")
