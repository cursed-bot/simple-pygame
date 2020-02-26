# the game code for the guessing game

import random
 
def p2(p1name, p2name):
    print("RULES: two dice will be rolled, you will try to guess the number.")
    print('whoever is closest will win, the second dice is a tie breaker.')
    print('it will keep going until someone loses.')
    while True:
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)

        print('what is your guess, ' + p1name + '?')
        p1_1 = input()
        p1g1 = abs(int(p1_1) - r1)
        print('what is your guess, ' + p2name + '?')
        p2_1 = input()
        p2g1 = abs(int(p2_1) - r1)
  
        if p1g1 < p2g1:
            print('the number was...')
            print(r1)
            print(p1name + ' wins!')
            break
        elif p2g1 < p1g1:
            print('the number was...')
            print(r1)
            print(p2name + ' wins!')
            break
        elif p1g1 == p2g1:
            print('TIE! time for the tie breaker.')

            print('what is your guess, ' + p1name + '?')
            p1_2 = input()
            p1g2 = abs(int(p1_2) - r2)
            print('what is your guess, ' + p2name + '?')
            p2_2 = input()
            p2g2 = abs(int(p2_2) - r2)
            
            if p1g2 < p2g2:
                print('the number was...')
                print(r2)
                print(p1name  + ' wins!')
                break
            elif p2g2 < p1g2:
                 print('the number was...')
                 print(r2)
                 print(p2name + ' wins!')
                 break
        else:
            print('if you are seeing this it means something went very wrong')
    print('thanks for playing!')

def p3(p1name, p2name, p3name):
    pass
    

    