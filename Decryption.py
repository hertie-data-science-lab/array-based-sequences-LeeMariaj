def decrypt(message, code):
    # Lists with lower and upper case letters
    letters_l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    letters_u = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

    # Generate a list with the position of the letters in the
    # encrypted message
    a = []
    for i in message:
        # Generate a code for lower case letters
        if i in letters_l:
            a.append(letters_l.index(i) - code)
        # Generate a code for lower case letters
        elif i in letters_u:
            a.append(letters_u.index(i) - code + 100)
        # Generate a code for lower case letters
        else:
            a.append(200)

    # Generate the decrypted message
    b = []
    for i in a:
        # for lower case letters
        if i < 26:
            b.append(letters_l[i])
        elif 26 <= i < 100:
            b.append(letters_l[(i - 26)])
        # for upper case letters
        elif 100 <= i < 126:
            b.append(letters_u[i - 100])
        elif 126 <= i < 200:
            b.append(letters_u[(i - 126)])
        # for spaces
        elif i == 200:
            b.append(" ")

    # Final Message
    encrypted = "".join(str(x) for x in b)
    return (encrypted)