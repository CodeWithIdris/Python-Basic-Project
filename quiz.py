users_list  = []
users_score = []

score = 0
def playquiz():
    global score, name, question
    question = {
        "In a website browser address bar, what does “www” stand for?": "A",
        "In what year were the first Air Jordan sneakers released?": "C",
        "According to Greek mythology, who was the first woman on earth?": "B",
        "Which African country was formerly known as Abyssinia?": "B",
        "Tennis star Serena Williams won which major tournament while pregnant with her first child?": "A",
        "Which country consumes the most chocolate per capita?": "C",
        "How many ribs are in a human body?": "A",
        "Which bone are babies born without?": "A",
        "What is the name of the group of men who elect a Pope?": "B",
        "Water has a pH level of around?": "B"
    }
    options = [
            ["A. World Wide Web", "B. Wide Web Window", "C. Window Web Wide"], 
            ["A. 1999", "B. 1986", "C. 1984"], 
            ["A. Flower", "B. Pandora", "C. Salt"], 
            ["A. Egypt", "B. Ethiopia", "C. Saudi Arabia"], 
            ["A. The Australian Open", "B. The South-Africa Open", "C. UK Open"],
            ["A. Australia", "B. South-Africa", "C. Switzerland"], 
            ["A. 24", "B. 32", "C. 22"], 
            ["A. Knee Cap", "B. Limb", "C. Brain"], 
            ["A. Section of Tranquility", "B. College of Cardinals", "C. Team Of The Highway"],
            ["A. 5", "B. 7", "C. 8.1"]
            ]

    name = input("Enter your name: ")
    
    sn = 1
    for k in question.keys():
        print(f"{sn}. {k}")
        for x in options[sn - 1]:
            print(x)
        user = input("Enter your answer: ").upper()
        if user == question.get(k):
            print("Correct")
            score += 1
        else:
            print("wrong")
        print("------------------------------------------")   
        sn += 1

def show_score():
    que_len = len(question)
    percentage = score/que_len * 100
    print(f"{name} you scored {score}/{que_len}")
    print(f"{name} you scored {percentage}%")

def show_status():
    if score > 5:
        print("Congrats. You passed the quiz")
    elif score < 5:
        print("Sorry, You failed the quiz")

def players_list():
    users_list.append(name)

def players_score():
    users_score.append(score)

def all_scores():
    global users_list, users_score
    for i in range(len(users_list)):
        print("Username\tScore")
        print(users_list[i],"\t\t",users_score[i])

def search_user():
    user = input("Enter name: ")
    if user in users_list:
        index = users_list.index(user)
        print("Username\tScore")
        print(f"{user}\t\t{users_score[index]}")
    else:
        print(f"{user} does not exist")

while True:
    playquiz()
    players_list()
    players_score()
    
    reply = input("Do you want to view your status(y/n): ")
    if reply == "y":
        show_status()    
    else:
        quit()

    reply = input("Do you want to view your score(y/n): ")
    if reply == "y":
        show_score()
        score = 0
        
    else:
        quit()

    reply = input("Do you want to view all scores?(y/n): ")
    if reply == "y":
        all_scores()
    else:
        quit()

    reply = input("Do you want to search for your result?(y/n): ")
    if reply == "y":
        search_user()
    else:
        quit()
    
    reply = input("Do you want to restart or quit?(y/n): ")
    if reply == "y":
        continue
    else:
        quit()

