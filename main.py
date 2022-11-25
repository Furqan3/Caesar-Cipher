#List of all alphabet
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#Encode the message
def caesar_cypher(string,shift):
    str=''
    for a in string:
        if a in Alphabet:
         x=Alphabet.index(a)+shift
         if x>52:
            x=x-53
            #x=x*-1    
         str=str+Alphabet[x]
        else:
            print(f'Error you have entered {a}')
            print('Only enter letters and spaces not symbols')
            input('Enter any key to exit')
            exit()
    return str
#Decode the message
def decode(string,shift):
    str=''
    for a in string:
        if a in Alphabet:
         x=Alphabet.index(a)-shift
         # if x<0:
         #     x=26+x   
         str=str+Alphabet[x]
        else:
            print(f'Error you have entered {a}')
            print('Only enter letters and spaces not symbols')
            input('Enter any key to exit')
            exit()
    return str
#choice
x=input('Choose:\n 1->Encoding\n 2->Decoding\n :')
print('Only enter Letter(upper case and lower case) and spaces!')
#for encoding
if x=='1':
    str=input('Enter messge you want to encode:')
    shf=input('Enter the shift:')
    print('--Encoded message--')
    print(caesar_cypher(str,int(shf)))
#for decoding
elif x=='2':
    str=input('Enter the decoded string:')
    shf=input('Enter the shift:')
    print('--Decoded message--')
    print(decode(str,int(shf)))
#if entered wrong choice
else:
    print('Error choose from the above')
#Exit
input('Enter any key to exit')