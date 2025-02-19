def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        text = f.read()
        count = word_count(text)
        frequency = frequency_characters(text)
        alpha = only_alpha_frequency(frequency)
        sorted_letters = sorted_alpha_frequency(alpha)
        print_report(file, count, sorted_letters)

def word_count(text):
    return len(text.split())

def frequency_characters(text):
    #get the frequency of each character in the text
    frequency = {}
    for character in text:
        character = character.lower()
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency

def only_alpha_frequency(frequency):
    alpha = {}
    for character, count in frequency.items():
        if character.isalpha():
            alpha[character] = count
    return alpha
def sorted_alpha_frequency(frequency):
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

def print_report(file, word_count, sorted_letters):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} Words found in the doucment\n")
    for letter, count in sorted_letters:
        print(f"The \'{letter}\' character was found {count} times")
    print(f"--- End Report ---")

main()
