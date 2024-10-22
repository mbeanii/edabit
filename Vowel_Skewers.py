VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']

def begins_and_end_with_consonant(s):
    return  (
                s[0].upper() not in VOWELS and
                s[-1].upper() not in VOWELS
            )
    
def alternates_between_consonants_and_vowels(s):
    stripped = s.strip('-')
    previous_was_vowel = 'Uninitialized'
    for char in stripped:
        is_vowel = char.upper() in VOWELS
        if is_vowel == previous_was_vowel:
            return False
        previous_was_vowel = is_vowel
    return True
    
def has_even_spacing(s):
    expected = 0
    expected_set = False
    for char in s[1:]:
      if not expected_set:
        if char == '-':
            expected += 1
        else:
            counter = expected # So the first one passes below
            expected_set = True
        continue
        
        if char == '-':
            counter += 1
        else:
            if counter != expected:
                return False
            counter = 0
    return True

def is_authentic_skewer(s):
    return  (
                begins_and_end_with_consonant(s) and
                alternates_between_consonants_and_vowels(s) and
                has_even_spacing(s)
            )