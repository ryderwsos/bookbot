
def print_book():
    print(file)

def word_count(file):
    words =file.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def print_character_count(file):
    dct = {}
    lower_file = file.lower()
    for i in lower_file:
        if(i in dct):
            dct[i] += 1
        else:
            dct[i] = 1

    lst = []
    for n in dct:
        if(n.isalpha()):
            lst.append({"char" : n, "num" : dct[n]})
    lst.sort(reverse=True, key=sort_on)
    print(lst)

    print("--- Printing book report ---")
    print(f"book has {word_count(file)} words")

    for i in lst:
        print(f"Character {i["char"]} appears {i["num"]} times in the book")
    
    print("--- Ending book report ---")


def main():
    file_contents = None
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print_character_count(file_contents)

main()