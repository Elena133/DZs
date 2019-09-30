import myLib
b=myLib.get_num('Vvedite chislo')
a=0
for i in range(b):
    a+=1
    print(' '*(b-i-1)+'^'*(a+i))
