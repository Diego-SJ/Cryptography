from io import open
import matplotlib.pyplot as plt


def Cesar_decrypt():
    
    # Read file with encrypted message
    txtFile = open('MessageEncrypted.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    encrypted_text = ""
    for fc in fileContent:
        encrypted_text += fc.replace("\n", " ").upper()

    print("\n\n========== Encrypted text ==========\n\n", encrypted_text,'\n\n')

     # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

    allKeys = ""

    for idxKey in range(len(alphabet)):
        # Cesar Decrypt method
        plain_text = ""
        for et in encrypted_text:
            if et in alphabet:
                plain_text += alphabet[((alphabet.index(et) - idxKey) % (len(alphabet)))]
            else:
                if et == " ":
                    plain_text += " "
                else:
                    plain_text += ""
        
        print('KEY '+str(idxKey)+' ===> '+plain_text+'\n')
        allKeys += ('KEY '+str(idxKey)+' ===> '+plain_text+'\n')


    # Create output file
    outputFile = open('results.txt','w')
    outputFile.write(allKeys)
    outputFile.close() 



def main():
    Cesar_decrypt()

if __name__ == "__main__":
    main()