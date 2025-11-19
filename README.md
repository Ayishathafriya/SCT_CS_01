# SCT_CS_01
#  Caesar Cipher Tool

A simple Python script that performs Caesar Cipher encryption and decryption on user-provided text. This classic cryptographic technique shifts each letter in the message by a fixed number of positions in the alphabet.

##  Features

- Encrypts text using Caesar Cipher
- Decrypts encrypted text using the same shift value
- Handles both uppercase and lowercase letters
- Preserves non-alphabetic characters (e.g., punctuation, spaces)

##  How It Works

The Caesar Cipher shifts each letter in the input text by a specified number of positions. For example, with a shift of 3:
- `A` becomes `D`
- `B` becomes `E`
- `Z` wraps around to `C`

Decryption simply reverses the shift.

##  Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Script

1. Clone or download the repository.
2. Run the script in your terminal or IDE:

```bash
python caesar_cipher.py
```

3. Enter your message and shift value when prompted.

##  Example

```
Enter your message: Hello, World!
Enter shift value (e.g., 3): 3
Encrypted message: Khoor, Zruog!
Decrypted message: Hello, World!
```

##  File Structure

```
caesar-cipher/
└── caesar_cipher.py       # Main script
```

