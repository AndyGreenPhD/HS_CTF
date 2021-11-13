import sys
 
def scrambler(word):
    eggs = list(word)
 
    scrambledeggs = []
    for i in range(len(eggs)):
        scrambledeggs.append(int(ord(word[i % 4]) / 2))
 
    return(scrambledeggs)
 
if len(sys.argv) < 2:
    print("Find the hidden message: \"4737473 920692 971597\"")
    print("No args!\nUsage: python3 scrambler.py <comma,separated,list>")
    sys.exit()
 
elif len(sys.argv) > 2:
    print("Find the hidden message: \"4737473 920692 971597\"")
    print("Supply one argument!\nUsage: python3 scrambler.py <comma,separated,list>")
    sys.exit()
 
else:
    val = str(sys.argv[1]).split(",")
 
    secret = ['4737473', '920692', '971597']
 
    answer = []
    for i in val:
 
        temp = []
        for c in scrambler(i):
            temp.append(chr(c))
        answer.append("".join(temp))
       
    try:
 
        for i in range(len(secret)):
 
            if secret[i] == answer[i]:
                continue
            else:
                print("That's a negative ghost rider.")
                sys.exit()
 
        print(f"You got it right! The answer is {val}")
        print("Submit your answer in this format ---> ", end="")
        for i in val:
            print(i, end=" ")
 
    except:
        print("That's not right...")