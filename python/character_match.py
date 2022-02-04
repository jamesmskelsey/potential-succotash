def is_character_match(string1, string2):
	return mangle(string1) == mangle(string2)

def mangle(str):
    return ''.join(sorted(list(str.lower()))).strip()