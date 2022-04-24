import crypt

def testPass(cryptPass):
    with open('dictionary.txt', 'r') as dictFile:
        salt = '$6$'+cryptPass.split('$')[2] # salt should be $6$~~~~ format
        #print(salt)
        for word in dictFile.readlines():
            word = word.strip('\n') # delete new line char in word
            cryptWord = crypt.crypt(word, salt)
            if (cryptWord == cryptPass):
                print( "[+] Found Password : "+word+"\n")
                return
        print( "[-] Password Not found \n")
    return

def main():
    with open('password.txt', 'r') as passFile:
        for line in passFile.readlines():
            if ":" in line :
                user = line.split(':')[0]
                cryptPass = line.split(':')[1]
                print("[*] Cracking Password For : "+user)  
                testPass(cryptPass)

if __name__ == "__main__": # only run this part if not imported
    main()