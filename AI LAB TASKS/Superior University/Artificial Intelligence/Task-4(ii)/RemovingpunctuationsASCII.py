my_phrase = input("Enter a string literal:")
list1 = []
for i in my_phrase:
    ascii_value = ord(i)
    if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122) or (48 <= ascii_value <= 57) or (ascii_value == 32):
        list1.append(i) 
    else:
        pass  
result = ''
for i in list1:
    result += i
print(result)

