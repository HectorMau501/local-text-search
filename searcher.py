from indexer import tokenize

def search(index: dict[str, dict[str, int]], word: str) -> list[tuple[str, int]]:
    word = ''.join(tokenize(word.lower()))
    index_word = index.get(word, {}) #Avoid the KeyError if the word is not in the index
    index_items = list(index_word.items()) #Convert the dictionary items to a list of tuples
    return index_items


def bubble_sort_by_count(results: list[tuple[str, int]]) -> list[tuple[str, int]]:
    n = len(results)
    for i in range(n):
        for j in range(0, n-i-1):
            if results[j][1] < results[j+1][1]:
                results[j], results[j+1] = results[j+1], results[j]
    return results