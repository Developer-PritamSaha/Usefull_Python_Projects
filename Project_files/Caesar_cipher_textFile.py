import string
import time

def caesar_cipher_dictionary(shift):
    '''This returns a dictionary which has all alphabet's corresponding shifted or cipher alphabet'''
    l = string.ascii_lowercase
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i+shift)%26] 
        d[(l[i].upper())] = d[l[i]].upper()
    return d

def encrypter_decrypter(s,shift):
    '''This will return an encrypted or decrypted sentence'''
    cipher_d = caesar_cipher_dictionary(shift)
    cipher_text = ''
    for i in s:
        if i.isalpha():
            i = cipher_d[i]
        cipher_text += i
    return cipher_text


print('\n <<| Hello, here you can encrypt OR decrypt a text file |>>')
t = input('\n#> Please provide the text file location(like C:\\Users\\Example.txt ) 3> ')
f = 1
c = 0
fileName = ''

while c > (-50):
    if (c == (-4)) :
        if fileName != '.txt':
            f = 0
            break
        else:
            fileName = ''
    c -= 1
    if t[c] == '\\':
        c = (c + 1) * (-1)
        break
    fileName = t[c] + fileName
    if c == (-50):
        f = 0
    
if f == 0:
    print("\n  <!> Please check your entered file path <!>")
else:
    #print(f"fileName > {fileName}")
    path = ''
    for i in range(0,(len(t)-c)):
        if t[i] == '\\':
            path += "\\\\"
        else:
            path += t[i]

    m_path = path + fileName + '.txt'

    #print(f'>>>> {m_path}')
    p = open(m_path,'r')

    #print(f'fileName >> {fileName[-11:]}')
  
    # if (fileName[-11:] == '(Encrypted)') or (fileName[-11:] == '(Decrypted)'):
    #     fileName = fileName[0:-11]
        #<<< OR >>>#
    if ('(Encrypted)' in fileName) or ('(Decrypted)' in fileName) :
        fileName = fileName[0:-11]
    #print(f'fileName >> {fileName}')
    e_path = path + fileName + '(Encrypted)' + '.txt'
    d_path = path + fileName + '(Decrypted)' + '.txt'
    

    shift = int(input("\n # Enter the shift amount : "))#> This will shift a charcter by given input times.
    choice = input("\n ##> Do you wanted to encrypt or decrypt then type 'e' or 'd' : ").lower()
    if choice == 'd':
        shift *= (-1)
    if choice == 'e':
        temp = open(e_path,'w')
    else:
        temp = open(d_path,'w')

    before_T = time.time()

    s = p.readline()
    while (s != ''):
        x = encrypter_decrypter(s,shift)
        #temp.write(f'{x}\n')
        temp.write(x)
        s = p.readline()
        if s == '':
            p.close()
            temp.close()

    after_T = time.time()
    time_taken = after_T - before_T

print_choice = 'n'
if choice == 'e':
    print(f"\n@>> Text encryption completed in {time_taken}s.")
    print_choice = input("\n >> Do you want to print the encrypted file on the console(y/n)? ").lower()
    temp = open(e_path,'r')
    print(f"\n @ Filename >> {fileName}(Encrypted).txt \n\n  #> The encrypted file has been saved to the original files's location.\n")
else:
    print(f"\n@>> Text decryption completed in {time_taken}s.")
    print_choice = input("\n >> Do you want to print the decrypted file on the console(y/n)? ").lower()
    temp = open(d_path,'r')
    print(f"\n @ Filename >> {fileName}(Decrypted).txt \n\n  #> The decrypted file has been saved to the original files's location.\n")


if print_choice == 'y':
    s = temp.read()
    print("----------------------------------------SOF-----------------------------------------------")
    print(f'\n {s}\n')
    print("----------------------------------------EOF-----------------------------------------------")
    temp.close()

        
    
