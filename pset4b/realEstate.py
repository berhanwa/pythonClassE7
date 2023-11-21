# Defined the de_vowel function where in the for loop that runs through the ad,
# checks if there are vowels and then puts the remaining characters inside the vowelless_ad variable
def de_vowel(ad):
    vowelless_ad = ''
    for i in range (0, len(ad)):
        if not(is_vowel(ad[i]) and i != 0 and ad[i-1]!=' '):
            vowelless_ad += ad[i]
    return vowelless_ad

# Then defined the function is_vowel to return true or false depending on whether or not the character has a vowel
def is_vowel(c):
    if c in 'aeiouAEIOU':
        return True
    else:
        return False

ad = "Desirable unfurnished flat in quiet residential area"
print (de_vowel(ad))