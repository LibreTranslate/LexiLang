import os
import pickle
from .languages import get_supported_languages, tokenize

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def compile_data():
    print("Compiling database...")
    words = {}
    langs = get_supported_languages()
    for name in langs:
        code = langs[name]

        with open(os.path.join(root_dir, "dictionaries", f"{name}.txt"), "r", encoding="utf-8") as f:
            lines = [l.strip().lower() for l in f.read().split("\n")]
            for l in lines:
                tokens = tokenize(code, l.strip())
                for tok in tokens:
                    if not tok in words:
                        words[tok] = [code]
                    elif not code in words[tok]:
                        words[tok].append(code)

    print("Serializing...")

    outfile = os.path.join(root_dir, "lexilang", "data", "words.pickle")
    with open(outfile, "wb") as f:
        pickle.dump(words, f, protocol=4)
    print(outfile)
