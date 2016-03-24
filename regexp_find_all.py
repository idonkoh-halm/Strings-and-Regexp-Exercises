import re
s = '<html><body><h1>This is an HTML string</h1><!-- this thing is not a tag —><p name="foo">This is a tag</p><ul><li>One</li><li>Two</li><li>Three</li></body></html>'
re.match('Th'[a-z][snt],'This'] #should return a match object
re.search('Th'[a-z][tsm],'That')
#re.findall prints the string matches of your expression
# Returns => ['html','body','h1','p','ul','li','li','li']


#* means match it by one item as many times as you'd like.

#* means 0 or no times

#means 1 or more times
#? denotes asking at once or no times

#MEEJAY NOTES
#Open document in directory, save it as a variable (infile), denote read status 'rb'
#readaslist
#split erases  the selected argument from the list
#for n in nlist:
#  if re.match('1[0-9-]*',
