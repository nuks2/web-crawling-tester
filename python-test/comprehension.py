import string

# List comprehension의 if 문

mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2) 
print(answer)

mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]
print(answer)

s = "string. With. Punctuation?"

out = ''.join([i for i in s if i not in string.punctuation])
print(out)