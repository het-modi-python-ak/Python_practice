with open("/home/het/Documents/Training Course/python practice/OOPs/inheritanc.py","r") as f:
    cont = f.read(100)
    print(cont)

    cont = f.read(100)
    print(cont)

file = open("/home/het/Documents/Training Course/python practice/OOPs/inheritanc.py","r")
print(file.read())


# write file

with open("text2.txt","w") as f1:
    f1.write('helo')

with open("text2.txt","a") as f1:
    f1.write('\nThis was Appended .')
    f1.write("Again s")


#write and read mode

with open("text2.txt","w+") as f1:
    f1.write('\n john is a tall boy')
    f1.seek(3)
    print(f1.read())