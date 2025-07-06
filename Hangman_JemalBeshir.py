#Jemal Beshir
#steps / thought process
#get input of the word
# define word
#put the word into a loop where the if the input of the
# user isn't contained in the word, then strike or
#counter is increased
#once counter hits 5, game over
#2 main ifs loops i believe
hangman_word = input("Please enter the word:")
hangman_word = hangman_word.upper()
counter = 0
letters_used = ""
while counter != 5:
    shown_word = ""
    letter = input("Please give a letter")
    if letter == "quit":
        break
    letter = letter.upper()
    if letter in letters_used:
            print("WORD ALREADY USED")

    else:
            letters_used += letter
            if letter not in hangman_word:
                counter+=1
            #added the if to the else loop because I kept
            #seeing that duplicated guesses were 
            #accounted for strikes. if I were to account
            #for it. I would take the if loop out of this
            #else loop and let it be a part of the while loop,
            #after the if letter in letters_used loop.

    for char_guess in hangman_word:
        if char_guess in letters_used:
            shown_word += char_guess
        else:
            shown_word += "-"
    if shown_word == hangman_word:
        print("You Have Won!!!")
        break


    print("You have used these letters:", letters_used)
    print("You have this many strikes now:", counter)


if counter == 5:
    print("You have lost!, the word was", hangman_word)



        