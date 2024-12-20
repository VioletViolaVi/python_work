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

# question counter
question_num = -1

for question in all_questions:
    print(" ------------------ ")
    print(question)
    question_num += 1
    for option_set in all_options[question_num]:
        print(option_set, end=" ")
        print()


# guesses = []
# score = 0

# print(all_questions): ('In the nursery rhyme, who had a farm?', 'If you freeze water, what do you get?', 'How many legs does a spider have?', 'Where does Santa Claus live?', 'On which holiday do you go trick-or-treating?')

# print(question): In the nursery rhyme, who had a farm?
                 # If you freeze water, what do you get?
                 # How many legs does a spider have?
                 # Where does Santa Claus live?
                 # On which holiday do you go trick-or-treating?


# print(option_set): ('A) Little Bo Peep', 'B) Old MacDonald', 'C) The Muffin Man', 'D) Jack and Jill')
                   # ('A) Ice', 'B) Lava', 'C) Fire', 'D) Wind')
                   # ('A) Six', 'B) Four', 'C) Eight', 'D)Zero')
                   # ('A) Loc Ness', 'B) The North Pole', 'C) Atlantis', 'D) Townsville')
                   # ('A) Christmas', 'B) Easter', 'C) Valentines Day', 'D) Halloween')
                   # ('A) Little Bo Peep', 'B) Old MacDonald', 'C) The Muffin Man', 'D) Jack and Jill')
                   # ('A) Ice', 'B) Lava', 'C) Fire', 'D) Wind')
                   # ('A) Six', 'B) Four', 'C) Eight', 'D)Zero')
                   # ('A) Loc Ness', 'B) The North Pole', 'C) Atlantis', 'D) Townsville')
                   # ('A) Christmas', 'B) Easter', 'C) Valentines Day', 'D) Halloween')
                   # ('A) Little Bo Peep', 'B) Old MacDonald', 'C) The Muffin Man', 'D) Jack and Jill')
                   # ('A) Ice', 'B) Lava', 'C) Fire', 'D) Wind')
                   # ('A) Six', 'B) Four', 'C) Eight', 'D)Zero')
                   # ('A) Loc Ness', 'B) The North Pole', 'C) Atlantis', 'D) Townsville')
                   # ('A) Christmas', 'B) Easter', 'C) Valentines Day', 'D) Halloween')
                   # ('A) Little Bo Peep', 'B) Old MacDonald', 'C) The Muffin Man', 'D) Jack and Jill')
                   # ('A) Ice', 'B) Lava', 'C) Fire', 'D) Wind')
                   # ('A) Six', 'B) Four', 'C) Eight', 'D)Zero')
                   # ('A) Loc Ness', 'B) The North Pole', 'C) Atlantis', 'D) Townsville')
                   # ('A) Christmas', 'B) Easter', 'C) Valentines Day', 'D) Halloween')
                   # ('A) Little Bo Peep', 'B) Old MacDonald', 'C) The Muffin Man', 'D) Jack and Jill')
                   # ('A) Ice', 'B) Lava', 'C) Fire', 'D) Wind')
                   # ('A) Six', 'B) Four', 'C) Eight', 'D)Zero')
                   # ('A) Loc Ness', 'B) The North Pole', 'C) Atlantis', 'D) Townsville')
                   # ('A) Christmas', 'B) Easter', 'C) Valentines Day', 'D) Halloween')                

# print(f"question_num: {question_num}"): question_num: 0
                                        # question_num: 1
                                        # question_num: 2
                                        # question_num: 3
                                        # question_num: 4
