import re
import csv

with open("tid5.csv", "r") as f:
    content = f.readlines()
f.close()
print(1)
for i,line in enumerate(content):
    if re.search(r'eval',line):
        
        content.pop(i)
print(2)
#print(content)

with open("fid5.csv", "w", newline="") as csvfile:
    csvfile.write("".join(content))
   