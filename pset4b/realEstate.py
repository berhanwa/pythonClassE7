def de_vowel(ad):
    vowelless_ad = 0
    for i in range (1, len(ad)):
        # if vowel = is_vowel(ad[i])
        # if is_vowel(c) and is_vowel(ad[i]):
        if is_vowel(ad[i]) and ad[i-1]!=' ':
            # ad += vowelless_ad
            ad = ad[:i] + ad [i+1:]
            ad += vowelless_ad
    return vowelless_ad


def is_vowel(c):
    if c in 'aeiouAEIOU':
        return True
    else:
        return False

# c = "aeiouAEIOU"
ad = "Desirable unfurnished flat in quiet residential area"
print (de_vowel(ad))
