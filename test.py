# 1 1 2 3 5 8 
firstnumber = 1
secondnumber = 1
print(firstnumber)
print(secondnumber)
count = 0
while count <= 10:
	count = count + 1
	firstnumber,secondnumber = secondnumber,firstnumber+secondnumber
	print(secondnumber)


# swap a b
a = input("请输入a的值:")
b = input("请输入b的值:")
temp = a
a = b
b = temp
print("a的值="+a)
print("b的值="+b)

# Palindrome Number

def isPalindrome(number):
	if number < 0:
		return False
	else:
		str1 = str(number)
		str2 = str1[::-1]
		if str1 ==  str2:
			return True
		else:
			return False
result = isPalindrome(int(input('请输入一个数字：'))) 
print(result)