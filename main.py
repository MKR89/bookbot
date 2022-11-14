def count_words(string):
    return len(string.split())

def count_characters(string):
    lc_string = string.lower()
    return {c:lc_string.count(c) for c in set(lc_string)}

def word_report(words_count, dict, path):
    keys_list = list(dict.keys())
    keys_list = [i for i in keys_list if i.isalpha()]
    keys_list.sort()
    
    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document")
    for key in keys_list:
        print(f"The {key} character was found {dict[key]} times")
    print("--- End report ---")

def main():    
    path = "/home/mr89/workspace/github.com/MKR89/bookbot/books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        # print(count_characters(file_contents))
        word_report(count_words(file_contents), count_characters(file_contents), path)
        
if __name__ == "__main__":
    main()