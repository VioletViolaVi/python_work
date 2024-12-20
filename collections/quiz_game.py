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
    all_user_guesses.append(input("Enter your answer: ").upper()) # gets each guess, capitalises it & stores in list

    if all_answers[question_and_option_num] == all_user_guesses[question_and_option_num]: # comparing answers w/ guesses
        score += 1

    question_and_option_num += 1 # to move on to next question

# done with loops
print(f"You scored: {score}/5!")
# what if they pick diff letter not a,b,c,d?
