import os
from glob import glob

file_name = glob(os.path.join('*.txt'))

text = {}
for element in file_name:    
    with open(element, encoding="utf-8") as file:
        content = file.readlines()                   
        text[element] = [len(content)] + content

text_sorted = {k: text[k] for k in sorted(text, key = text.get)}

with open('4.txt', 'w') as file:
    for k, v in text_sorted.items():
        print(k, file=file)
        for s in v:
            print(s, file=file)


            