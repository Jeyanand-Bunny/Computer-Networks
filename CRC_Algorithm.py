def CRC():
    d=input("Data Word: ") # Code word
    m=d
    q=''
    g=input("Generator: ") #Divisor
    m+=('0'*(len(g)-1)) # Dividend 
    while(len(m)>=len(g)): # Until the dividend is completely iterated
        s=m[:len(g)] 
        q+=str(s[0])
        # print(s)
        if s[0]=='1': # check if first digit is either 0 or 1 
            t=g 
        else:
            t='0'*len(g) # else append 0s 
        r=""
        for i in range(len(g)):
            r+=str(int(s[i])^int(t[i])) #XOR operation
        m=r[1:]+m[len(g):]

    print("\nRemainder: ",end='')    
    print(r[1:])

    print("Quotient: ",end='')
    print(q)
    num='0'*(len(g)-1)
    if(r[1:]==num):
        print("\nNo Error.")
    else:
        print("\nAs the remainder is non zero, there is an error in transmission. ")
        print("The error can be corrected by appending Remainder to the Data word")

    print("\nFinally, Transmitted Code Word from sender: ",end='')
    print(d+r[1:])

CRC()