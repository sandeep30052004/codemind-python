a=input()
c=0
for i in a:
    if i in "0123456789":
        c+=1
if(c>0):
    print("Contains",+c,"digit")
else:
    print("Doesn't contain digit")