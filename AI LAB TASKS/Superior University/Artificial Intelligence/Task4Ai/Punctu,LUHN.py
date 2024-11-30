#Sorrting Alphabets
text = "banana apple cherry date"
def sort_word(word):
    list1 = list(word)
    limit= len(list1)
    for i in range(limit):
        for j in range(0, limit-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
        sorted_word = ""
    for gather in list1:
        sorted_word += gather
    return sorted_word
words = text.split()
sorted_alphab = [sort_word(word) for word in words]
sorted_text = ' '
for words in sorted_alphab:
    sorted_text += words
print("Sorted text:", sorted_text)
#Removing Puntuation ASCII
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
#LUHN algo
def work():
    num=[5,8,9,3,8,0,4,1,1,5,4,5,7,2,8,9]
    x=num.pop(-1)
    print(x)
    print(num)
    num.reverse()
    print(num)
#Doubling even indexes
    for i in range(0, len(num), 2):
        num[i] *= 2
        print(num)
#Subtracting num>9 from 9
    for i in range(len(num)):
        if num[i] > 9:
            num[i] -= 9
            print(num)
    total = sum(num)
    exact=total+x
    print(exact)
    if exact % 10 == 0:
        print("Card num is valid")
    else:
        print("Card num is invalid.")
work()
