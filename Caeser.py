alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter your encrypted text: ")
encString = input()
encString.upper()
list(encString)
encString = [ord(c) for c in encString]
shift = 0
cycled = False
while not cycled:
    for i in encString:
        temp = []
        int(i)
        i = i + shift
        i = chr(i)
        temp.append(i)
    shift += 1
    print("".join(temp))
    if shift == 26:
        cycled = True
