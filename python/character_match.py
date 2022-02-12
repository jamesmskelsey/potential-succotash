"""
Is character match should return true if the same number of characters 
exist in each string, regardless of case. i.e. 'add' and 'DAD' are 
matches.
"""
def is_character_match(string1, string2):
	return mangle(string1) == mangle(string2)

def mangle(str):
    return ''.join(sorted(list(str.lower()))).strip()