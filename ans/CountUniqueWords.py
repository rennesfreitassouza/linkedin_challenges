import re
#import Counter

def count_words(path): # for comparative purposes
    
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print('\nTotal Words:', len(all_words))
        
        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1
        
        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '\t', word[1])

def word_counter_aux(wordsDict):
    md = {}
    wordsDict_list = []
    [wordsDict_list.append(k) for k in wordsDict.keys()]

    biggest_value = max(wordsDict[key] for key in wordsDict_list)
    while(len(md) < 20):
        i = 0
        for k in list(wordsDict_list):
            if (wordsDict[k] == biggest_value):
                md[k] = biggest_value
                wordsDict_list.pop(i)
                biggest_value = max(wordsDict[key] for key in wordsDict_list)
                break
            i += 1
    return md

def word_counter(pathToTextFile): # my solution
    with open(pathToTextFile, "r", encoding='utf-8') as fp:
        full_str = fp.read()
        word_list = re.findall(r"[-0-9a-zA-Z']+", full_str)
        
        wordsDict = dict()
        for w in word_list:
            wl = w.lower()
            if wl in wordsDict.keys():
                wordsDict[wl] += 1
            else: wordsDict[wl] = 1
        
        print(f"Total word count: {len(word_list)}\n\n")

        most_common = wordsDict 
        if (len(wordsDict) > 20):
            most_common = word_counter_aux(wordsDict)
            
    return most_common

def main(pathToTextFile = 'shakespeare.txt'):
    
    top20 = word_counter(pathToTextFile)
    print(f'Top 20 words:\n')
    for k, v in top20.items():
        print(f'{k} {v}')

if __name__ == '__main__': main()
