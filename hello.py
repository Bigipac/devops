def count_lines_words_chars(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
            return num_lines, num_words, num_chars
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


def main():
    filename = input("Enter the filename: ")
    result = count_lines_words_chars(filename)
    if result:
        num_lines, num_words, num_chars = result
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")


if __name__ == "__main__":
    main()
