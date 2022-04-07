import argparse

from .core import main

def arg():
    parser = argparse.ArgumentParser(description='srtTranslator.py')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-l', '--lang', help='Language like es,en', default='es', required=False)
    args = parser.parse_args()
    return args


def cli():
    args = arg()
    main(args.input, args.lang)