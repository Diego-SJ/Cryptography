from io import open
import matplotlib.pyplot as mpl

def encript():
    plainTextFile = open('plainText.txt','r', encoding="utf8")
    textFile = plainTextFile.readlines()
    plainTextFile.close()

    plainText = ""
    for tf in textFile:
        plainText += tf.replace("\n", " ").upper()

    print("\n\n============================================================")
    print("                         PLAIN TEXT                         ")
    print("============================================================\n")
    print(plainText)

    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    A=0;B=0;C=0;D=0;E=0;F=0;G=0;H=0;I=0;J=0;K=0;L=0;M=0;N=0;Ñ=0;O=0;P=0;Q=0;R=0;S=0;T=0;U=0;V=0;W=0;X=0;Y=0;Z=0
    one=0;two=0;three=0;four=0;five=0;six=0;seven=0;eigth=0;nine=0;ten=0

    key = int (input("\n~# insert the key: ")) % len(alphabet)

    cipherText = ""
    for pt in plainText:
        if pt in alphabet:
            cc = alphabet[((alphabet.index(pt) + key) % (len(alphabet)))]
            cipherText += cc
            if cc == 'A': A += 1
            if cc == 'B': B += 1
            if cc == 'C': C += 1
            if cc == 'D': D += 1
            if cc == 'E': E += 1
            if cc == 'F': F += 1
            if cc == 'G': G += 1
            if cc == 'H': H += 1
            if cc == 'I': I += 1
            if cc == 'J': J += 1
            if cc == 'K': K += 1
            if cc == 'L': L += 1
            if cc == 'M': M += 1
            if cc == 'N': N += 1
            if cc == 'Ñ': Ñ += 1
            if cc == 'O': O += 1
            if cc == 'P': P += 1
            if cc == 'Q': Q += 1
            if cc == 'R': R += 1
            if cc == 'S': S += 1
            if cc == 'T': T += 1
            if cc == 'U': U += 1
            if cc == 'V': V += 1
            if cc == 'W': W += 1
            if cc == 'X': X += 1
            if cc == 'Y': Y += 1
            if cc == 'Z': Z += 1
            if cc == '0': one += 1
            if cc == '1': two += 1
            if cc == '2': three += 1
            if cc == '3': four += 1
            if cc == '4': five += 1
            if cc == '5': six += 1
            if cc == '6': seven += 1
            if cc == '7': eigth += 1
            if cc == '8': nine += 1
            if cc == '9': ten += 1
        else:
            if pt == " ":
                cipherText += pt
            else:
                cipherText += ""

    print("\n\n============================================================")
    print("                        CIPHER TEXT                         ")
    print("============================================================\n")
    print(cipherText,"\n\n")

    cipherTextFile = open('cipherText.txt','w')
    cipherTextFile.write(cipherText)
    cipherTextFile.close()

    histogram = mpl.figure(u'FRECUENCY HISTOGRAM ON CIPHER TEXT')
    axis = histogram.add_subplot(111)

    aLabels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    num = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eigth,nine,ten]
    xx  = range(len(num))
    axis.bar(xx,num,width=0.5,align='center')
    axis.set_xticks(xx)
    axis.set_xticklabels(aLabels)
    mpl.show()

def main():
    encript()

if __name__ == "__main__":
    main()