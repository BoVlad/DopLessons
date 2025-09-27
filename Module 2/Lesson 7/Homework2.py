words = ["apple", "banana", "kiwi", "grapefruit", "orange"]

def lenging(word):
    return len(word) < 6

new_list = list(filter(lenging, words))
print(new_list)