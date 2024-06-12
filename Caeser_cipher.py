alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        cipher_text = cipher_text + alphabet[position + shift]
    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
  plain_text = " "
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


if direction == ("encode"):
  encrypt(text, shift)
else:
  decrypt(text, shift)
