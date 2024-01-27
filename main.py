def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words, "words found in the document")
    dict_letters = get_num_letters(text)
    print_sorted_list(dict_letters)

def get_num_words(string):
    words = string.split()
    return len(words)

def get_num_letters(string):
    list = {}
    new_string = string.lower()
    for i in new_string:
        list[i] = list.get(i, 0) + 1
    return list

def get_alpha_list(input):
    new_list = list(input.items())
    isalpha_list = []
    for i in new_list:
        if i[0].isalpha() == True:
            isalpha_list.append(i)
    return isalpha_list

def print_sorted_list(input):
    alpha_list = get_alpha_list(input)
    sorted_list = []
    list_num = 0

    for n in range(0,len(alpha_list)):
        max_so_far = 0

        for i in range(0,len(alpha_list)):
            if alpha_list[i][1] > max_so_far:
                max_so_far = alpha_list[i][1]
                list_num = i
        sorted_list.append(alpha_list.pop(list_num))

    for n in range(0, len(sorted_list)):
        print(f"The '{sorted_list[n][0]}' character was found {sorted_list[n][1]} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()