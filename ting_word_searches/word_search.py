import re


def getting_target_word(content, index, line):
    if content:
        return {
            'linha': index + 1,
            'conteudo': line
        }
    else:
        return {'linha': index + 1}


def getting_match_word(word, instance, content):
    result = []
    insensitive_case_word = word.lower()
    for file in instance._data:
        lines = []
        for index, line in enumerate(file['linhas_do_arquivo']):
            line_insensitive_case = line.lower()
            if re.search(insensitive_case_word, line_insensitive_case):
                main_content = getting_target_word(content, index, line)
                lines.append(main_content)
        if len(lines) > 0:
            result.append(
                {
                    'palavra': word,
                    'arquivo': file['nome_do_arquivo'],
                    'ocorrencias': lines
                }
            )
    return result


def exists_word(word, instance):
    result = getting_match_word(word, instance, content=False)
    return result


def search_by_word(word, instance):
    result = getting_match_word(word, instance, content=True)
    return result
