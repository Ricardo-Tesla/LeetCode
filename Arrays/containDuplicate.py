def containDuplicate(nums):
    number_set=set()
    
    
    for i in range(len(nums)):
        number=nums[i]
        
        if number in number_set:
            return True
        
        number_set.add(number)
        
    return False

nums=[1,2,3]
print(containDuplicate(nums))