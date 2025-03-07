import sys
from stats import word_count, frequency_characters, only_alpha_frequency, sorted_alpha_frequency

def main():

    # I want to be able to run the program from the command line
    # I want to be able to pass in a file as an argument
    # I want to be able to read the contents of the file
    if len(sys.argv) != 2:
        print("Usage: python main.py <file>")
        sys.exit(1)

    file = sys.argv[1]
    with open(file) as f:
        text = f.read()
        count = word_count(text)
        frequency = frequency_characters(text)
        alpha = only_alpha_frequency(frequency)
        sorted_letters = sorted_alpha_frequency(alpha)
        print_report(file, count, sorted_letters)

def print_report(file, word_count, sorted_letters):
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words\n")
    print(f"--------- Character Count -------")
    for letter, count in sorted_letters:
       # print(f"The \'{letter}\' character was found {count} times")
        print(f"{letter}: {count}")
    print(f"============= END ===============")

main()
