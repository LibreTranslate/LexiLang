def get_supported_languages():
    return {
        'afrikaans': 'af', 
        'albanian': 'sq', 
        'arabic': 'ar', 
        'bengali': 'bn', 
        'bulgarian': 'bg', 
        'catalan': 'ca', 
        'chinese': 'zh', 
        'czech': 'cs', 
        'danish': 'da', 
        'dutch': 'nl', 
        'english': 'en', 
        'esperanto': 'eo', 
        'estonian': 'et', 
        'finnish': 'fi', 
        'french': 'fr', 
        'german': 'de', 
        'greek': 'el', 
        'hebrew': 'he', 
        'hindi': 'hi', 
        'hungarian': 'hu', 
        'indonesian': 'id', 
        'italian': 'it', 
        'japanese': 'ja', 
        'kazakh': 'kk', 
        'korean': 'ko', 
        'latvian': 'lv', 
        'lithuanian': 'lt', 
        'macedonian': 'mk', 
        'norwegian': 'nb', 
        'polish': 'pl', 
        'portuguese': 'pt', 
        'romanian': 'ro', 
        'russian': 'ru', 
        'serbian': 'sr', 
        'slovak': 'sk', 
        'slovenian': 'sl', 
        'spanish': 'es', 
        'swedish': 'sv', 
        'thai': 'th', 
        'turkish': 'tr', 
        'ukrainian': 'uk', 
        'vietnamese': 'vi', 
        'farsi': 'fa'
    }

# https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers
_weights = {
    'en': 1.456,
    'zh': 1.138,
    'hi': 0.609,
    'es': 0.559,
    'fr': 0.310,
    'ar': 0.274,
    'bn': 0.273,
    'pt': 0.264,
    'ru': 0.255,
    'ur': 0.232,
    'id': 0.199,
    'de': 0.133,
    'ja': 0.123,
    'tr': 0.09,
    'vi': 0.086,
    'it': 0.068,
    'th': 0.061,
    'ca': 0.0081,
}

def get_language_weight(code):
    return _weights.get(code, 0.001)

def tokenize(code, text):
    if code in ['zh', 'ko', 'ja']:
        return list(text)
    else:
        return text.split(" ")

def is_cjk(text):
    c = 0
    for ch in text[:5]:
        if any([start <= ord(ch) <= end for start, end in 
                [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215), 
                 (63744, 64255), (65072, 65103), (65381, 65500), 
                 (131072, 196607)]
                ]):
            c += 1
    return c > 1 and text.count(" ") < 3