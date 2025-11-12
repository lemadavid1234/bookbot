# file that contains functions for analyzing text
def get_num_words(fileContent):
    count = fileContent.split()
    return len(count)

def get_num_char(fileContent):
    dict = {}
    for letter in fileContent:
        if(letter.lower() not in dict):
            dict[letter.lower()] = 1
        else: 
            dict[letter.lower()] += 1

    return dict



def get_sorted_list(dict):
    def sort_on(items):
        return items["num"]

    letters = []
    for ch, count in dict.items():
        if ch.isalpha():
            letters.append({"char": ch, "num": count})


    letters.sort(reverse=True, key=sort_on)
    return letters


 
