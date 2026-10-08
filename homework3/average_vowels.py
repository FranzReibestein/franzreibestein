# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(text):
    vowels=0
    consonants=0
    string = text.lower() #to ensure that capital letters are no different from lowercase letters
    vocals = "aeiou"

    for char in string: #loop over all characters 
        if char.isalpha()==True: #if the character is a letter
            if char in vocals: #if the character is one of the character in the vocals string
                vowels+=1
            else: 
                consonants+=1
    return (vowels, consonants) #return a tuple that contains the vowel and consonants
        



# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
import re
#useful function to search for regular expressions. We will use it to cut a paragraph into sentences

def average_vowels_and_consonants(paragraph):
    sentences = re.split(r'[.?!]', paragraph) # splitting the paragraph into sentences with help of the split function of the re package. We make a split when a raw regular expression (r) is followed
    #by one of the characters ?!. (Because sentences end with one of these characters.)
    total_vowels=0
    total_consonants=0
    num_of_sentences=0
    
    for sentence in sentences:
        if sentence != "": #sentence is not empty
            num_of_sentences+=1 #reaise the sentence count by one
            v, c = counting_vowels_and_consonants(sentence) #calculate the number of vowels and consonants in this sentence with the function from ex. 1)
            total_vowels+=v # add the number of vowels in the sentence to the total vowel count
            total_consonants+=c # add the number of consonants in the sentence to the total consonant count
    avg_vowels = total_vowels/num_of_sentences 
    avg_consonants = total_consonants/num_of_sentences

    return(num_of_sentences, avg_vowels, avg_consonants)

print(average_vowels_and_consonants(paragraph))

print(f"The paragraph contains {average_vowels_and_consonants(paragraph)[0]} sentences. Every sentence has on average {average_vowels_and_consonants(paragraph)[1]} vowels and {average_vowels_and_consonants(paragraph)[2]} consonants")



    


    
