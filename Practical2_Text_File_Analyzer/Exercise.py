def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt')
print(content[:100])


def count_lines(content):
    return len(content.split('\n'))

num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")


def count_words(content):
    return len(content.split())

num_words = count_words(content)
print(f"Number of words: {num_words}")


from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")


def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")


def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)


def find_longest_word(content):
    words = content.split()
    longest_word = ""
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word = word
            longest_word_length = len(word)
    return longest_word, longest_word_length


def count_specific_word(content, target_word):
    words = content.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)



def percentage_words(content):
    words = content.split()
    avg_length = average_word_length(content)
    
    longer_than_avg_count = 0
    for word in words:
        if len(word) > avg_length:
            longer_than_avg_count += 1
    
    percentage = (longer_than_avg_count / len(words)) * 100
    return percentage



def analyze_text(filename, specific_word=None):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    num_unique_words = count_unique_words(content)
    avg_length = average_word_length(content)
    longest_word, longest_word_length = find_longest_word(content)
    percentage_avg = percentage_words(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Longest word: '{longest_word}' ({longest_word_length} characters)")
    print(f"Percentage of words longer than average length: {percentage_avg:.2f}%")

    if specific_word:
        specific_word_count = count_specific_word(content, specific_word)
        print(f"Occurrences of '{specific_word}': {specific_word_count}")

analyze_text('sample.txt', specific_word='software')