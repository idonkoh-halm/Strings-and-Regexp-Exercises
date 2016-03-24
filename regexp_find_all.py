import re
s = '<html><body><h1>This is an HTML string</h1><!-- this thing is not a tag —><p name="foo">This is a tag</p><ul><li>One</li><li>Two</li><li>Three</li></body></html>'
re.
# Returns => ['html','body','h1','p','ul','li','li','li']
