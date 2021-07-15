import sys
sys.path.append('/mymodule/')
from functools import reduce

from mathy import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Enter some text")
    for word in text.split():

        if word.upper() in operations.keys():

            try:
                l=extract_numbers_from_text(text)

                r=operations[word.upper()]
                k=reduce(r,l)
                print(k)

            except:
                print("something went wrong please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break

        elif word.isnumeric():
            continue
        else:
            sorry()