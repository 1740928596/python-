def find_unlearned_words(learned_words, article):
    learned_set = set(learned_words)
    article_words = article.split()
    unlearned_words = []
    seen_words = set()
    
    for word in article_words:
        if word == '#':
            break
        if word not in learned_set and word not in seen_words:
            unlearned_words.append(word)
            seen_words.add(word)
    
    return unlearned_words

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    learned_words = data[1:n+1]
    article = data[n+1]
    
    unlearned_words = find_unlearned_words(learned_words, article)
    
    for word in unlearned_words:
        print(word)

if __name__ == "__main__":
    main()
