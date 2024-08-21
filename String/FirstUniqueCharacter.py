def firstUniqueCharacter(s):
    left=0
    
    for i in range(1,len(s)-1):
        if(s[left] != s[i]):
            break
            return left
        else:
            return -1
            
        left +=1
        
s=['l', 'e', 'e', 't']
print(firstUniqueCharacter(s))
        
    