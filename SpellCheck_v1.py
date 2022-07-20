#Check to see if spelling of a paragraph is correct     By: Charlotte

#Make sure you download words.txt before running

from ast import While


def word_check(word):   #Checks spelling for individual words
    with open ("words.txt", "r") as word_spell:
        word = word.lower()

        word = word + '''
'''                     #in words.txt there is a new line after every word 

        spelling = "incorrect"

        for line in word_spell:
            if word == line:
                spelling = "correct"
                word_spell.close()
                break
            if word != line:
                pass

        if spelling=="incorrect":
            ""
        return(spelling)


def in_alpha(letter):  #checks to see if letter is in alphabet
    alpha = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","'")
    letter = letter.lower()   #Changes letter to lowercase because alpha is all lowercased
    if letter in alpha:
        return(True)
    else:
        return(False)

while True:
    #Checks spelling of a paragraph
    paragraph = input("Type a paragraph to check the spelling: ")
    parword = ""   #paragraph word
    ex_notLetter = True
    one_incorrect_word = False   #is there at least 1 incorrect word?


    for char in paragraph:
        if in_alpha(char) == False:   #if there is a space or period
            if ex_notLetter == True:
                continue
            elif word_check(parword) == "incorrect":  #check to see if word before is correct
                print(f"{parword} is spelt incorrectly.")
                parword = ""
                one_incorrect_word = True
            elif word_check(parword) == "correct":
                parword = ""
            ex_notLetter = True

                
        if in_alpha(char) == True:
            ex_notLetter = False
            parword = parword + char   #add the current char to parword
            
    #the loop doesn't check the last word
    if ex_notLetter == True:
        ""
    elif in_alpha(char) == False:
        ""
    elif word_check(parword) == "incorrect":
        print(parword,"is spelt incorrectly.")
        one_incorrect_word = True

    if one_incorrect_word == False:
        print("There are no misspelled words! :D")
