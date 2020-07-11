
while True:
    print("Welcome to Zoomaland!")
    name=input("What is your name? ")
    age=int(input("What is your age? "))
    # print("Hello", name, "you are", age, "years old.")

    health=10
    if age >= 18 or age>=14:
        print("--------------------------------------------------")
        if age>=18:
            print("You are old enough!")
        elif(age>=14):
            print("You can play with supervision.")
        wants_to_play=input("Do you want to play ?...(yes/no): ").lower()
        if wants_to_play =="yes":
            print("Let's Play!")
            print("You are starting with",health,"health")
            left_or_right= input("Enter Choice... Left or Right(left/right)? ").lower()
            if left_or_right == "left":
                ans=input("You follow the path and reach a lake...Do you swim across or go around (across/around)? ").lower()

                if ans =="across":
                    print("You managed to go across, but were bit by a fish and lost 5 health.")
                    health-=5

                    ans= input("You notice a house and a car, Which do you go to (house/car)? ").lower()
                
                    if ans=="house":
                        print(".....You got attacked by a zombie and lose 5 health.....")
                        health-=5

                        if health<=0:
                            print("Your health is ",health)
                            print("-----Unfortunately, You lost all health, Game Over !!-----")
                        
                    elif ans=="car":
                        print("-----You have managed to escape...You Win !!-----")


                elif ans=="around":
                    print("You went around and reach the other side of the lake...")
                    ans=input("You saw a kit which had a gun and health booster, which one you choose(gun/booster)? ").lower()

                    if ans=="gun":
                        print("Oops, you forgot to refill...Zombie attacked you from behind.")
                        health-=10
                        if health<=0:
                            print("Your health is ",health)
                            print("-----Unfortunately, You lost all health, Game Over !!-----")

                    elif ans=="booster":
                        health-=2
                        print("Your health is ",health)
                        print("-----You have managed to escape...You Win !!-----")

                else:
                    print("You Lost...")

            else:
                print("You fell down and Lost...")


        else:
            print("GoodBye!...")


    else:
        print("Oops!, you are not old enough to play...")


    if input("Play Again...(yes/no)? ").lower()!='yes':
        print("Thanks for visiting...GoodBye!")
        break