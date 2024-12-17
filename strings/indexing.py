# # String Indexing

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
