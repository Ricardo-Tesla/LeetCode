def reverseBits(n):
    
    result=0
    
    for i in range(32):
        bit= n & 1
        
        result= result << 1 | bit
        
        n >>= 1
        
    return result

n=43261596
print(reverseBits(n))