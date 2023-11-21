def de_vowel(ad):
    vowelless_ad = ' '
    for i in range (1, len(ad)):
        # if vowel = is_vowel(ad[i])
        # if is_vowel(c) and is_vowel(ad[i]):
        if is_vowel(ad[i]) and ad[i-1]!=' ':
            # ad += vowelless_ad
            vowelless_ad = vowelless_ad[:i] + vowelless_ad[i+1:]
    return vowelless_ad

def is_vowel(c):
    # c = ' '
    if c in 'aeiouAEIOU':
        return True
    else:
        return False

ad = "Desirable unfurnished flat in quiet residential area"
print (de_vowel(ad))
# print (is_vowel(c))
