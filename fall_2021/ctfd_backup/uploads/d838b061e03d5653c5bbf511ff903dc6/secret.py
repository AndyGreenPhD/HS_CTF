import sys
 
if len(sys.argv) < 2:
    print("No args!\nUsage: python3 check.py <string>")
    sys.exit()
 
elif len(sys.argv) > 2:
    print("Supply one argument!\nUsage: python3 check.py <string>")
    sys.exit()
 
else:
    val = str(sys.argv[1])
 
    secret = [75, 83, 85, 61, 68, 97, 66, 101,  115, 116]
 
    count = 0
    for i in val:
 
        if ord(i) == secret[count]:
            print(f'wowzer, char {i} is correct.')
            count += 1
            continue
 
        else:
            print("das not right")
            sys.exit()
 
print(f"Wow, you made it! The correct answer is {val}")