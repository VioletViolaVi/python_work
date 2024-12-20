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

# stores users' guesses
all_user_guesses = []

# gets all answers then gives result @ end
for question in all_questions:
    print(" ------------------ ")
    print(question)
    for option_set in all_options[question_and_option_num]:
        print(option_set, end=" ")
        print()
    all_user_guesses.append(input("Enter your answer: ").lower()) # gets users' guess & stores it in list
    question_and_option_num += 1 # to move on to next question

print(f"all_user_guesses: {all_user_guesses}")


# score = 0
# what if they pick diff letter not a,b,c,d?
