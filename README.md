# LexiLang

Simple, fast dictionary-based language detector for short texts.

## Installation

```bash
pip install lexilang
```

## Usage

```python
from lexilang.detector import detect

print(detect("bonjour")) # ('fr', 0.45)
print(detect("学中文")) # ('zh', 0.45)
print(detect("ciao mondo")) # ('it', 0.9)
print(detect("El gato doméstico")) # ('es', 0.45)

# Optionally, specify a subset of languages to consider
print(detect("ciao", languages=["de", "ro"])) # ('de', 0.45)
```

`detect(text, languages=[])` -> tuple (`iso_639_1`, `confidence`)

## Supported Languages

 * Afrikaans
 * Albanian
 * Arabic
 * Bengali
 * Bulgarian
 * Catalan
 * Chinese
 * Czech
 * Danish
 * Dutch
 * English
 * Esperanto
 * Estonian
 * Finnish
 * French
 * German
 * Greek
 * Hebrew
 * Hindi
 * Hungarian
 * Indonesian
 * Italian
 * Japanese
 * Kazakh
 * Korean
 * Latvian
 * Lithuanian
 * Macedonian
 * Norwegian
 * Polish
 * Portuguese
 * Romanian
 * Russian
 * Serbian
 * Slovak
 * Slovenian
 * Spanish
 * Swedish
 * Thai
 * Turkish
 * Ukrainian
 * Vietnamese
 * Farsi

## Limitations

This detector was designed for handling small texts (< 20 characters). It will probably not work reliably for longer text sequences. As it relies on dictionaries, if a word is missing or mispelled, the detection will fail.

## Contributing

If you want to add a new language, or improve an existing one, add more words to the respective dictionary in the `dictionaries` folder.

## License

AGPLv3
