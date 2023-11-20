def de_vowel(ad):
    for i in range (1, len(ad)):
        # if vowel = is_vowel(ad[i])
        # if is_vowel(c) and is_vowel(ad[i]):
        if is_vowel(ad[i]):
            ad = ad[:i] + ad [i+1:]
            
    return ad




def is_vowel(c):
    if c in 'aeiouAEIOU':
        return True
    else:
        return False

# c = "aeiouAEIOU"
ad = "Desirable unfurnished flat in quiet residential area"
print (de_vowel(ad))
