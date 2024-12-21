# Python Quiz Game

# Questions (some) taken from:
    # https://parade.com/944584/parade/trivia-questions-for-kids/

# questions
question_1 = "In the nursery rhyme, who had a farm?"
question_2 = "If you freeze water, what do you get?"
question_3 = "How many legs does a spider have?"
question_4 = "Where does Santa Claus live?"
question_5 = "On which holiday do you go trick or treating?"

# options
question_1_options = ("A) Little Bo Peep", "B) Old MacDonald", "C) The Muffin Man", "D) Jack and Jill")
question_2_options = ("A) Ice", "B) Lava", "C) Fire", "D) Wind")
question_3_options = ("A) Six", "B) Four", "C) Eight", "D) Zero")
question_4_options = ("A) Loc Ness", "B) The North Pole", "C) Atlantis", "D) Townsville")
question_5_options = ("A) Christmas", "B) Easter", "C) Valentines Day", "D) Halloween")

# answers
question_1_answer = "B" # Old MacDonald
question_2_answer = "A" # Ice
question_3_answer = "C" # Eight
question_4_answer = "B" # The North Pole
question_5_answer = "D" # Halloween

# nested tuples using above values
all_questions = (question_1, question_2, question_3, question_4, question_5) # strings
all_options = (question_1_options, question_2_options, question_3_options, question_4_options, question_5_options) # tuples
all_answers = (question_1_answer, question_2_answer, question_3_answer, question_4_answer, question_5_answer) # strings

# question / option set counter
question_and_option_num = 0

# stores user guesses
all_user_guesses = []

# holds score
score = 0

# gets all answers then gives result @ end
for question in all_questions:
    print(" ------------------ ")
    print(question) # prints *1 question
    for option_set in all_options[question_and_option_num]:
        print(option_set, end=" ") # prints all options to *1 question
        print()

    # part of outer loop
    user_input = input("Enter your answer: ").upper()

    # ensures only A, B, C or D can be selected
    while not user_input == "A" and not user_input == "B" and not user_input == "C" and not user_input == "D":
        print("Not Valid. Choose between A, B, C and D")
        user_input = input("Enter your answer: ").upper()

    all_user_guesses.append(user_input) # gets each guess, capitalises it & stores in list

    if all_answers[question_and_option_num] == all_user_guesses[question_and_option_num]: # comparing answers w/ guesses
        score += 1
        print(f"Correct!") # right answer given
    else:
        print(f"Wrong! Correct answer: {all_answers[question_and_option_num]}") # wrong answer given, shows right answer

    question_and_option_num += 1 # to move on to next question

print(" --------- RESULT --------- ")

# dynamic variables for displaying results
score_feedback = ("Dreadful", "Bad", "Okay", "Good", "Great", "WOW") # index positions: [ 0 -> 1 -> 2 -> 3 -> 4 -> 5 ]
score_emoji = ("😧", "☹️", "😐", "🙂", "😀", "🥳") # index positions: [ 0 -> 1 -> 2 -> 3 -> 4 -> 5 ]
score_percentage = (score/len(all_questions)) * 100 # percentage calculation

# conditional messages for specific scores
if score:
    print(f"{score_feedback[score]}! You scored: {score}/{len(all_questions)}! ({score_percentage}%) {score_emoji[score]}")
elif score == 0:
    print(f"{score_feedback[score]}! You scored: {score}/{len(all_questions)}! ({score_percentage}%) {score_emoji[score]}")
else:
    print("ERROR!!! 😶")
