# 3 ways to reverse a string

# index
s1 = "love"
print(s1)
s1_reverse = s1[::-1]
print(s1_reverse)

# join and reversed
s2 = "Keith"
print(s2)
s2_reverse = "".join(reversed(s2))
print(s2_reverse)

# list reverse, sort
s3 = "Texas"
print(s3)
s3_list = list(s3)
s3_list.reverse()
s3_string = "".join(s3_list)
print(s3_string)
