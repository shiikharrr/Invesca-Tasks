# Python3 program to reverse a string
# s = input()
s = "i like this program very much"
words = s.split(' ')
string =[]
for word in words:
	string.insert(0, word)

print("Reversed String:")
print(" ".join(string))

def reverseList(A):
    print( A[::-1])
	
# Driver function to test above function
A = 'my name is shikha gupta'
print(A)
print("Reversed list is")
reverseList(A)
