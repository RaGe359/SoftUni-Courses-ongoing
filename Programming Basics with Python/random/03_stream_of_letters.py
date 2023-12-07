secret_word = ""
word = ""
sentence = ""
c_c = 0
c_n = 0
c_o = 0

while True:
    letters = input()
    if not letters.isalpha():
        continue

    if letters == "End":
       break

    if letters == "c" and c_c == 0:
        c_c = 1
        secret_word += letters
        if c_o == 0 or c_n == 0:
            continue
        elif c_o == 1 and c_n == 1:
            pass
    elif letters == "o" and c_o == 0:
        c_o = 1
        secret_word += letters
        if c_c == 0 or c_n == 0:
            continue
        elif c_c == 1 and c_n == 1:
            pass
    elif letters == "n" and c_n == 0:
        c_n = 1
        secret_word += letters
        if c_o == 0 or c_c == 0:
            continue
        elif c_o == 1 and c_c == 1:
            pass

    if c_c == 1 and c_o == 1 and c_n == 1:
        word += " "
        c_c = 0
        c_o = 0
        c_n = 0
        secret_word = ""
        sentence += word
        word = ""
        continue

    word += letters

print(sentence)