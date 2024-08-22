def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    s_count, t_count= {}, {}
    
    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
    for letter in s_count:
        if s_count[letter] != t_count.get(letter, 0):
            return False
        
    return True
    
s="anagram"
t="nagaram"
print(isAnagram(s,t))
        