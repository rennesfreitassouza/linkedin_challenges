
import queue

# https://www.linkedin.com/learning/python-code-challenges/sort-a-string?autoAdvance=true&autoSkip=false&autoplay=true&resume=false
def sort_words_w_queue(string_of_words):
    """"""
    list_of_words = string_of_words.split(' ')
    
    list_of_low_words = [word.lower() + word for word in list_of_words]

    list_of_low_words.sort()

    q = queue.Queue()

    for l_word in list(list_of_low_words):
        for original_word in list_of_words:
            if (original_word == l_word[len(l_word) // 2 :]):
                q.put(original_word)
                list_of_words.remove(original_word)
                break
        list_of_low_words.remove(l_word)
    
    str_sorted = ''
    while not q.empty():
        str_sorted += q.get()
        if not q.empty():
            str_sorted += ' '

    return str_sorted

def sort_words_linkedin(words_param):
    words = words_param.split(' ')
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

def main():
    string_of_words = input("Type a phrase: ")
    resultado = sort_words_w_queue(string_of_words)
    print (resultado)
if __name__ == '__main__': main()
