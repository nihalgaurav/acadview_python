# Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = "Betty bought a bit of butter, But the butter was so bitter, " \
#        "So she bought some better butter, To make the bitter butter better."
import re
text="""Betty bought a bit of butter, But the butter was so bitter,
        So she bought some better butter, To make the bitter butter better."""

#method 1
# q=re.compile(r"^[bB]+")
# result2=[]
# text1=text.split(" ")
# for i in text1:
#     if ['b']==q.findall(i) or ['B']==q.findall(i):
#         result2.append(i)
# print("words starting with 'b' or 'b' :")
# print(result2)


#method 2
p = re.compile(r'\b[bB]\w+')
print(p.findall(text))