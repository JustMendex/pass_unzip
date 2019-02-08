import zipfile
import os
def zipcracker(dictlocation,ziplocation):

    zfile=zipfile.ZipFile(ziplocation)

    passfile=open(dictlocation,'r')

    for line in passfile.readlines():

        password =line.strip('\n')
            
        try:

            zfile.extractall(pwd=password)

            print "[+] password= "+password +"\n"

        except Exception, e:

            pass 
            
def main():

    print "[*] input the location of the dictionary file to use "

    dictlocation = raw_input()

    if  os.path.isfile(dictlocation):
        
        print "[*] input the zip file to use "

        ziplocation = raw_input()

        if  os.path.isfile(ziplocation):

            print"[*]cracking password "

            zipcracker(dictlocation,ziplocation)

if __name__ =='__main__':

    main()