import string

# ─── Load and clean a text file into a list of words ───
def load_essay(filename):
    with open(filename, 'r') as f:
        text = f.read().lower()
    # Remove punctuation
    for char in string.punctuation:
        text = text.replace(char, '')
    words = text.split()
    return words

# ─── Find common words ───
def find_common_words(words1, words2):
    set1 = set(words1)
    set2 = set(words2)
    common = set1 & set2
    print(f"\nCommon words found: {len(common)}")
    for word in common:
        print(f"  '{word}' → Essay1: {words1.count(word)} times | Essay2: {words2.count(word)} times")
    return common

# ─── Search for a word ───
def search_word(words1, words2):
    keyword = input("\nEnter a word to search: ").lower().strip()
    found1 = words1.count(keyword)
    found2 = words2.count(keyword)
    if found1 == 0 or found2 == 0:
        print(f"  Essay1: {found1} times | Essay2: {found2} times")
        print(f"  Result: False — '{keyword}' not found in one or both essays.")
    else:
        print(f"  '{keyword}' → Essay1: {found1} times | Essay2: {found2} times")
        print(f"  Result: True")

# ─── Calculate plagiarism % ───
def calculate_plagiarism(words1, words2):
    set1 = set(words1)
    set2 = set(words2)
    intersection = set1 & set2
    union = set1 | set2
    percentage = (len(intersection) / len(union)) * 100
    print(f"\nPlagiarism Percentage: {percentage:.2f}%")
    if percentage >= 50:
        print("  Decision: PLAGIARISM DETECTED!")
    else:
        print("  Decision: No plagiarism.")

# ─── Main ───
def main():
    print("=" * 50)
    print("  PLAGIARISM DETECTOR")
    print("=" * 50)

    words1 = load_essay('essay1.txt')
    words2 = load_essay('essay2.txt')

    print(f"Essay 1: {len(words1)} words")
    print(f"Essay 2: {len(words2)} words")

    find_common_words(words1, words2)
    search_word(words1, words2)
    calculate_plagiarism(words1, words2)

if __name__ == '__main__':
    main()