def is_vowel(c):
    # c = ' '
    if c in 'aeiouAEIOU':
        return True
    else:
        return False

def de_vowel(ad):
    vowelless_ad = ''
    for i in range (0, len(ad)):
        # if vowel = is_vowel(ad[i])
        # if is_vowel(c) and is_vowel(ad[i]):
        # if is_vowel(ad[i]) and ad[i-1]!=' ':
        if not(is_vowel(ad[i]) and i != 0 and ad[i-1]!=' '):
            # ad += vowelless_ad
            # vowelless_ad = vowelless_ad[:i] + vowelless_ad[i+1:]
            vowelless_ad += ad[i]
    return vowelless_ad


ad = "Desirable unfurnished flat in quiet residential area"
print (de_vowel(ad))
# print (is_vowel(c))
