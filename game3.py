r = '🪨' 
p = '📃' 
s = "✂️"
print ("""|welcome to rock paper scissors game\n 
choose rock by typing r\n choose paper by typing p\n 
choose scissors by typing s""")
import random

while True:
    try:
        print("rock,paper or scissors[r/p/s]:", end=" ")
        a = input("").lower()
        b = random.choice(['r','p','s'])
        if a == b:
            print("you choose:", end=" ")
            if a == 'r':
                print(r)
            elif a == 'p':
                print(p)
            else:
                print(s)
            print("computer choose:", end=" ")
            if b == 'r':
                print(r)
            elif b == 'p':
                print(p)
            else:
                print(s)

            print("tie")
            continue

        elif (a == 'r' and b == 's') or (a == 'p' and b == 'r') or (a == 's' and b == 'p'):

            print("you choose:", end=" ")
            if a == 'r':
                print(r)
            elif a == 'p':
                print(p)
            else:
                print(s)
            print("computer choose:", end=" ")
            if b == 'r':
                print(r)
            elif b == 'p':
                print(p)
            else:
                print(s)

            print("you win")


            print("continue?:(y/n)")
            c = input("").lower()
            if c == 'y':
                continue
            else:
                print("thanks for playing")
                break


        elif (a == 'r' and b == 'p') or (a == 'p' and b == 's') or (a == 's' and b == 'r'):
            print("you choose:", end=" ")
            if a == 'r':
                print(r)
            elif a == 'p':
                print(p)
            else:
                print(s)
            print("computer choose:", end=" ")
            if b == 'r':
                print(r)
            elif b == 'p':
                print(p)
            else:
                print(s)
            print("you lose")

            continue
        
        else:
            raise ValueError("invalid option")
            
    except ValueError as e:
        print(e)
        continue

#  use dictonary other time to make it more efficient and less code