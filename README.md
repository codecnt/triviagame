# triviagame

## MVP
1. Make a trivia game  
2. Questions are created in a JSON file structure by chat GPT with the question options, the correct answer and hints
3. The trivia games are stored in the questionen.json file
4. Each player will have a username 
5. The player will decide what theme they would like to play
6. The game will present an introduction and instructions
7. While playing, it will track and provide the score
8. Once the game is over, it will present a goodbye message

## How to play
From your terminal, write "python3 trivia2.py" and press enter
Best of luck!

## Want to add more, look at the below features:
1. Leadership board for solo players stored in JSON file (started with class HighScore and leadership.json, didn't settle on the JSON structure)
    a. Would verify if the existing user name exists
    b. Add as a key and value the user name and score
    c. Ensure that the key and value are added in the order of highest to lowest scores
    d. Inform players of their position number
    e. send a celebratory message if the player made it to the top 3 of the theme
2. Option for playing solo in a group or at an event 
3. Play it from a friendly GUI with a button for answers instead of having to type
4. Add the ChatGPT API to generate any theme preferred and add it to the questionsen.json file
5. Create a library to store and avoid unnecessary queries to JSON file temporarily
6. Organizations can personalize, and donations will go to their business PayPal account
7. Create options to buy answers and buy hints (fundraising purposes)
8. Leadership board for groups and events
9. The final dashboard for group and events game will include the total raised per table and scores
10. Limited time to answer each question, stopwatch per question per round, and player can go back x amount of times. 


## How to play your own theme:

Start by cloning this GitHub repository, and ask chatGPT to create a Trivia game with the theme you would like to play. Remember, it must have the same structure as the rest of the file.

In the trivia2.py file you will need to modify 2 sections of the code:

### First change - 
In the accessjson method change the else of elif self.theme == "Super Heroes": and add
 else: 
    chosen_theme_index = 2

    def accessjson(self):
        
        with open ('questionsen.json') as json_file_q_en:
            python_dict_q_en = json.load(json_file_q_en)
        
        if self.theme == "Food":
            chosen_theme_index = 0
        else:
            chosen_theme_index = 1

        chosen_theme = python_dict_q_en["trivia_game"][chosen_theme_index]
        
        return chosen_theme

### Second change - 
Add as a third choice the name of your theme. 

choice = input("Hi, " + player_name + "! Let's pick our game! Would you like to play a 1-Food or 2-Super Heroes game? (Write 1 or 2 and press enter): ")

while choice != '1' and choice != '2':
  choice = input("Whoops, it looks like you didn't choose '1' for Food or '2' for Super Heroes. Try selecting one again!")


if choice == '1':
  game = Trivia("Food")
  active_user = Player(player_name, "Food")
else:
  game = Trivia("Super Heroes")
  active_user = Player(player_name, "Super Heroes")



Thanks for taking the time to read my first project. Appreciate any feedback you can provide.
