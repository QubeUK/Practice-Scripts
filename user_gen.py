from wonderwords import RandomWord


def user_gen() -> str:
    first = RandomWord()
    second = RandomWord()
    first.word(word_min_length=6, word_max_length=8)
    second.word(word_min_length=6, word_max_length=8)
    username = first.word() + "." + second.word()

    return username


print(user_gen())
