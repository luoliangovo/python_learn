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