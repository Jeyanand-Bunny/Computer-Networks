# 7 bit Hamming code
def parity(a,i):
    if(a[i]%2==0):
        return 0
    else:
        return 1
a=[0]*7

a[2],a[4],a[5],a[6]=(int(x) for x in input("Data Word(4-bit): ").split())
print("Given 4-bit Data Word: "+str(a[2])+str(a[4])+str(a[5])+str(a[6]))

a[0]=(a[2]+a[4]+a[6])
a[1]=(a[2]+a[5]+a[6])
a[3]=(a[5]+a[4]+a[6])


a[0]=parity(a,0)
a[1]=parity(a,1)
a[3]=parity(a,3)

print("")
print("                    | D7 | D6 | D5 | P4 | D3 | P2 | P1 |")
print("7-bit Hamming Code:    ", end="")
for i in range(1,8):
    print(str(a[7-i])+'    ',end="")

x=list(int(i) for i in input("\nEnter Received code word: ").split())
p1=x[0] + x[2] + x[4] + x[6] 
p2=x[2]+x[5]+x[6]+ x[1] 
p3=x[3]+ x[4] + x[5] + x[6] 

p1=p1%2
p2=p2%2
p3=p3%2
loc=(p3*4+p2*2+p1*1) - 1
if (loc<0):
    print("There is no error in Transmission")
else:
    print("Error at location-" + str(loc+1))
    if(x[loc]==1):
        x[loc]=0
    else:
        x[loc]=1
    print("Corrected code word - ",end="")
    for i in range(len(x)):
        print(x[i],end="")