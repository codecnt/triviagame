import json

# Define the load_all_questions function
def load_all_questions():
    with open('questionsen.json', 'r') as json_file_q_en:
        python_dict_q_en = json.load(json_file_q_en)
    return python_dict_q_en["trivia_game"]

def ask_question(question, choices):
    while True:
        print(question)
        for idx, choice in enumerate(choices, start=1):
            print(f"{idx}) {choice}")
        try:
            choice_num = int(input("Choice: "))
            if 1 <= choice_num <= len(choices):
                return choice_num - 1
            else:
                print(f"{choice_num} is not a valid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid choice number.")

# Load all questions
all_questions = load_all_questions()

player_name = input("Welcome to trivia. Please enter a name for player one and hit enter: ")

print("Hi, " + player_name + " If you need to stop the game at any point press ctrl + C \n \n")

# Choose a theme
theme_choices = [theme["theme"] for theme in all_questions]
choicetheme = ask_question("Choose a theme:", theme_choices)
selected_theme = theme_choices[choicetheme]
chosen_theme = next(theme for theme in all_questions if theme["theme"] == selected_theme)

sscore = 0

# Iterate through sections and questions
for section in chosen_theme["sections"]:
    print(f"\nSection: {section['title']}")
    for question in section["questions"]:
        question_text = question["question"]
        options = question["options"]
        answer = question["correct_answer"]

        choice = ask_question(question_text, options)
        selected_option = options[choice]
        print("You chose:", selected_option)
        if selected_option == answer:
            sscore += 1
            print("You got it right! your score is: " + str(sscore))
        else:
            print("Keep trying your score is still " + str(sscore))
        print()

print("Game Over")
