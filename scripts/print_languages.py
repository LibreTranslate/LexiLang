import sys
import os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from lexilang.languages import get_supported_languages

for lang in get_supported_languages():
    lang = lang[0].upper() + lang[1:]
    print(f" * {lang}")