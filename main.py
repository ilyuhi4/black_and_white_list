"""
Имеется список "плохих" и "хороших" слов.
Необходимо проверить качество текста - "хорошие" слова должны быть обязательно, "плохих" не должно быть
"""

# список слов, которые обязательно должны быть в проверяемом тексте
white_set = {'god', 'blue'}

# список слов, которых не должно быть в проверяемом тексте
black_set = {'pig', 'meat', 'kill'}

# входной текст
input_text = ' With this pig we will live together. With God we trust in blue skies.'


def make_list_clean_and_separate(text: str) -> set:
    """Очищаем данные, переводим в нижний регистр, создаём множество (нам не нужно количество повторов)"""
    word_set = set(text.lower().strip(",.!&:?").split())
    return word_set


def main(text, white_words: set, black_words: set) -> str:
    word_set = make_list_clean_and_separate(text)
    # возвращаем положительную рецензию если
    return ("Отличный текст"
            # если хорошие слова являются подмножеством текста
            if white_words.issubset(word_set)
            # и плохие слова не пересекаются с текстом
               and black_words.isdisjoint(word_set)
            # иначе отрицательная рекомендация
            else "Текст не годится")


if __name__ == '__main__':
    print(main(input_text, white_set, black_set))
