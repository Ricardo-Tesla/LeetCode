def longestCommonPrefix(strs):
    
    #if the input array is empty
    
    if not strs:
        return ""
    
    
    #start with the first string as the initial prefix
    
    prefix= strs[0]
    
    #iterate over the remaining strings
    
    for i in range(1, len(strs)):
        
        #reduce the prefix length while it doesnt match the current string
        
        while strs[i].find(prefix) !=0:
            prefix = prefix[:-1]
            
            #if the prefix becomes empty, return ""
            
            if not prefix:
                return ""
            
    return prefix

strs=["flower", "flow", "flight"]
print(longestCommonPrefix(strs))