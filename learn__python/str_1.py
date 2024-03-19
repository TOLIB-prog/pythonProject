s = "lead me to win"
less = (" ".join(s[::-1]))
print(less, sep = "\n")


def reverse(s):
	str = " "
	for i in s:
		str = i + str
	return str
print(reverse(s))

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

