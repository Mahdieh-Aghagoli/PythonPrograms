import random

words = ["rabbit", "peach", "car", "orange", "hammer", "parrot", "bike", "glasses", "pencil", "refrigerator"]

# answers: Each key has a list of words that answer yes to the key
answers = {"1": ["peach", "orange", "hammer", "parrot", "glasses", "pencil"], "2": ["peach", "orange"],
           "3": ["rabbit", "parrot"], "4": ["car", "bike"], "5": ["glasses", "pencil"], "6": ["peach", "orange"],
           "7": ["rabbit", "parrot"], "8": ["hammer"], "9": ["parrot"], "10": ["car", "bike"], "11": ["pencil"],
           "12": ["refrigerator"], "13": ["refrigerator"], "14": [], "15": [], "16": [], "17": ["parrot"],
           "18": ["pencil"], "19": [], "20": [], "21": ["bike"], "22": [], "23": ["peach", "orange"], "24": ["parrot"]}

questions = ["Does it fit in pocket", "Is it edible", "Is it alive", "Is it a mechanical device", "Is it fragile",
             "Is it fruit", "Is it an animal", "Is it a tool", "Is it a bird", "Is it a vehicle", "Is it stationery",
             "Is it a kitchen appliance", "Does it work with electricity", "Is it aquatic", "Is it nuts",
             "Is it an insect", "Does it fly", "Is it made of wood", "Are they creepy", "Is it a public vehicle",
             "Does it have two wheels", "Is it amphibian", "Does it have a core?", "Does speak"]


def game():
    guess_number = 1
    user_guesses = {}
    current_score = 100
    counter = 0
    print("\n1.{}\n2.{}\n3.{}\n4.{}\n5.{}\n6.{}\n7.{}\n8.{}\n9.{}\n10.{}\n11.{}\n12.{}\n13.{}\n14.{}\n"
          "15.{}\n16.{}\n17.{}\n18.{}\n19.{}\n20.{}\n21.{}\n22.{}\n23.{}\n24.{}\n".format(*questions))

    while current_score != 0 and counter != 20:
        # Checking the conditions for continuing the game
        print("\nyou can ask me {} question".format(20 - counter))

        option = input("Choose a question or enter 0 for new guess: ")
        if 1 <= int(option) < 25:
            # Displaying the answer of the selected question
            counter += 1
            current_score -= 5
            if random_choice in answers[option]:
                answer = "Yes"
            else:
                answer = "No"
            print("{}? {}\nCurrent Score = {}".format(questions[int(option) - 1], answer, current_score))
        elif int(option) == 0:
            # Checking the player's guess
            choice = input("New guess: ")
            user_guesses[guess_number] = choice
            guess_number += 1
            if ''.join(choice.lower().split(' ')) == random_choice:
                current_score += 20
                print(
                    "That's right.You won:)\nCurrent Score= {}\nAll your guesses{}".format(current_score, user_guesses))
                return
            else:
                current_score -= 10
                print("Wrong guess!\nCurrent Score= " + str(current_score))
        else:
            print("\n\aChoose a number between 0 and 24")
    print("You lose:( and Selective random word: " + random_choice)


random_choice = random.choice(words)
game()
