#"Generate the word
import random
import hangmanStages
word_list=['apple','beautiful','fatima']
chose_word = random.choice(word_list)
length = len(chose_word)
lives=6
blank = '_'

list = []

for i in range(1,length+1):
    list.append(blank)
print(list)
game_over=False
while not game_over:
    guess = input("guess the letter : ").lower()
    for position in range(length):
        letter =chose_word[position]
        if letter==guess:
            list[position]=guess
    print(list)
    if guess not in chose_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!!")

    if  '_' not in list:
        game_over=True
        print("You Win!!")

    print(hangmanStages.stages[lives])