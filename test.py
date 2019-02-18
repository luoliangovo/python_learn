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


#Roman To Integer
#
def romanToInt(s):
	a = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
ans = 0
for i in range(len(s)):
	if i ==0 or a[s[i]]<=a[s[i-1]]:
		ans+=a[s[i]]
	else:
		ans+=a[s[i]]-2*a[s[i-1]]
	return ans
result = romanToInt(input('请输入罗马字符:'))
print(result)


	






