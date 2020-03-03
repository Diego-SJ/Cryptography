from io import open
import matplotlib.pyplot as mpl

def encryption():
    plainTextFile = open('plainText.txt','r', encoding="utf8")
    textFile = plainTextFile.readlines()
    plainTextFile.close()

    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
    plainText = ""
    plainTextClean = ""

    for tf in textFile:
        plainText += tf.replace("\n", " ").upper()

    for et in plainText:
        if et in alphabet:
            plainTextClean += et
        else:
            if et == " ":
                plainTextClean += " "
            else:
                plainTextClean += ""

    print("\n\n============================================================")
    print("                         PLAIN TEXT                         ")
    print("============================================================\n")
    print(plainTextClean)

    A=0;B=0;C=0;D=0;E=0;F=0;G=0;H=0;I=0;J=0;K=0;L=0;M=0;N=0;Ñ=0;O=0;P=0;Q=0;R=0;S=0;T=0;U=0;V=0;W=0;X=0;Y=0;Z=0
    one=0;two=0;three=0;four=0;five=0;six=0;seven=0;eigth=0;nine=0;ten=0

    key = str(input("\n~# messy alphabet: ")).upper()
    cipherText = ''

    if keyValidate(alphabet,key):
        for i in range(len(plainTextClean)):
            if plainTextClean[i] in alphabet:
                indxAlpha = alphabet.find(plainTextClean[i])
                cipherText += key[indxAlpha]

                if key[indxAlpha] == 'A': A += 1
                if key[indxAlpha] == 'B': B += 1
                if key[indxAlpha] == 'C': C += 1
                if key[indxAlpha] == 'D': D += 1
                if key[indxAlpha] == 'E': E += 1
                if key[indxAlpha] == 'F': F += 1
                if key[indxAlpha] == 'G': G += 1
                if key[indxAlpha] == 'H': H += 1
                if key[indxAlpha] == 'I': I += 1
                if key[indxAlpha] == 'J': J += 1
                if key[indxAlpha] == 'K': K += 1
                if key[indxAlpha] == 'L': L += 1
                if key[indxAlpha] == 'M': M += 1
                if key[indxAlpha] == 'N': N += 1
                if key[indxAlpha] == 'Ñ': Ñ += 1
                if key[indxAlpha] == 'O': O += 1
                if key[indxAlpha] == 'P': P += 1
                if key[indxAlpha] == 'Q': Q += 1
                if key[indxAlpha] == 'R': R += 1
                if key[indxAlpha] == 'S': S += 1
                if key[indxAlpha] == 'T': T += 1
                if key[indxAlpha] == 'U': U += 1
                if key[indxAlpha] == 'V': V += 1
                if key[indxAlpha] == 'W': W += 1
                if key[indxAlpha] == 'X': X += 1
                if key[indxAlpha] == 'Y': Y += 1
                if key[indxAlpha] == 'Z': Z += 1
                if key[indxAlpha] == '0': one += 1
                if key[indxAlpha] == '1': two += 1
                if key[indxAlpha] == '2': three += 1
                if key[indxAlpha] == '3': four += 1
                if key[indxAlpha] == '4': five += 1
                if key[indxAlpha] == '5': six += 1
                if key[indxAlpha] == '6': seven += 1
                if key[indxAlpha] == '7': eigth += 1
                if key[indxAlpha] == '8': nine += 1
                if key[indxAlpha] == '9': ten += 1
            else:
                if plainTextClean[i] == " ":
                    cipherText += " "
                else:
                    cipherText += ""

        outputFile = open('cipherText.txt','w')
        outputFile.write(cipherText)
        outputFile.close()

        print("\n\n============================================================")
        print("                        CIPHER TEXT                         ")
        print("============================================================\n")
        print(cipherText,"\n\n")


        histogram = mpl.figure(u'FRECUENCY HISTOGRAM ON CIPHER TEXT')
        axis = histogram.add_subplot(111)

        aLabels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        num = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eigth,nine,ten]
        xx  = range(len(num))
        axis.bar(xx,num,width=0.5,align='center')
        axis.set_xticks(xx)
        axis.set_xticklabels(aLabels)
        mpl.show()

def keyValidate(alphabet,key):
    if(len(alphabet) != len(key)):
        print("\n\n******************************************************************")
        print(" THE KEY MUST BE EQUAL TO THE ALPHABET [A-Z][0-9] (37 CHARACTERS)")
        print("******************************************************************\n\n")
        return False

    flag = True
    for a in alphabet:
        if not a in key:
            flag = False

    if not flag:
        print("\n\n******************************************************************")
        print("        MISSING ONE LETTER OF THE ALPHABET IN YOUR KEY        ")
        print("******************************************************************\n\n")
        return False
    else:
        return True

def main():
    encryption()

if __name__ == "__main__":
    main()

# QWERTYUIOPASDFGHJKLZXCVBNMÑ0978651423
# 12345QWERTYUIOP67890MNBVCXZALKSJDHFGÑ
# 123ASDFGHJKL456POIUYTREWQ789ZXCVBNM0Ñ
# 1QAZXSW23EDCVFR45ÑTGBNHY67UJMKI89OLP0