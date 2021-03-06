# 1.2 Unpacking Elements from Iterables of Arbitrary Length

# Problem: You need to unpack N-elements form an iterable, but the iterable may be longer than N elements, causing a "too many values to pack" exception.

# Solution: Python "star expressions" can be used to address this problem. 

def drop_first_last(grades):
	first, *middle, last = grades
	return middle
	
print(drop_first_last([72, 40, 80, 92]))

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(email)
print(phone_numbers)

# Note: The phone_numbers variable will always be a list, regardless of how many phone numbers are unpacked(including none). Thus, any code that uses phone_numbers won't have to account for the possibility that it might not be a list or perform any kind of additional type checking.