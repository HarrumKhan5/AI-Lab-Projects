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
