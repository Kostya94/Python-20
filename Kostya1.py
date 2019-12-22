a = input("число:")
if a.isdigit():
    a = int(a)
    print("odd")
    if int(a) % 2 == 0 and int(a) <= 27 and int(a) >= 2:
        print("in first range")
    if int(a) % 2 != 0 and int(a) >= 29 and int(a) <= 53:
        print("in second range")
else:
    print("it's something")