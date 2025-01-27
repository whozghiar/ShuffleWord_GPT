import random
import re

def shuffle_word(word):
    """Mélange les lettres internes d'un mot (sans toucher à la première, la dernière lettre, et les caractères de ponctuation internes)."""
    if len(word) <= 3:
        return word  # Pas besoin de mélanger

    # Identifier les lettres et caractères spéciaux
    letters = [char for char in word if char.isalpha()]

    # Conserver la première et la dernière lettre
    first, last = letters[0], letters[-1]
    middle_letters = letters[1:-1]

    # Mélanger les lettres internes jusqu'à obtenir un résultat différent
    while True:
        shuffled_middle = middle_letters[:]
        random.shuffle(shuffled_middle)
        if shuffled_middle != middle_letters:
            break

    # Reconstruire le mot avec les caractères spéciaux à leur place
    shuffled_word = ''
    letter_index = 0
    for char in word:
        if char.isalpha():
            if letter_index == 0:
                shuffled_word += first
            elif letter_index == len(letters) - 1:
                shuffled_word += last
            else:
                shuffled_word += shuffled_middle[letter_index - 1]
            letter_index += 1
        else:
            shuffled_word += char

    return shuffled_word

def shuffle_text(text):
    """Mélange les lettres internes de tous les mots d'un texte en respectant les règles."""
    words = re.split(r'(\W+)', text)  # Conserver les espaces et la ponctuation
    shuffled_words = [shuffle_word(word) for word in words]
    return ''.join(shuffled_words)