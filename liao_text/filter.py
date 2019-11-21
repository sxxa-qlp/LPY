def is_palindrome(n):
	return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1,1000))
print('1~1000',list(output))
















# def _not_divisible(n):
# 	return lambda x: x% n > 0
# def primes():
# 	yield 2
# 	it = _odd_iter()
# 	while True:
# 		n = next (it)
# 		yield n 
# 		it = filter(_not_divisible()n, it)