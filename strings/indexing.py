# String Indexing

abc_song = "abc-def-ghi-jkl-mno-pqr-stu-vwx-yz"
print(f"abc_song[2]: {abc_song[2]}")
print(f"abc_song[8]: {abc_song[8]}")
print(f"abc_song[-1]: {abc_song[-1]}")
print(f"abc_song[13]: {abc_song[13]}")
print(f"abc_song[0]: {abc_song[0]}")
print(f"abc_song[-4]: {abc_song[-4]}")



print(" --- new --- ")



# [start : end : step]
abc_song_2 = "abc-def-ghi-jkl-mno-pqr-stu-vwx-yz"

print(f"abc_song_2[0 : 3 : 1]: {abc_song_2[0 : 3 : 1 ]}")

print(abc_song_2.find("s"))
print(f"make 'stu': {abc_song_2[24:27:1]}")
print(f"make 'stu': {abc_song_2[24:27:1]}")

number_chain = "0123456789"

even_only = number_chain[0:len(number_chain):2]
odd_only = number_chain[1:len(number_chain):2]
divisible_by_3 = number_chain[0:len(number_chain):3]
divisible_by_4 = number_chain[0:len(number_chain):4]

divisible_by_34 = number_chain[0:len(number_chain):34]

print(f"length: {len(number_chain)}")
print(f"even only: {even_only}")
print(f"odd only: {odd_only}")
print(f"divisible by 3: {divisible_by_3}")
print(f"divisible by 4: {divisible_by_4}")

print(f"divisible by 34: {divisible_by_34}")



print(" --- new --- ")



# [start : end : step] part 2

colours = "red | yellow | pink | green | black | orange"

print(len(colours))

stepping = colours[0::2]
print(stepping)
stepping_2 = colours[2:35:3]
print(stepping_2)
stepping_3 = colours[6:27:5]
print(stepping_3)
stepping_4 = colours[:20:2]
print(stepping_4)

print(colours.find("orange"))
orange_word = colours[38:]
print(f"orange_word: {orange_word}")
orange_word = colours[colours.find("orange"):]
print(f"orange_word: {orange_word}")

print(colours.find("red"))
red_word = colours[0:3]
print(f"red_word: {red_word}")
red_word = colours[colours.find("red"):3]
print(f"red_word: {red_word}")

print(colours.find("black"))
black_word = colours[30:35]
print(f"black_word: {black_word}")
black_word = colours[colours.find("black"):35]
print(f"black_word: {black_word}")

print(colours.find("pink"))
print(colours.find(" | green"))
pink_word = colours[15:19]
print(f"pink_word: {pink_word}")
pink_word = colours[colours.find("pink"):colours.find(" | green")]
print(f"pink_word: {pink_word}")

print(colours.find("green"))
print(colours.find(" | black"))
green_word = colours[22:27]
print(f"green_word: {green_word}")
pink_word = colours[colours.find("green"):colours.find(" | black")]
print(f"green_word: {green_word}")

print(colours.find("yellow"))
print(colours.find(" | pink"))
yellow_word = colours[6:12]
print(f"yellow_word: {yellow_word}")
yellow_word = colours[colours.find("yellow"):colours.find(" | pink")]
print(f"yellow_word: {yellow_word}")
