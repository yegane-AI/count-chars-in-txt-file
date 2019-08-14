'''this program count the alphabet you ask '''
y = open('text.txt','r')
data = y.read()
x = 0
d = input("Type an alphabet you want to count in This text: ")
for i in data:
    if i == d:
       x = x +1
print("We have ",x, d,"'s in our text. \n " )
#print(data)
input("press Enter to exit")
y.close()

