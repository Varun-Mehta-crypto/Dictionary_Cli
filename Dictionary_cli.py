import json
import difflib

data = json.load(open("data.json"))
gm = difflib.get_close_matches

def meaning(k):
    try:
        if k in data.keys():
            print("\n".join(data[k]))
        elif k.capitalize() in data.keys():
            print("\n".join(data[k.capitalize()]))
        elif k.upper() in data.keys():
            print("\n".join(data[k.upper()]))
        else:
            raise Exception("Need to check the database")         
    except:
        possible_word = " ".join(gm(k,data.keys(),1))
        if len(possible_word) == 0:
            print("Word does not exists in dictionary databases")
        else:
            w = input(f"Did you mean {possible_word}?[y/n]:").lower()

            if w == "y":
                meaning(possible_word)
            else:
                print("Not found!!")
        


word = input("Enter the word:")
meaning(word.lower())





