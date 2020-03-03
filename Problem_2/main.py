from io import open
import matplotlib.pyplot as plt

def decrypt():
    cipherTextFile = open('cipherText.txt','r', encoding="utf8")
    fileContent = cipherTextFile.readlines()
    cipherTextFile.close()

    cipherText = ""
    for fc in fileContent:
        cipherText += fc.replace("\n", " ").upper()

    print("\n\n============================================================")
    print("                        CIPHER TEXT                         ")
    print("============================================================\n")
    print(cipherText)

    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

    key = int (input("\n~# insert the key: ")) % len(alphabet)

    plainText = ""
    for et in cipherText:
        if et in alphabet:
            plainText += alphabet[((alphabet.index(et) - key) % (len(alphabet)))]
        else:
            if et == " ":
                plainText += " "
            else:
                plainText += ""

    print("\n\n============================================================")
    print("                         PLAIN TEXT                         ")
    print("============================================================\n")
    print(plainText,"\n\n")

    for idxKey in range(len(alphabet)):
        plain_text = ""
        for et in cipherText:
            if et in alphabet:
                plain_text += alphabet[((alphabet.index(et) - idxKey) % (len(alphabet)))]
            else:
                if et == " ":
                    plain_text += " "
                else:
                    plain_text += ""
        outputFile = open('./all keys/' + alphabet[idxKey] + '_key.txt','w')
        outputFile.write(plain_text)
        outputFile.close()

    print("============================================================")
    print("                        CREATED FILES                         ")
    print("============================================================\n\n")

def main():
    decrypt()

if __name__ == "__main__":
    main()