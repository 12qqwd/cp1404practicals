def main():
    text = input("Text: ").strip().lower()
    words = text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.keys())
    max_word_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_counts[word]}")


if __name__ == "__main__":
    main()

