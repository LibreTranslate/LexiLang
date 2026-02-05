import sys
import re

def is_latin(word):
    return bool(re.match(r'^[a-zA-Z]+$', word))

def main():
    if len(sys.argv) != 2:
        print("Usage: python remove_latin.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    
    original_count = len(words)
    non_latin_words = [word for word in words if not is_latin(word)]
    remaining_count = len(non_latin_words)
    removed_count = original_count - remaining_count
    
    with open(filename, 'w', encoding='utf-8') as file:
        for word in non_latin_words:
            file.write(word + '\n')
    
    print(f"Statistics:")
    print(f"Original lines: {original_count}")
    print(f"Lines removed: {removed_count}")
    print(f"Remaining lines: {remaining_count}")

if __name__ == "__main__":
    main()