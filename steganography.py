from PIL import Image


# Fucntion to generate Binary format of given text to encode  
def binary_func(n):      #optional You can use inbuit func bin() but some error will get raise try to slove it.                    
  n = ord(n)

  binary = ''

  while True:
    binary = binary + str( n % 2 )
    n = n//2
    if n == 0:
      break
  binary = binary[::-1]

  return binary.zfill(8)

def convert_to_img(lis): 
  by = []
  for i in lis:
    by.extend((list(i)))
  data = bytes(by)
  im = Image.frombytes("RGB", (1280, 720), data) # Change size accordinf to your img very IMP
  return im


def encode():
  prompt_path = input('Enter path of img:- ')
  prompt_text = input('Enter the text you want to encode:- \n') # Put your own path of img any random you want.
  
  key = (len(prompt_text)*8)   # This is to generate key because this program change pixel values to encode.
  with open('Key.txt', 'w') as wrt:
    wrt.write(f" Your key is {key}")
    print('key generated !')
  encoding_img = Image.open(prompt_path) 
  size = encoding_img.size
  pixel = encoding_img.getdata()  # will get pixel format array
  pixel_list = list(pixel) 
  # print('Pixel Format of your Img:\n',pixel_list)


  pixel_list_mod = []
  for i in pixel_list:
    pixel_list_mod.extend((list(i)))
  # print('pixel_list_mod:- making sequence of pixel ex [R1,G1,B1,R2,B2,G2,...........')
  byte_list = [str(binary_func(x)) for x in prompt_text] # this code used own created binary func to change chr into binary
  
  k = 0
  for x in byte_list:

    for y in range(len(x)):
   
      if x[y] == '1':
        if pixel_list_mod[k] % 2 == 0:
          k = k+1
    
          continue 
        else:
    
          pixel_list_mod[k] = pixel_list_mod[k] - 1
          k = k+1 
      else:
        if pixel_list_mod[k] % 2 !=0:
          k = k+1
      
          continue 
        else:
      
          pixel_list_mod[k] = pixel_list_mod[k] + 1
          k = k+1
 
  pixel_new_list = []
  temp = []


  for u in range(len(pixel_list_mod)):

    temp.append(pixel_list_mod[u])

    if (u+1)%3 == 0:
      pixel_new_list.append(tuple(temp))
      temp = []

  return pixel_new_list


def decode():
    result = ''
    prompt_path = input('Enter path of img:- ')
    promt_len = int(input('Enter the key:- '))

    decoding_img = Image.open(prompt_path)

    pixel = decoding_img.getdata()
    pixel_list = list(pixel)

    pixel_list_mod = []
    for i in pixel_list:
        pixel_list_mod.extend((list(i)))
    res =''
    for i in range(promt_len):

        if pixel_list_mod[i] % 2 == 0:
            res = res+'1'

     
        else:
            res = res + '0'
           

        if len(res) == 8:
            
            result = result + chr(int(res,2))
        
            res = ''

    return result
            
     
    




if __name__ == '__main__':
    choice = int(input("If want to Encode into IMG Press 1\nIf Decode Encoded Img Press 2\n"))
    if choice == 1:
        lis = encode()
        imm = convert_to_img(lis)
        imm.save('Encoded.png')
    else:
        print((decode()))
      






