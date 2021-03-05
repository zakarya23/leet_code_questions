def merge_the_tools(string, k):
    # your code goes here
    all_words = [] 
    sub_words = []
    count = 0 
    for i in range(len(string)): 
        if count < k:
            if string[i] not in sub_words: 
                sub_words.append(string[i])
            count += 1
        else: 
            count = 0
            all_words.append(sub_words)
            sub_words = []
            sub_words.append(string[i])
            count += 1
        
    all_words.append(sub_words)
    for word in all_words: 
        output = ''
        for letter in word: 
            output += letter
        print(output)

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    