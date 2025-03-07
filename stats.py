def word_count(text):
    return len(text.split())

def frequency_characters(text):
    # get the frequency of each character in the text
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