try:
    import random
    print(" "*30,"Guess What??")
    print("*"*80)
    print()
    name=input("Enter your name:")
    print()
    while name=="":
        print("Are you nameless??")
        print()
        name=input("Enter your name:")
        print()
        
    gb=3
    marks=0
    result=[]
    def intro():
        print(f'Hi {name},')
        print('Anonymous: Welcome to the "game of guesses"---')
        print(" "*10,"Guess What??")
        print()
        input("press ENTER to continue...")
        print("_"*80)
        print()
        input("GAMEPLAY: Rules are simple! Make a guess...")
        input("          You will be provided a SITUATION... ")
        input("          You can make only SPECIFIED no. of guesses...")
        input("          Don't worry! You will be provided suitable HINT after every guess...")
        input("          Also you are provided 3 GOLDEN BALLS...")
        input("          With each ball,you can make an additonal guess, so use them wisely...")
        print("_"*80)
        print()
        print("Anonymous: Before we begin, here's a brief PERSONALITY test")
        print()
        input("press ENTER to begin...")
        print()


    def assessment():
        global b,x,y,z,e,inp,like,rc
        print("-"*20,"PERSONALITY TEST","-"*20)
        print()
        print("Hey",name,"!!, Answer wisely...")
        print()
        print("1.Who is your best friend?")
        b=input()
        while b=="":
            print("please enter a valid name...")
            b=input()
        print("_"*80)
        print()
        print("2.Name 3 companions whose company suits you the most >>")
        x=input("  1:")
        while x=="":
            print("please enter a valid name...")
            x=input("  1:")
        y=input("  2:")
        while y=="":
            print("please enter a valid name...")
            y=input("  2:")
        z=input("  3:")
        while z=="":
            print("please enter a valid name...")
            z=input("  3:")
        print("_"*80)
        print()
        print("3.Who is your biggest enemy?")
        e=input()
        while e=="":
            print("please enter a valid name...")
            e=input()
        print("_"*80)
        print()
        print("4.Do you believe in LUCK or LOGIC?")
        print("enter a choice:(a/b/c)")
        print("   a.Luck")
        print("   b.Logic")
        print("   c.Sometimes both..")
        inp=input()
        while inp.lower()!="a" and inp.lower()!="b" and inp.lower()!="c":
            print("Enter a Valid choice!")
            inp=input()
        if inp.lower()=="a":
            inp="Luck"
        if inp.lower()=="b":
            inp="Logic"
        if inp.lower()=="c":
            inp="both luck and logic"
        print("_"*80)
        print()
        print("5.What you like the most?")
        print("a.Study")
        print("b.Music")
        print("c.Games")
        print("enter a choice:(a/b/c)")
        like=input()
        while like.lower()!="a" and like.lower()!="b" and like.lower()!="c":
            print("Enter a Valid choice!")
            like=input()
        if like.lower()=="a":
            like="Study"
        if like.lower()=="b":
            like="Music"
        if like.lower()=="c":
            like="Games"
        rc=[b,[x,y,z],e,inp,like]
        print()
        input("Anonymous: Alright, it's time to play GUESS WHAT??...")
        print()
        return rc


    def guess_what():
        def no_checker(single_digit,remain):
                 while True:
                    try:
                        single_digit_guess=int(input("Make your guess:"))
                        print()
                        while len(str(single_digit_guess))!=1:
                            print("bad input..")
                            print("enter a single digit no.")
                            print()
                            single_digit_guess=int(input("Make your guess:"))
                            print()
                        if type(single_digit_guess)==int :
                            break
                    except:
                        print("bad input!! enter a no...")
                        print()

                 return solver(single_digit_guess,single_digit,remain)
                
        def solver(single_digit_guess,single_digit,remain):
                    global gb
                    global marks
                    global result
                    if single_digit_guess==single_digit:
                        print()
                        input("Anonymous: Well it seems you have got it!!...")
                        print()
                        result.append("Cleared")
                        marks+=1
                        return True
                    elif remain==1:
                        if gb!=0:
                            print("Oops!! wrong guess..")
                            print(f"You have {gb} golden balls..")
                            ub=input("Would you like to use one (y,n):")
                            print()
                            while ub.upper()!="Y" and ub.upper()!="N":
                                print("Please enter a valid choice!!")
                                ub=input("enter your choice :")
                                print()
                            else:
                                if ub.upper()=="Y":
                                    gb-=1
                                    single_digit_guess=no_checker(single_digit,remain)
                                elif ub.upper()=="N":
                                    input("Sorry You LOST....")
                                    print()
                                    result.append("Failed")

                        else:
                            print("It seems you don't have any golden ball...")
                            input("Sorry You LOST....")
                            result.append("Failed")
                    else:
                        print("wrong guess!!")
                        hint(single_digit_guess,single_digit)


        def card_distributor():
            A=[]
            B=[]
            C=[]
            D=[]
            suit=["Heart","Diamond","Club","Spade"]
            card=["Ace","Deuce","Thrice","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
            shuffled_deck=[]
            while len(shuffled_deck)!=52:
                rand_suit=random.choice(suit)
                rand_card=random.choice(card)
                CARD=f"{rand_card} of {rand_suit}"
                if CARD not in shuffled_deck:
                    shuffled_deck.append(CARD)
            pointer=0
            p=[A,B,C,D]
            for i in range(0,52):
                if pointer==len(p):
                    pointer=0
                p[pointer].append(shuffled_deck[i])
                pointer+=1
                
            P=card_checker(A,B,C,D,"Ace of Spade")
            if P==0:
                return "A",A,B,C,D
            if P==1:
                return "B",A,B,C,D
            if P==2:
                return "C",A,B,C,D
            if P==3:
                return "D",A,B,C,D


        def card_checker(A,B,C,D,card):
            P=0
            for suit in [A,B,C,D]:
                if card in suit:
                    return P
                else:
                    P+=1    
            

        def hint(single_digit_guess,single_digit):
            if single_digit_guess>single_digit:
                print("(Hint: Maybe you should try a smaller digit...)")
                print()
            else:
                print("(Hint: Maybe you should try a greater digit...)")
                print()


        def single_digit_mystery():
            global gb
            global result
            max_guess=5
            print("1>>"," "*10,"__SINGLE DIGIT MYSTERY__")
            print()
            print("Anonymous: This very moment I am thinking of a single digit no.")
            print("Can you guess what it is ?")
            print()
            input(f"You can make atmost {max_guess} guesses...")
            print()

            single_digit=random.randint(0,9)

            for remain in range(max_guess,0,-1):
                print("REMAINING GUESSES:",remain)
                single_digit_guess=no_checker(single_digit,remain)
                if single_digit_guess:
                    break

            print()
            print("^"*10)
            print("OUTCOME :")
            print("^"*10)
            print("x"*15,single_digit,"x"*15)
            print(f"Anonymous: Ah!! You see, {single_digit} is my favourite no.")
            input("...")


        def pi():
            global marks
            global result
            max_guess=4
            print("2>>"," "*10,"__Pi-Puzzzler__")
            print()
            pi=[3,1,4,1,5,9,2,6,5,3,5]
            decimal=random.randint(5,10)
            digit=pi[decimal]
            print(f"Anonymous: {name}, Can you guess which digit is in {decimal}th decimal place of pi??")
            print()
            input(f"You can make atmost {max_guess} guesses...")
            print()
            for remain in range(max_guess,0,-1):
                print("REMAINING GUESSES:",remain)
                single_digit_guess=no_checker(digit,remain)
                if single_digit_guess:
                    break

            print()
            print("^"*10)
            print("OUTCOME:")
            print("^"*10)
            print("pi: 3.1415926535")
            print(f"Anonymous: Well, <<{digit}>> is {decimal}th decimal place of pi")
            input("...")


        def god_father():
            global marks
            global result
            max_guess=2
            print("3>>"," "*10,"__THE GOD FATHER__")
            print()
            print(f"Anonymous: Just now!! {x},{y},{z},{b} started playing a card game...")
            input("           Deck is being shuffled and cards are distributed...")
            input("           Don't worry you don't have to guess the card game...")
            print()
            print("Can you guess who got 'ACE of SPADE'??")
            print()
            print(f"a.{x}")
            print(f"b.{y}")
            print(f"c.{z}")
            print(f"d.{b}")
            print()
            input(f"You can make atmost {max_guess} guesses...")
            print()
            ace_holder,A,B,C,D=card_distributor()
                
            for remain in range(max_guess,0,-1):
                print("REMAINING GUESSES:",remain)
                guess=input("Enter choice:")
                while guess.upper()!="A" and guess.upper()!="B" and guess.upper()!="C" and guess.upper()!="D":
                    guess=input("Enter a valid choice (a/b/c/d):")
                print()

                if guess.upper()==ace_holder:
                    print("BINGO!! You got it!")
                    marks+=1
                    print()
                    result.append("Cleared")
                    break
                else:
                    if remain==1:
                        global gb
                        if gb!=0:
                            print("Wtf!! wrong guess..")
                            print(f"You have {gb} golden balls..")
                            ub=input("Would you like to use one (y,n):")
                            print()
                            while ub.upper()!="Y" and ub.upper()!="N":
                                print("Please enter a valid choice!!")
                                ub=input("enter your choice :")
                                print()
                            else:
                                if ub.upper()=="Y":
                                    gb-=1
                                    guess=input("Enter choice:")
                                    print()
                                    while guess.upper()!="A" and guess.upper()!="B" and guess.upper()!="C" and guess.upper()!="D":
                                        guess=input("Enter a valid choice (a/b/c/d):")
                                        print()
                                    if guess.upper()==ace_holder:
                                        print("BINGO!! You got it!")
                                        marks+=1
                                        print()
                                        result.append("Cleared")
                                        break
                                    else:
                                        print("Seems like you do not have faith in them..")
                                        print()
                                        result.append("Failed")
                                        break
                                        
                                elif ub.upper()=="N":
                                    print("Seems like you do not have faith in them..")
                                    input("Sorry You LOST....")
                                    print()
                                    result.append("Failed")
                                    break               
                        if gb==0:
                            print("You don't have any golden ball!!")
                            input("Sorry You LOST....") 
                            print("Seems like you do not have faith in them..")
                            print()
                            result.append("Failed")
                            break               
                            
                    else:
                        print("Wrong Guess!! Try Again...")
                        print("(Hint: It all depends upon your 'faith in four'...)")
                        print()

            if ace_holder=="A":
                ace_holder=f"{x}"
            if ace_holder=="B":
                ace_holder=f"{y}"
            if ace_holder=="C":
                ace_holder=f"{z}"
            if ace_holder=="D":
                ace_holder=f"{b}"

            print()
            print("^"*10)
            print("OUTCOME:")
            print("^"*10)
            print(f"{x}: ",A)
            print()
            print(f"{y}: ",B)
            print()
            print(f"{z}: ",C)
            print()
            print(f"{b}: ",D)
            print()
            print(f"Anonymous: Guess what?? {ace_holder} got The GOD FATHER...")
            input("...")


        def missing_alpha():
            global gb
            global marks
            global result
            max_guess=3
            print("4>>"," "*10,"__WORD PROBLEM__")
            print()
            print(f"Anonymous: I found a letter in {e}'s bag...")
            input(f"           There is written a word: [B#T]")
            print()
            print("May be you can find what comes in place of '#'... ")
            print()
            input(f"You can make atmost {max_guess} guesses...")
            print()
            vowel=["A","E","I","O","U"]
            missing_alpha=random.choice(vowel)
            for remain in range(max_guess,0,-1):
                print("REMAINING GUESSES:",remain)
                guess=input("Guess:")
                while len(guess)!=1:
                    guess=input("Enter a single ALPHA:")
                
                print()
                if guess.upper()==missing_alpha:
                    print("Awesome!! You guessed it right!")
                    marks+=1
                    print()
                    result.append("Cleared")
                    break
                else:
                    if remain==1:
                        global gb
                        if gb!=0:
                            print("Its a wrong guess..")
                            
                            print(f"You have {gb} golden balls..")
                            ub=input("Would you like to use one (y,n):")
                            print()
                            while ub.upper()!="Y" and ub.upper()!="N":
                                print("Please enter a valid choice!!")
                                ub=input("enter your choice :")
                                print()
                            else:
                                if ub.upper()=="Y":
                                    gb-=1
                                    guess=input("Guess:")
                                    while len(guess)!=1:
                                        guess=input("Enter a single ALPHA:")
                                    if guess.upper()==missing_alpha:
                                        print("Nice!! You got it!")
                                        marks+=1
                                        print()
                                        result.append("Cleared")
                                        break
                                    else:
                                        print("Bad LUCK..")
                                        print()
                                        result.append("Failed")
                                        break
                                        
                                elif ub.upper()=="N":
                                    print("Don't tell me..")
                                    input("You LOST....")
                                    print()
                                    result.append("Failed")
                                    break
                        if gb==0:
                            print("You don't have any golden ball!!")
                            input("You LOST....")
                            print()
                            result.append("Failed")
                            break
                    else:
                        print("Wrong Guess!! Try Again...")
                        if guess.upper() not in vowel:
                            print("(Hint: It should be a vowel...)")
                        else:
                            print(f"(Hint: Believe in your superiority over {e})")
                        print()
            print()
            print("^"*10)
            print("OUTCOME:")
            print("^"*10)
            print(f"{missing_alpha} is the missing ALPHABET!!")
            print(f"WORD:B{missing_alpha.lower()}t")
            print()
            if missing_alpha=="A":
                input(f"Anonymous: Well, it seems that {e} is planning to hit you..")
                print("..with a 'bat'!!")
            if missing_alpha=="E":
                input("Anonymous: Can you 'bet' that you are far better than..")
                print(f"..{e} ??")
            if missing_alpha=="I":
                input(f"Anonymous: {name} vs {e},who will win..")
                print("..well its quite a 'bit' difficult to say!!")
            if missing_alpha=="O":
                input("Anonymous: I can assure you that I am not..")
                print("..an AI 'bot'")
            if missing_alpha=="U":
                input("Anonymous: ..'but' I must appreciate in your firm belief..")
                print(f"..that you are better than {e}")
            input("...")


        def dice_roller():
            global x,y,z,b,e,marks
            global result
            print("5>>"," "*10,"__THE BLIND GUESS__")
            print()
            print(f"Anonymous: {x},{y},{z},{b},{e} are going to play ...")
            input('                  "THE DICE ROLLER..."')
            print()
            input("Each of them will throw dice twice...")
            print()
            input('Can you guess "how" many will get a "DOUBLET"??')
            print()
            print("a.Only one")
            print("b.More than one")
            print("c.None")
            print("d.All")
            print()
            print("You can make only single guess")
            input("(Note: Golden Balls are disabled...)")
            print()
            guess=input("Enter choice:")
            print()
            while guess.upper()!="A" and guess.upper()!="B" and guess.upper()!="C" and guess.upper()!="D":
                guess=input("Enter a valid choice (a/b/c/d):")
                print()

            if guess.upper()=="A":
                choice="Only one"
            if guess.upper()=="B":
                choice="More than one"
            if guess.upper()=="C":
                choice="None"
            if guess.upper()=="D":
                choice="All"
            print(f"Anonymous: Alright! so, you think that {choice} will get a DOUBLET!!")
            input("Let's check this out...")
            print()
            print("^"*10)
            print("OUTCOME:")
            print("^"*10)
            dice=[1,2,3,4,5,6]
            resultd=[]
            doublet_holder=[]
            for turn in [x,y,z,b,e]:
                print("Turn:",turn)
                input(f"{turn} throws the dice...")
                t1=random.choice(dice)
                print(' '*10,t1,"appears..")
                input(f"{turn} throws the dice again...")
                t2=random.choice(dice)
                print(' '*10,t2,"appears..")
                input("...")
                resultd.append((t1,t2))
                if t1==t2:
                    doublet_holder.append(turn)
            doublet_count=0     
            for (x,y) in resultd:
               if x==y:
                   doublet_count+=1

            if doublet_count==0:
               print("Anonymous: Guess What?? No one got a DOUBLET!!")
               sol="C"
            if doublet_count==1:
               print(f"Anonymous: Guess What?? Only one i.e. {doublet_holder} got a DOUBLET!!")
               sol="A"
            if doublet_count>1 and doublet_count!=5:
               print(f"Anonymous: Guess What?? {doublet_count} {doublet_holder} got a DOUBLET!!")
               sol="B"
            if doublet_count==5:
               print("Anonymous: Guess What?? ALL got a DOUBLET!!")
               sol="D"
            if guess.upper()==sol:
               status="right"
            if guess.upper()!=sol:
               status="wrong"
            print()
            input(f"Anonymous: You guessed it {status}!!...")
            if status =="wrong":
               print("Anonymous: It seems that you are no good at blind guesses...")
               result.append("Failed")
            else:
               print("Anonymous: Maybe its just a FORTUNE...")
               marks+=1
               result.append("Cleared")
            input("...")


        def showdown():
            global result
            host="4chan"
            print(" "*10,"__ F I N A L  S H O W  D O W N __")
            print()
            input(f"Anonymous: {name}, So you have come this far...")
            print()
            input(f"Anonymous: Now it is time for the final showdown...")
            print()
            ready=input("Are you READY (y/n):")
            while ready.upper()!="Y" and ready.upper()!="N":
                ready=input("Enter a valid choice!(y/n):")
            print()
            if ready.upper()=="Y":
                input("Anonymous: There we go...")
            else:
                print("Anonymous: Well it seems that you are afraid of loosing!!")
                input("...but sorry you don't have any other choice...")
            print()
            print(f'{host}: Hold on...')
            input(f'       Now I will decide your match!!')
            print()
            input(f"Anonymous: The legendary {host}! Is this a reality??")
            print()
            input(f'{host}: The match begins...')
            input(f'       now...')
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(" "*10,f"__CHAIN BREAKER__<<Anonymous VS {name}>>")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print()
            alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            anon_alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            alpha_tried=[]
            secret_alphabet=random.choice(alphabet)
            input(f"{host}: An alphabet is being encrypted...")
            input(f"       You both have infinite guesses...")
            print()
            input(f"       Lets see who will get it FIRST??")
            input("...")
            roundd=1
            while True:
                print("*"*10)
                print("ROUND:",roundd)
                print("*"*10)
                print()
                print("ALPHABETS TRIED so far:",alpha_tried)
                print()
                guess=input("Enter your guess:")
                while guess.lower() not in alphabet:
                    guess=input("Guess an Alphabet:")
                if guess.lower() in anon_alpha:
                    anon_alpha.remove(guess.lower())
                if guess.lower() not in alpha_tried:
                    alpha_tried.append(guess.lower())
                if anon_alpha!=[]:
                    anon_guess=random.choice(anon_alpha)
                    print("Anonymous guessed :",anon_guess)
                    print()
                    input("PRESS ENTER to check result...")
                    print()
                    anon_alpha.remove(anon_guess)
                    alpha_tried.append(anon_guess.lower())
                else:
                    anon_guess=""
                    
                if guess.lower()==secret_alphabet:
                    final="Winner"
                    print("*"*20)
                    print("SECRET ALPHABET:",secret_alphabet)
                    print("*"*20)
                    print()
                    input(f"{host}: ..And the winner is {name}!!")
                    print()
                    input(f'Anonymous: IMPOSSIBLE!! {name} surpassed me??')
                    break
                elif anon_guess==secret_alphabet:
                    final="Looser"
                    print("*"*20)
                    print("SECRET ALPHABET:",secret_alphabet)
                    print("*"*20)
                    print()
                    input(f"{host}: ..And the winner is Anonymous!!")
                    print()
                    input(f'Anonymous: Ha ha...')
                    input(f'Anonymous: See {name}, you are just a lad...')
                    break
                else:
                    input(f"{host}: You both GUESSED it WRONG!!")
                    print("Try Again...")
                    print()
                roundd+=1
            print()   
            if final=="Winner":
                input(f"{host}: Anyway {name},CONGRATULATIONS...")
                result.append("Victory")
            if final=="Looser":
                input(f"{host}: Don't be upset {name}!!...")
                input(f"{host}: Perhaps..Its just a matter of LUCK")
                result.append("Defeat")
            print()
            print(f"##############################################################################")
            input(f"       ~~~~~Always remember to make a perfect balance b/w LUCK & LOGIC...")
            input(f"       That was all our MOTTO~~~~~")
            print(f"##############################################################################")
            print()
            print()
            print("------------------------------- T h e    E  N  D -------------------------------")
            print()
            print("* Result will be sent ASAP...")
            input("press enter to exit...")
            return host
                     
        print()       
        single_digit_mystery()
        print()
        pi()
        print()
        god_father()
        print()
        missing_alpha()
        print()
        dice_roller()
        print()
        print("*"*60)
        if marks==5:
            print("Anonymous: Well done!! You scored 5 out of 5...")
            input("           Hmm..Quite IMPRESSIVE!!")
        elif marks<5 and marks>=3:
            print(f"Anonymous: Great!! You scored {marks} out of 5...")
            
        else:
            print(f"Anonymous: You scored {marks} out of 5...")
            print("           Perhaps you are too much dependent on LUCK...")
        print("*"*60)
        print()
        input("...")
        
        host=showdown()
        return host
      
    #### main  #############################################################################
    intro()
    rc=assessment()
    host=guess_what()
    if result[5]=="Victory":
        k="defeated anonymous in FINAL SHOWDOWN..."
    if result[5]=="Defeat":
        k="got defeated by anonymous in FINAL SHOWDOWN"
    agregate=(marks/5)*100
    gbu=3-gb
    file=open("Result.txt","w")
    file.write(f'''Hi {name},

Glad to see you again!!

Here's your result-----

GOLDEN BALLS used: {gbu} of 3...
___________________________________________
|Sr.no.|       Event          |   status
|______|______________________|____________
|  1   | SINGLE DIGIT MYSTERY | {result[0]}
|  2   | Pi-Puzzzler          | {result[1]}
|  3   | THE GOD FATHER       | {result[2]}
|  4   | WORD PROBLEM         | {result[3]}
|  5   | THE BLIND GUESS      | {result[4]}
|______|______________________|____________
|  *   | FINAL SHOWDOWN       | {result[5]}            
|______|______________________|____________

********************************************************************
| You scored {marks} out of 5               
| You got {agregate}%                      
********************************************************************
| You {k}                                   
********************************************************************

So you believe in {inp}!!

Well,this guessing game is simply LUCK vs LOGIC
Making a balance between the two is always fruitful
Don't be too much dependent on LUCK...

As rightly said by someone that--
"If you are LOGICAL, LUCK will automatically follow you....."

Hope you enjoyed it!!
    ...Thanks for playing...


Regards

{host}



#########################################################
Credits:
     Made by Abhay Damalu         Made with Python

© Copyright 20i9-
All copyright reserved

Feedback at: abhaydamalu@gmail.com''')
    file.close()
except:
    print()
    print()
    print("############################################")
    print("# Oops something went wrong...             #")
    print("# Exception: Keyboard interrupt or UNKNOWN #")
    print("#                                          #")
    print("# Please contact: abhaydamalu@gmail.com    #")
    print("#                                          #")
    print("############################################")
    print()
    input("enter to quit...")
