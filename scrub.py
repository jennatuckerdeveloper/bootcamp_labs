"""
Jenna M Tucker

PEP 257

"""
#module level doc string

#this is called a doctest, we can run it as code


import re
#regular expressions module

def scrub_numbers(raw_data: str) -> str: #PEP 404 Typing notation
    """
    This function takes a string and removes all the numbers.
    Then returns the cleaned string.
    """
#function definition line
    cleaned = re.sub(r'\d', '', raw_data)
    #sub() is a method in the re module that substitutes
    return cleaned


print(scrub_numbers("Be9autiful9 i4s be2tter th4an ug42ly"))

""">>> gentle_clean('Explicit_is-better_than -implicit')
'Explicit is better than implicit.'"""

def gentle_clean(raw_data: str) ->str:
    """
    This function takes a string and removes the dashes and underscores.
    If there's no whitespace, it inserts a whitespace.
    If there is a whitespace, it leave it alone.
    """
#function definition line
    cleaned = re.sub(r' {2}', ' ', (re.sub(r'[_-]', ' ', raw_data)))
    #sub() is a method in the re module that substitutes
    return cleaned

print(gentle_clean('Explicit_is-better_than -implicit'))


""">>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex.'"""

def clean_data(raw_data: str) ->str:
    """
    This function removes numbers, then replaces _ and - with a space.
    Then it takes beginning and ending spaces and makes them gone.
    """
#function definition line
    cleaned = re.sub(r'\d| {2,}', '',  (re.sub(r'[_-]', ' ', raw_data)))
    #sub() is a method in the re module that substitutes
    #(re.sub(r' {2,}', ' ', --> I couldn't add this again to the method.
    return cleaned

print(clean_data('  42Simple-is_better_than-compl9ex   '))

""">>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently.'"""

#>>> extracto('1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.')

def extracto(raw_data: str) ->str:
    total = re.findall('\d', raw_data)
    answer = sum(int(i) for i in total)
    cleaned = re.sub('\d', '', raw_data)
    return cleaned, answer

print(extracto("1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules."))
print(extracto("2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules."))
print(extracto("3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules."))

def strong_cleaner(raw_data: str) ->str:
#This function deletes odd characters and a capital letter in the middle of a word.
    cleaned = re.sub(r'[!@#$%^&*()1I]', '', raw_data)
    return cleaned

print(strong_cleaner("Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly"))


def some_scrubber(raw_data: str) ->str:
    cleaned =  re.sub(r' {2}', ' ', (re.sub(r'(?<!\s)(\s)', '', raw_data)))
    return cleaned

print(some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . '))


""">>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '"""

def mr_clean(raw_data: str) ->str:
#Function that inserts a space after every character
    cleaned = re.sub('(?<=.)', ' ', raw_data)
    return cleaned
print(mr_clean('Sparse is better than dense'))

""">>> ms_clean('Readability counts')
'R9y c4s'"""

def ms_clean(raw_data: str) ->str:
    words = raw_data.split( )
    answer = ""
    for item in words:
        first = item[0]
        last = item[-1]
        middle = item[1:len(raw_data)]
        numb = len(middle)-1
        cleaned = first + str(numb) + last
        answer += (cleaned + " ")
    return answer
#answer = [], answer.append(cleaned)
#return " ".join(answer)"
print(ms_clean('Readability counts'))

"""This function replaces the characters between the beginning and end
    of a word with a number representing the number of characters removed
    So start after the first and before the last characterself.
    get the length of that string
    replace that string with the result of len

"""
