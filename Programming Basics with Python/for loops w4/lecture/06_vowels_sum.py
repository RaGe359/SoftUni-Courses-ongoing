word = input()
sum = 0

for char in word:
    if char == "a":
        sum += 1
    elif char == "e":
        sum += 2
    elif char == "i":
        sum += 3
    elif char == "o":
        sum += 4
    elif char == "u":
        sum += 5

print(sum)

# word = input()
# sum = 0

# for i in range(0, len(word)):
#     if word[i] == "a":
#         sum += 1
#     elif word[i] == "e":
#         sum += 2
#     elif word[i] == "i":
#         sum += 3
#     elif word[i] == "o":
#         sum += 4
#     elif word[i] == "u":
#         sum += 5

# print(sum)