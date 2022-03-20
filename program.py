string=input()
rev=string[::-1]
for i in range(0,len(string)+1):
    
    if(string[i]!=rev[i]):
        print(string[i])
        break
    
    
    
