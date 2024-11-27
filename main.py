MORSE_DICTIONARY = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
    ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--', 
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    """Converts text to Morse code."""
    morse_code = []
    for char in text.upper():
        if char in MORSE_DICTIONARY:
            morse_code.append(MORSE_DICTIONARY[char])
        else:
            morse_code.append('?')
    return ' '.join(morse_code)

def main():
    print("Text to Morse Code Converter")
    print("-----------------------------")
    while True:
        text = input("\nEnter text to convert (or type '!exit' to quit): ")
        if text.lower() == '!exit':
            print("Exiting program. Goodbye!")
            break
        morse = text_to_morse(text)
        print(f"Morse Code: {morse}")
        print()
        

main()
