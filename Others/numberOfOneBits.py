def count_one_bits(n):
    count = 0
    while n:
      count += n & 1
      n >>= 1
    return count

#Example

n=11
print(count_one_bits(n))
