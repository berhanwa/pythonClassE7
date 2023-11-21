def is_vowel(c):
    # c = ' '
    if c in 'aeiouAEIOU':
        return True
    else:
        return False

def de_vowel(ad):
    vowelless_ad = ' '
    for i in range (0, len(ad)):
        # if vowel = is_vowel(ad[i])
        # if is_vowel(c) and is_vowel(ad[i]):
        # if is_vowel(ad[i]) and ad[i-1]!=' ':
        if is_vowel(c) and i != 0 and ad[i-1]!=' ':
            # ad += vowelless_ad
            vowelless_ad = vowelless_ad[:i] + vowelless_ad[i+1:]
    return vowelless_ad


ad = "Desirable unfurnished flat in quiet residential area"
print (de_vowel(ad))
# print (is_vowel(c))
