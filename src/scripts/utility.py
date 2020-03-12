from typing import List, Tuple
import os


def pair_wise(path1: str, path2: str) -> List[Tuple[str, str]]:
    """
    Takes in paths to the two language pair wise files and returns list of paired translations
    :param path1: path to file
    :param path2: path to file
    :return: [("sentence in language 1", "sentence in language 2"), ... ]
    """

    # handle paths not found
    if not os.path.exists(path1) or not os.path.exists(path2):
        result = "Path not found at: "
        if not os.path.exists(path1):
            result += path1 + "; "
        if not os.path.exists(path2):
            result += path2 + "; "
        raise ValueError(result)

    file1 = ''
    file2 = ''
    with open(path1, 'r') as f1:
        file1 = f1.read()
    with open(path2, 'r') as f2:
        file2 = f2.read()

    file1 = file1.split('\n')
    file2 = file2.split('\n')

    paired_sentences = [(file1[i], file2[i]) for i in range(len(file1))]

    return paired_sentences


