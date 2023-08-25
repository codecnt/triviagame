import logging
import os
from dotenv import load_dotenv
import json

class Trivia:
    def __init__(self, theme):
        self.theme = theme
        # sectionnum, questionnum, optionsnum
        # self.sectionnum = sectionnum
        # self.questionnum = questionnum
        # self.optionsnum = optionsnum

    def __repr__(self):
        return "This trivia game will be {theme} theme".format(theme = self.theme)
    
    def accessjson(self):
        
        with open ('questionsen.json') as json_file_q_en:
            python_dict_q_en = json.load(json_file_q_en)
        
        if self.theme == "Food":
            chosen_theme_index = 0
        else:
            chosen_theme_index = 1

        chosen_theme = python_dict_q_en["trivia_game"][chosen_theme_index]
        
        return chosen_theme
    
    def accessintr(self):
        chosen_theme = self.accessjson()
        introdox = chosen_theme["introduction"]
        return introdox

    def accesssection(self, num1):
        self.num1 = num1
        chosen_theme = self.accessjson()
        sectionlist = []
        for section in chosen_theme["sections"]:
            sectionsprelist = (section["title"])
            sectionlist.append(sectionsprelist)
        return sectionlist[num1]
    
    def accessquestion(self, num2):
        self.num2 = num2
        chosen_theme = self.accessjson()
        questionlist = []
        for section in chosen_theme["sections"]:
            for question in section["questions"]:
                questionsprelist = (question["question"])
                questionlist.append(questionsprelist)
        return questionlist[num2]

    def accessoptions(self,num2):
        self.num2 = num2
        chosen_theme = self.accessjson()
        optionlist = []
        for section in chosen_theme["sections"]:
            for question in section["questions"]:
                optionsprelist = (question["options"])
                optionlist.append(optionsprelist)
        return optionlist[num2]

    def accessoption(self, num2, num3):
        self.num2 = num2
        self.num3 = num3

        chosen_theme = self.accessjson()
        optionlist = []
        for section in chosen_theme["sections"]:
            for question in section["questions"]:
                optionsprelist = (question["options"])
                optionlist.append(optionsprelist)
        return optionlist[num2][num3]
    

class Player:
    def __init__(self, user, theme, score = 0):
        self.user = user
        self.theme = theme
        self.score = score
        self.user_score = score

    def __repr__(self):
        return "{user} Let's win!".format(user = self.user)

    def nose(self):
        # return print("YEY")
        self.user_score += 1
        print("You scored! Current balance: " + str(self.user_score))

    def accessjson(self):
        
        with open ('questionsen.json') as json_file_q_en:
            python_dict_q_en = json.load(json_file_q_en)
        
        if self.theme == "Food":
            chosen_theme_index = 0
        else:
            chosen_theme_index = 1

        chosen_theme = python_dict_q_en["trivia_game"][chosen_theme_index]
        
        return chosen_theme

    def accessanswer(self, num2):
        chosen_theme = self.accessjson()
        answerslist = []
        for section in chosen_theme["sections"]:
            for question in section["questions"]:
                answersprelist = (question["correct_answer"])
                answerslist.append(answersprelist)
        return(answerslist[num2])



class HighScore:
    def __init__(self, user):
        self.theme = theme
        self.user = user
        
        pass


player_name = input("Welcome to trivia. Please enter a name for player one and hit enter: ")

choice = input("Hi, " + player_name + "! Let's pick our game! Would you like to play a 1-Food or 2-Super Heroes game? (Write 1 or 2 and press enter): ")

while choice != '1' and choice != '2':
  choice = input("Whoops, it looks like you didn't choose '1' for Food or '2' for Super Heroes. Try selecting one again!")


if choice == '1':
  game = Trivia("Food")
  active_user = Player(player_name, "Food")
else:
  game = Trivia("Super Heroes")
  active_user = Player(player_name, "Super Heroes")
  
print(game)

print(game.accessintr())

print(active_user)

print("After each question and options are presente type your answer, remember to use same spelling and capital letters! GOOD LUCK")

print("If you need to stop the game at any point press ctrl + C")

for i in range(25):

    choice = input(str(print(game.accessquestion(i))) + str(print(game.accessoptions(i))))

    while choice != str(game.accessoption(i,0)) and choice != str(game.accessoption(i,1)) and choice != str(game.accessoption(i,2)) and choice != str(game.accessoption(i,3)):
        choice = input("Whoops, it looks like you didn't choose. Try selecting one again!")

    if choice == str(active_user.accessanswer(i)):
        active_user.nose()
    else:
        print("Keep trying you will get there")


print("Well done! You finished the game! You will now forever be remembered in our leadership board")
