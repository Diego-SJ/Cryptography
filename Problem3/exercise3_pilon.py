ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

def decrypt(c_text, key=None):
    cipher_text = c_text.upper()

    if key is None:
        key = find_key_from_cipher(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        #Skipping special characters (incomplete solution)
        if letter in ALPHABET:
            plain_text += ALPHABET[((ALPHABET.index(letter) - key) % (len(ALPHABET)))]
        else:
            if letter == " ":
                cipher_text += letter
            else:
                cipher_text += ""

    return plain_text

def find_key_from_cipher(cipher_text):
    index_of_most_common_letter = 4 #Index of 'e'

    #Calculate distribution
    distribution_dict = analyse_letter_distribution(cipher_text)
    #Get common letters
    common_letters = sorted(distribution_dict, key=distribution_dict.get, reverse=True)
    print('cl: ',common_letters)
    #Use most common letter to get key
    key = ALPHABET.find(common_letters[0]) - index_of_most_common_letter % (len(ALPHABET))
    return key

def analyse_letter_distribution(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        if letter not in ALPHABET:
            continue
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    print(distribution_dict)
    
    return distribution_dict


if __name__ == "__main__":

    # Read file
    txtFile = open('MessageEncrypted.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    secret = ""
    for fc in fileContent:
        secret += fc.replace("\n", " ").upper()
    
    print(secret)

    print(decrypt(secret))
