class FString_Name:
    first='Franklin'
    middle='Delano'
    last='Roosevelt'



def formatting_strings():
    print("""
Formatting Strings Instructions:
Starting with the variables first, middle and last, define names in:
Formal style (last, first)
Regular style (first last)
Full style (first middle last)
and full w/ middle initial (first middle-initial last) using string formatting.
"""
)
    print "Formal Style: " '%s, %s' % (FString_Name.last,FString_Name.first)
    print "Regular Style: " '%s %s' % (FString_Name.first,FString_Name.last)
    print "Full Style: " '%s %s %s' % (FString_Name.first, FString_Name.middle,FString_Name.last)
    print "Full with Middle Initial: " '%s %.1s. %s' % (FString_Name.first, FString_Name.middle, FString_Name.last)

def join():
    pass
def regexp_find_all():
    pass
def regexp_for_word_games():
    pass
def regexp_for_word_games_2():
    pass
def regexp_for_word_games_3():
    pass
def regexp_test_for_a_phone_number():
    pass

Grading=raw_input("""I want to grade Isaac's code on:
Formatting Strings
Join
Regexp: Find All
Regexp: Word Games
Regexp: Word Games 2
Regexp: Word Games 3
Regexp: Test for a Phone Number

""")

if Grading=="Formatting Strings":
    formatting_strings()
else:
    print "Uh-Oh! An error! Please check your capitalization. If that is not the case, you may use the separate files."

