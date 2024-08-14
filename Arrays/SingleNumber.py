def singleNumber(nums):
    single=0
    for num in nums:
        single ^=num
    return single
    
    

nums=[2,2,1]   # [4,1,2,1,2], [1]
print(singleNumber(nums))