print('''  --------------------------------------------------
           ---- WELCOME TO PERSONALITY PREDICTION SYSTEM ----
           --------------------------------------------------

          Take this psychology test to find out about your personality!
          This test measures what many psychologists consider to be
          the five fundamental dimensions of personality.

''')
print(" To start quiz enter your name \n")
UserName = input()
print(" Enter Age: \n")
Age = int(input())
print(" Enter Gender : \n")
Gender = input()

def Evaluate():
    print('''
               1. Strongly disagree
               2. Disagree
               3. Neither disagree nor agree
               4. Agree
               5. Strongly agree
         ''')
    print("\n Enter Your Choice ")
    Value = int(input())
    if Value==1:
        return 1
    if Value==2:
        return 0.5
    if Value==3:
        return 0
    if Value==4:
        return -0.5
    if Value==5:
        return -1


def StartQuiz():
    print(''' Directions: The following statements concern your perception about yourself
                in a variety of situations. Your task is to indicate the strength
                of your agreement with each statement, utilizing a scale in which
                1 denotes strong disagreement, 5 denotes strong agreement, and 2,
                3, and 4 represent intermediate judgments.
                Submit a number from 1 to 5 from the following scale:

    1. Strongly disagree
    2. Disagree
    3. Neither disagree nor agree
    4. Agree
    5. Strongly agree ''')
    Choice=1;
    Extraversion=0;Agreeableness=0;Conscientiousness=0;Neuroticism=0;Openness=0;
    while Choice:
        print('''1. I see as my self as one who is talkative
               ''')
        Extraversion=Extraversion-Evaluate()
        print('''2. I see as my self as one who tends to find fault with others
               ''')
        Agreeableness=Agreeableness+Evaluate()
        print('''3. I see as my self as one who does a through job
               ''')
        Conscientiousness=Conscientiousness-Evaluate()

        print('''4. I see as my self as one who is depressed, blue.
               ''')
        Neuroticism=Neuroticism-Evaluate()
        print('''5. I see as my self as one who is original, come up with new ideas.
               ''')
        Openness=Openness-Evaluate()
        print('''6. I see as my self as one who is reserved
               ''')
        Extraversion=Extraversion+Evaluate()
        print('''7. I see as my self as one who is helpful and unselfish with others
              ''')
        Agreeableness=Agreeableness-Evaluate()
        print('''8. I see as my self as one who can be somewhat careless
               ''')
        Conscientiousness=Conscientiousness+Evaluate()
        print('''9. I see as my self as one who is relaxed, handles stress very well.
               ''')
        Neuroticism=Neuroticism+Evaluate()
        print('''10. I see as my self as one who is curious about many different things.
              ''')
        Openness=Openness-Evaluate()
        print('''11. I see as my self as one who is full of energy
               ''')
        Extraversion=Extraversion-Evaluate()
        print('''12. I see as my self as one who starts quarrel with others
               ''')
        Agreeableness=Agreeableness+Evaluate()
        print('''13. I see as my self as one who is a reliable worker
               ''')
        Conscientiousness=Conscientiousness-Evaluate()
        print('''14. I see as my self as one who can be tense
               ''')
        Neuroticism=Neuroticism-Evaluate()
        print('''15. I see as my self as one who is ingenious a deep thinker
               ''')
        Openness=Openness-Evaluate()
        print('''16. I see as my self as one who generates a lot of enthusiasm
               ''')
        Extraversion=Extraversion-Evaluate()
        print('''17. I see as my self as one who has a forgiving nature
               ''')
        Agreeableness=Agreeableness+Evaluate()
        print('''18. I see as my self as one who tend to be disorganized
               ''')
        Conscientiousness=Conscientiousness+Evaluate()
        print('''19. I see as my self as one who worries a lot
              ''')
        Neuroticism=Neuroticism-Evaluate()
        print('''20. I see as my self as one who has an active imagination
               ''')
        Openness=Openness-Evaluate()
        print('''21. I see as my self as one who tend to be quiet.

               ''')
        Extraversion=Extraversion+Evaluate()
        print('''22. I see as my self as one who is generally trusting
              ''')
        Agreeableness=Agreeableness-Evaluate()
        print('''23. I see as my self as one who tends to be lazy
               ''')
        Conscientiousness=Conscientiousness+Evaluate()
        print('''24. I see as my self as one who is emotionally stable not easily upset
               ''')
        Neuroticism=Neuroticism+Evaluate()
        print('''25. I see as my self as one who is inventive
               ''')
        Openness=Openness-Evaluate()
        print('''26. I see as my self as one who has an assertive personality
               ''')
        Extraversion=Extraversion-Evaluate()
        print('''27. I see as my self as one who can be cold and aloof
               ''')
        Agreeableness=Agreeableness+Evaluate()
        print('''28. I see as my self as one who preserves until the task is finished
               ''')
        Conscientiousness=Conscientiousness-Evaluate()
        print('''29. I see as my self as one who can be moody
               ''')
        Neuroticism=Neuroticism-Evaluate()
        print('''30. I see as my self as one who values artistic, aesthetic experience
               ''')
        Openness=Openness-Evaluate()
        print('''31. I see as my self as one who is sometimes shy, inhibited
              ''')
        Extraversion=Extraversion+Evaluate()
        print('''32. I see as my self as one who is considerate and kind to almost everyone
               ''')
        Agreeableness=Agreeableness-Evaluate()
        print('''33. I see as my self as one who does things efficiently
              ''')
        Conscientiousness=Conscientiousness-Evaluate()
        print('''34. I see as my self as one who remains calm in tense situations
              ''')
        Neuroticism=Neuroticism+Evaluate()
        print('''35. I see as my self as one who prefers to work that is routine
               ''')
        Openness=Openness+Evaluate()
        print('''36. I see as my self as one who is outgoing, sociable
              ''')
        Extraversion=Extraversion-Evaluate()
        print('''37. I see as my self as one who is sometimes rude to others
               ''')
        Agreeableness=Agreeableness+Evaluate()
        print('''38. I see as my self as one who makes plans and follows through with them.
              ''')
        Conscientiousness=Conscientiousness-Evaluate()
        print('''39. I see as my self as one who gets nervous easily
              ''')
        Neuroticism=Neuroticism-Evaluate()
        print('''40. I see as my self as one who likes to reflect plays with ideas.
               ''')
        Openness=Openness-Evaluate()
        print('''41. I see as my self as one who has a few artistic interests
               ''')
        Openness=Openness+Evaluate()
        print('''42. I see as my self as one who likes to cooperate with others
               ''')
        Agreeableness=Agreeableness-Evaluate()
        print('''43. I see as my self as one who is easily distracted.
               ''')
        Conscientiousness=Conscientiousness+Evaluate()
        print('''44. I see as my self as one who is sophisticated in arts, music or literature.
               ''')
        Openness=Openness-Evaluate()
        
        print('Congrats'+UserName+' for successfully completing this test \n ------Your Big 5 trait Score ------')
        print('Extraversion'+Extraversion+'\n Agreeableness'+Agreeableness+'\n Conscientiousness'+Conscientiousness+'\n Neuroticism'+Neuroticism+'\n Openness'+Openness)
        Choice=0





print("\n \n Hello "+UserName+" Your details are as follows \n Age "+str(Age)+"\n Gender "+Gender)
print("You can start the test now \n")
StartQuiz()
