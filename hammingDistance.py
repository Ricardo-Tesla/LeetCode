def hammingDistance(x,y):
    
    #perform XOR 
    
    xor_result= x ^ y
    
    count= 0
    
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1
        
    return count

x=4
y=1
print(hammingDistance(x,y))