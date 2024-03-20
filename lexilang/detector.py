import pickle
import os
from .languages import get_language_weight, is_cjk

_words = None
_translate_table = str.maketrans(dict.fromkeys("!\"#$%&()*+,/:;<=>?@[\\]^_`{|}~.", " "))  # not included ' -

def detect(text, languages=[]):
    global _words

    if _words is None:
        # Initialize
        words_file = os.path.join(os.path.dirname(__file__), "data", "words.pickle")

        if not os.path.isfile(words_file):
            from .utils import compile_data
            compile_data()

        with open(words_file, "rb") as f:
            _words = pickle.load(f, encoding="utf-8")

    text = text.lower().strip()
    text = text.translate(_translate_table)
    if is_cjk(text):
        tokens = list(text)
    else:
        tokens = text.split(" ")

    lang_bins = {}
    for tok in tokens:
        if tok in _words:
            for lang in _words[tok]:
                if (not languages) or (lang in languages):
                    if not lang in lang_bins:
                        lang_bins[lang] = 1
                    else:
                        lang_bins[lang] += 1

    if len(lang_bins) == 0:
        return "en", 0

    max_value = max(lang_bins.values())
    candidates = [l for l in lang_bins if lang_bins[l] == max_value]

    if len(candidates) == 1:
        return candidates[0], 0.9
    else:
        best_lang = candidates[0]
        best_weight = get_language_weight(best_lang)
        for lang in candidates[1:]:
            weight = get_language_weight(lang)
            if weight > best_weight:
                best_lang = lang
                best_weight = weight

        return best_lang, (1 / len(candidates)) * 0.9
