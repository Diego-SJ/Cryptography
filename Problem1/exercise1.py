from io import open
import matplotlib.pyplot as plt

def cesar_encryption():
    
    # Read file
    txtFile = open('file.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ").upper()

    print("\n\n========== Plain text ==========\n\n", plain_text)

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    A=0;B=0;C=0;D=0;E=0;F=0;G=0;H=0;I=0;J=0;K=0;L=0;M=0;N=0;Ñ=0;O=0;P=0;Q=0;R=0;S=0;T=0;U=0;V=0;W=0;X=0;Y=0;Z=0
    one=0;two=0;three=0;four=0;five=0;six=0;seven=0;eigth=0;nine=0;ten=0

    # Scroll key
    key = int (input("\n---------- Cesar's key: ")) % len(alphabet)

    # Encrypted text variable
    encrypted_text = ""
    
    # Cesar encryption method
    for pt in plain_text:
        if pt in alphabet:

            le = alphabet[((alphabet.index(pt) + key) % (len(alphabet)))]

            encrypted_text += le

            # data for histogram
            if le == 'A': A += 1
            if le == 'B': B += 1
            if le == 'C': C += 1
            if le == 'D': D += 1
            if le == 'E': E += 1
            if le == 'F': F += 1
            if le == 'G': G += 1
            if le == 'H': H += 1
            if le == 'I': I += 1
            if le == 'J': J += 1
            if le == 'K': K += 1
            if le == 'L': L += 1
            if le == 'M': M += 1
            if le == 'N': N += 1
            if le == 'Ñ': Ñ += 1
            if le == 'O': O += 1
            if le == 'P': P += 1
            if le == 'Q': Q += 1
            if le == 'R': R += 1
            if le == 'S': S += 1
            if le == 'T': T += 1
            if le == 'U': U += 1
            if le == 'V': V += 1
            if le == 'W': W += 1
            if le == 'X': X += 1
            if le == 'Y': Y += 1
            if le == 'Z': Z += 1
            if le == '0': one += 1
            if le == '1': two += 1
            if le == '2': three += 1
            if le == '3': four += 1
            if le == '4': five += 1
            if le == '5': six += 1
            if le == '6': seven += 1
            if le == '7': eigth += 1
            if le == '8': nine += 1
            if le == '9': ten += 1

        else:
            if pt == " ":
                encrypted_text += pt
            else:
                encrypted_text += ""
    
    # Print encrypted text
    print("\n\n========== Text encrypted by cesar ==========\n\n",encrypted_text)

    # Create output file
    outputFile = open('fileC.txt','w')
    outputFile.write(encrypted_text)
    outputFile.close() 
    print("\n\n========== Check fileC.txt file ==========\n\n") 

    fig = plt.figure(u'Histograma')
    ax = fig.add_subplot(111)

    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    num = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eigth,nine,ten]
    xx = range(len(num))

    ax.bar(xx,num,width=0.8,align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(abc)

    plt.show()


def main():
    
    cesar_encryption()

if __name__ == "__main__":
    main()