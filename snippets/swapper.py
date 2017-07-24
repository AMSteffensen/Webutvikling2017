def _compile_sentence(sentence):
    d = dict()
    s = set()

    for letter in sentence:
        if letter in s:
            continue

        s.add(letter)
        count = sentence.count(letter)
        if count == 1:
            d[letter] = [sentence.index(letter)]
        else:
            indexes = []
            prev_index = 0
            for occ in range(0, sentence.count(letter)):
                this_index = sentence.index(letter, prev_index)
                indexes.append(this_index)
                prev_index = this_index + 1
            d[letter] = indexes
    return d


def _compile_transtable(lettersA, lettersB):
    if len(lettersA) != len(lettersB):
        raise Exception("Not equal length")

    d = dict()
    for index in range(0, len(lettersA)):
        d[lettersA[index]] = lettersB[index]
    return d


def swap(sentence, lettersA, lettersB):
    sent_table = _compile_sentence(sentence)
    trans_table = _compile_transtable(lettersA, lettersB)

    sent_list = list("#" * len(sentence))

    for key, value in sent_table.items():
        if key not in trans_table:
            new_letter = key
        else:
            new_letter = trans_table[key]
        for pos in value:
            sent_list[pos] = new_letter

    return ''.join(sent_list)