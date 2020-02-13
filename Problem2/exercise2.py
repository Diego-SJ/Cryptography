import sys
from io import open
import matplotlib.pyplot as plt

def mono_encryption():
    txtFile = open('file.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ")

    # Print the plaint text
    print("\n\n========== Plain text ==========\n\n", plain_text)

    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
    A=0;B=0;C=0;D=0;E=0;F=0;G=0;H=0;I=0;J=0;K=0;L=0;M=0;N=0;Ñ=0;O=0;P=0;Q=0;R=0;S=0;T=0;U=0;V=0;W=0;X=0;Y=0;Z=0
    one=0;two=0;three=0;four=0;five=0;six=0;seven=0;eigth=0;nine=0;ten=0

    message = plain_text.upper()

    # Examples of Messy Alphabets
    # QWERTYUIOPASDFGHJKLZXCVBNMÑ0978651423
    # 12345QWERTYUIOP67890MNBVCXZALKSJDHFGÑ
    # 123ASDFGHJKL456POIUYTREWQ789ZXCVBNM0Ñ
    # 1QAZXSW23EDCVFR45ÑTGBNHY67UJMKI89OLP0

    clave = str(input("\n\n-------Messy alphabet: ")).upper() 
    cifrado = ''

    # Encrypted text
    if checkKey(alphabet,clave): 
        for i in range(len(message)):
            if message[i] in alphabet:
                letter = message[i]

                indxAlpha = alphabet.find(letter) #int
                cifrado += clave[indxAlpha]

                # data for histogram
                if clave[indxAlpha] == 'A': A += 1
                if clave[indxAlpha] == 'B': B += 1
                if clave[indxAlpha] == 'C': C += 1
                if clave[indxAlpha] == 'D': D += 1
                if clave[indxAlpha] == 'E': E += 1
                if clave[indxAlpha] == 'F': F += 1
                if clave[indxAlpha] == 'G': G += 1
                if clave[indxAlpha] == 'H': H += 1
                if clave[indxAlpha] == 'I': I += 1
                if clave[indxAlpha] == 'J': J += 1
                if clave[indxAlpha] == 'K': K += 1
                if clave[indxAlpha] == 'L': L += 1
                if clave[indxAlpha] == 'M': M += 1
                if clave[indxAlpha] == 'N': N += 1
                if clave[indxAlpha] == 'Ñ': Ñ += 1
                if clave[indxAlpha] == 'O': O += 1
                if clave[indxAlpha] == 'P': P += 1
                if clave[indxAlpha] == 'Q': Q += 1
                if clave[indxAlpha] == 'R': R += 1
                if clave[indxAlpha] == 'S': S += 1
                if clave[indxAlpha] == 'T': T += 1
                if clave[indxAlpha] == 'U': U += 1
                if clave[indxAlpha] == 'V': V += 1
                if clave[indxAlpha] == 'W': W += 1
                if clave[indxAlpha] == 'X': X += 1
                if clave[indxAlpha] == 'Y': Y += 1
                if clave[indxAlpha] == 'Z': Z += 1
                if clave[indxAlpha] == '0': one += 1
                if clave[indxAlpha] == '1': two += 1
                if clave[indxAlpha] == '2': three += 1
                if clave[indxAlpha] == '3': four += 1
                if clave[indxAlpha] == '4': five += 1
                if clave[indxAlpha] == '5': six += 1
                if clave[indxAlpha] == '6': seven += 1
                if clave[indxAlpha] == '7': eigth += 1
                if clave[indxAlpha] == '8': nine += 1
                if clave[indxAlpha] == '9': ten += 1
            else:
                if message[i] == " ":
                    cifrado += " "
                else:
                    cifrado += ""
        
        # Create output file
        outputFile = open('fileM.txt','w')
        outputFile.write(cifrado)
        outputFile.close() 
        
        print("\n\n========== Encrypted text ==========\n\n",cifrado,"\n\n")

        # Plot Histogram
        fig = plt.figure(u'Histograma')
        ax = fig.add_subplot(111)

        abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        num = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eigth,nine,ten]
        xx = range(len(num))

        ax.bar(xx,num,width=0.8,align='center')
        ax.set_xticks(xx)
        ax.set_xticklabels(abc)

        plt.show()
        

    

def checkKey(alphabet,key):
    if(len(alphabet) != len(key)):
        print('\n\nTHE KEY MUST BE EQUAL TO THE ALPHABET [A-Z] - [0-9] (37 CHARACTERS)')
        return False
    
    i = 0
    for a in alphabet:
        if not a in key:
            i += 1

    if i > 0:
        print('\n\nA LETTER OF THE ALPHABET IS MISSING IN YOUR KEY')
        return False
    else:
        return True

def main():
    
    mono_encryption()

if __name__ == "__main__":
    main()