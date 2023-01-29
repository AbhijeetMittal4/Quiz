#import matplotlib.pyplot as plt

print("Hello by taking this quiz you can know which Marvel/DC character you resemble the most")
print("The quiz will havea few questions for which you will be given 4 options for each question")
print("You need to select option by , like if you want to select option A type A for option B type B")


batmanpts = 0  
supermanpts = 0
ironmanpts = 0
drstrangepts = 0                       
scarlettwitchpts = 0                            
thanospts = 0
darksiedpts = 0
ghostriderpts = 0
lokipts = 0 

a=0



#q1 = input("Q1- What is  your main priority \n A| Saving People \n B| Eliminating threat \n C| Completing Obective \n D| Saving yourself \n Your option - ")
#q2 = input("Q2- What is  your goal \n A| Getting successfull in life \n B| Achieving a certain goal \n C| Living happily with family or friends \n D| Don't know \n Your option - ")
#q3 = input("Q3- You are  \n A| Hero \n B| Anti-Hero \n C| Villian \n D| Anti-Villian \n Your option - ")
#q4 = input("Q4- Who would you like as your sidekick \n A| Someone from your family \n B| Best friend \n C| Someone who you can control \n D| Will do it alone \n Your option - ")
#q5 = input("Q5- Best way to defeat enemy \n A| Overwhelm them with your power \n B| Exploit weakness  \n C| Try to bring them on your side \n D| Keep fighting hope for the best \n Your option - ")
#q6 = input("Q6-  \n A| Getting successfull in life \n B| Achieving a certain goal \n C| Living happily with family or friends \n D| Don't know \n Your option - ")


#Q1
while a != 1:
    q1 = input("Q1- What is  your main priority \n A| Saving People \n B| Eliminating threat \n C| Completing Obective \n D| Saving yourself \n Your option - ")
    q1 = q1.upper()
    if (q1=="A" or q1=="B" or q1=="C" or q1=="D"):
        if q1 == "A" or "a":
            supermanpts += 1 
            ironmanpts += 1
        elif q1 == "B" or "b":
            batmanpts += 1
            ghostriderpts += 1
            ironmanpts += 1
            drstrangepts += 1
        elif q1 == "C" or "c":
            batmanpts += 1
            lokipts += 1
            thanospts += 1
            scarlettwitchpts += 1
            darksiedpts += 1
            ironmanpts +=1
            drstrangepts += 1                                          
        elif q1 == "D" or "d":
            lokipts += 1 
            darksiedpts += 1
        a += 1
    elif not(q1=="A" or q1=="B" or q1=="C" or q1=="D"):
            print("You selected an invalid option pls select your option again")


#Q2
while a!=2:
    q2 = input("Q2- What is  your goal \n A| Getting successfull in life \n B| Achieving a certain goal \n C| Living happily with family or friends \n D| Don't know \n Your option - ")
    q2 = q2.upper()
    if (q2=="A" or q2=="B" or q2=="C" or q2=="D"):
        if q2 == "A":
            lokipts += 1
            darksiedpts += 1
        elif q2 == "B": 
            batmanpts += 1
            ironmanpts += 1
            drstrangepts += 1
            thanospts += 1
            darksiedpts += 1
            ghostriderpts += 1
        elif q2 == "C":
            supermanpts += 1
            scarlettwitchpts += 1                                          
        elif q2 == "D":
            lokipts += 1 
            batmanpts += 1
        a += 1
    elif not(q2=="A" or q2=="B" or q2=="C" or q2=="D"):
        print("You selected an invalid option pls select your option again")


#Q3
while a!=3:
    q3 = input("Q3- You are  \n A| Hero \n B| Anti-Hero \n C| Villian \n D| Anti-Villian \n Your option - ")
    q3 = q3.upper()    
    if (q3=="A" or q3=="B" or q3=="C" or q3=="D"):
        if q3 == "A":
            supermanpts += 1
            ironmanpts += 1
            drstrangepts += 1

        elif q3 == "B": 
            batmanpts += 1 
            ghostriderpts += 1

        elif q3 == "C":
            darksiedpts += 1

        elif q3 == "D":
            lokipts += 1
            scarlettwitchpts += 1
        a += 1    
    elif not(q3=="A" or q3=="B" or q3=="C" or q3=="D"):
        print("You selected an invalid option pls select your option again")


#Q4
while a !=4:
    q4 = input("Q4- Who would you like as your sidekick \n A| Someone from your family \n B| Best friend \n C| Someone who you can control \n D| Will do it alone \n Your option - ")
    q4 = q4.upper()
    if (q4=="A" or q4=="B" or q4=="C" or q4=="D"):
        if q4 == "A":
            scarlettwitchpts += 1
        elif q4 == "B": 
              ironmanpts += 1
              supermanpts += 1
        elif q4 == "C":
            darksiedpts += 1 
            thanospts += 1
            batmanpts += 1                                               
        elif q4 == "D":
            drstrangepts += 1
            ghostriderpts += 1
            lokipts += 1
        a += 1
    elif not(q4=="A" or q4=="B" or q4=="C" or q4=="D"):
        print("You selected an invalid option pls select your option again")


#Q5
while a != 5:
    q5 = input("Q5- Best way to defeat enemy \n A| Overwhelm them with your power \n B| Exploit weakness  \n C| Try to bring them on your side \n D| Keep fighting hope for the best \n Your option - ")
    q5 = q5.upper()
    if (q5=="A" or q5=="B" or q5=="C" or q5=="D"):
        if q5 == "A":
            scarlettwitchpts += 1
            ghostriderpts += 1
            darksiedpts += 1 
            thanospts += 1
        elif q3 == "B":
            batmanpts += 1 
            thanospts
        elif q3 == "C":
            lokipts += 1
            darksiedpts += 1
        elif q3 == "D":
            supermanpts += 1
            ironmanpts += 1
            drstrangepts += 1
        a += 1
    elif not(q5=="A" or q5=="B" or q5=="C" or q5=="D"):
        print("You selected an invalid option pls select your option again")


#Q6
while a != 5:
    q6 = input("Q6- Favourite thing to kill time  \n A| Reading \n B| Playing Games \n C| Thinking \n D| Listening to Music - ")
    q6 = q6.upper()
    if (q6=="A" or q6=="B" or q6=="C" or q6=="D"):
        if q5 == "A":
            drstrangepts += 1
            thanospts += 1
        elif q3 == "B":
            ironmanpts += 1
            darksiedpts += 1
        elif q3 == "C":
            batmanpts += 1
            lokipts += 1
        elif q3 == "D":
            scarlettwitchpts += 1
            ghostriderpts += 1
            supermanpts += 1
        a +=   1
    elif not(q5=="A" or q5=="B" or q5=="C" or q5=="D"):
        print("You selected an invalid option pls select your option again")

z  = {'BATMAN':batmanpts  ,  'IRON MAN':ironmanpts,  'DARKSEID':darksiedpts, 'THANOS':thanospts, 'SCARLETT WITCH':scarlettwitchpts, 'GHOST RIDER':ghostriderpts,'LOKI':lokipts,'SUPERMAN':supermanpts,'DR. STRANGE':drstrangepts}
z1 = [batmanpts , ironmanpts , darksiedpts , thanospts , scarlettwitchpts , ghostriderpts , lokipts , supermanpts , drstrangepts]


b = max(z1)
for y in z:
    if z[y] == b:
        x = y
        break 


if x == "BATMAN":
    reason = "I AM VENGEANCE"
elif x == "IRON MAN":
    reason = "I AM IRON MAN"
elif x == "DARKSEID":
    reason = "ALL OF EXISTENCE SHALL BE MINE!"
elif x == "THANOS":
    reason = "I AM INEVITABLE"
elif x == "SCARLETT WITCH":
    reason = "YOU BREAK THE RULES AND BECOME A HERO"
elif x == "GHOST RIDER":
    reason = "SO MANY VICTIMS FEEL THEIR PAIN!"
elif x == "LOKI":
    reason = "YOUR SAVIOUR IS HERE!"
elif x == "SUPERMAN":
    reason = "IT'S NEVER AS BAD AS IT SEEMS"
elif x == "DR. STRANGE":
    reason = "DORMAMMU, I'VE COME TO BARGAIN."






print(f'YOU ARE {x}\n{reason}')
