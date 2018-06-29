# Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re
user1="zuck26@facebook.com"
user2="page33@google.com"
user3="jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9._]+)@([a-zA-Z]+).([a-z]+)")
def show(user):
    result=p.match(user)
    #print(result)
    print(result[1],end=" ")
    print(result[2],end=" ")
    print(result[3])
show(user1)
show(user2)
show(user3)