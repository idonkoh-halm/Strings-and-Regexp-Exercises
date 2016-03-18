import re
class Name:
    first='Franklin'
    middle='Delano'
    last='Roosevelt'

print("""
Formatting Strings Instructions:
Starting with the variables first, middle and last, define names in:
formal style (last, first)
regular style (first last)
full style (first middle last)
and full w/ middle initial (first middle-initial last) using string formatting.
"""
)

print 'Formal Style: ' '%s %s %s' % (Name.last,',',Name.first)
print 'Regular Style: ' '%s %s' % (Name.first,Name.last)
print 'Full Style: ' '%s %s %s' % (Name.first, Name.middle,Name.last)
print 'Full with Middle Initial: ' '%s %.1s. %s' % (Name.first, Name.middle, Name.last)