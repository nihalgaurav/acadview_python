#  Clean up the following tweet so that it contains only the user’s message. That is,
#  remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to
#  code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

import re
tweet='''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

p=re.compile(r"(.+) RT (.+): (.+) http(.+)")
result=p.findall(tweet)
print(result[0][0],result[0][2])