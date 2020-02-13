from datetime import date
import os
import re
from extract import get_docx_text


def count_words(filename):
    s = get_docx_text(filename)
    word_count = 0
    for line in s:
        line = line.split()
        word_count += len(line)
    return word_count


def natural_sort(l):
    """
    Sorts a list like a windows file manager.
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def get_docx_files(path=None):
    """
    Gets every docx in the current path.
    """
    if not path:
        dir_path = os.path.dirname(os.path.realpath(__file__))
    else:
        dir_path = path

    res = []

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            res.append(os.path.join(root, file))

    return res


def update_progress(new_total):
    """
    Updates change in word count day to day.
    """
    today = date.today()
    lines = []
    with open('@progress.txt', 'r') as file:
        current = int(file.readline())
        for line in file:
            lines.append(line)

    last_date = lines[-1].split(':')[0]
    last_count = int(lines[-1].split(':')[1])

    with open('@progress.txt', 'w') as file:
        diff = new_total - current
        file.write(str(new_total) + '\n')
        for i in range(0, len(lines) - 1):
            file.write(lines[i])

        if str(last_date) != str(today):
            file.write(lines[-1])
            file.write(str(today) + ": " + str(diff) + '\n')
        else:
            file.write(str(today) + ": " + str(last_count + diff) + '\n')


def count():
    """
    Prints out individual word count of every docx file.
    :return: Total word count of all docx files.
    """
    files = get_docx_files()
    files = natural_sort(files)
    total = 0
    for file in files:
        extension = file.split(".")[-1]
        if extension == "docx" and file[0] != "@":
            num_words = count_words(file)
            if num_words is not None:
                total += num_words
                print(file + ": " + str(num_words))
    if total != 0:
        print("-----------------------")
        print("Total: " + str(total))

    return total


if __name__ == "__main__":
    total = count()
    update_progress(total)
    input()  # Keep terminal open until keypress is issued
    # pyinstaller main.py --onefile
