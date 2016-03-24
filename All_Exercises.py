import re
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

    print("""
Formatting Strings + Numbers Instructions:
Use the %f options to properly print out the strings as an
integer, with 2 decimal places, or in scientific notation
with 3 significant digits.
"""
)
    print "Third=" '%.2f' %(1.0/3)
    print "Oddball_percentage =" '%.2f%s' %(2.7/14*100,'%')
    print """Big Ol' Number =""" '%e' %(43**23/2.123)
def join():
    print """
    Join Instructions:
    Use the built-in "join" method of a string to elegantly print out the items in a list with commas in between them.
    """
    colors = ['red','white','blue','yellow']
    s=","
    print s.join(colors)
def regexp_find_all():
    pass
def regexp_for_word_games():
    print "Word Games!"
def regexp_for_word_games_2():
    pass
def regexp_for_word_games_3():
    pass
def regexp_test_for_a_phone_number():
    pass

Grading=raw_input("""I want to grade Isaac's code on:
Formatting Strings
Join
Regular Expressions Exercises
""")

if Grading=="Formatting Strings":
    formatting_strings()
if Grading=="Join":
    join()
if Grading=="Regexp Exercises":
    RegExpGrading=raw_input("""     I want to grade Isaac's Regular Expressions code:
            Find All
            Test for a Phone Number
            Word Games
            Word Games 2
            Word Games 3
    """)
if RegExpGrading=="Word Games":
    regexp_for_word_games()
if RegExpGrading=="Find All":
    regexp_find_all()
if RegExpGrading=="Word Games 2":
    regexp_for_word_games_2()
if RegExpGrading=="Word Games 3":
    regexp_for_word_games_3()
if RegExpGrading=="Test for a Phone Number":
    regexp_test_for_a_phone_number()
else:
    pass
