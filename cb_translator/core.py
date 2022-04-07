import time
from pysrt import SubRipFile, SubRipItem
import os
import sys

from .services.azure import azure_translator


def main(path, lang):
    subs = SubRipFile.open(path)
    for sentence in subs:
        original = sentence.text
        sentence.text = azure_translator(sentence.text.replace('\n', ' '), lang=lang)
        print(f'{original} ===> {sentence.text}')
    subs.save(f'{lang}.{os.path.basename(path)}', 'utf-8')


if __name__ == '__main__':
    main()
