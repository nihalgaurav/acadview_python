# Split the following irregular sentence into words
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"

import re
sentence="A,very very;irregular_sentence"

#method 1
# p=re.compile(r"([a-zA-Z]+),([a-zA-Z]+) ([a-zA-Z]+); ([a-zA-Z]+)_([a-zA-Z]+)")
# result=p.match(sentence)
# print(result[1],end=" ")
# print(result[2],end=" ")
# print(result[3],end=" ")
# print(result[4],end=" ")
# print(result[5])


#method 2
p = re.compile(r"[^A-Za-z0-9]")
print(p.sub(" ",sentence))