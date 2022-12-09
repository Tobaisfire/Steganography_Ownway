# Steganography_Ownway a Streamlit WebApp
A progarm to encode text data into Image  with decoding Function.

Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination. The use of steganography can be combined with encryption as an extra step for hiding or protecting data. The word steganography is derived from the Greek words steganos (meaning hidden or covered) and the Greek root graph (meaning to write).

# Output

![image](https://user-images.githubusercontent.com/67000746/206674897-f9def5df-c526-4a70-b454-83f6c141b2ef.png)

# Methodology

1] Program takes Img and returns its pixel list in format of (R,G,B).
  

  Size of img: (1280, 720)

Pixel format of above fig: 
[(23, 24, 10), (35, 35, 23), (24, 26, 13), (16, 18, 7), (28, 31, 22), (26, 29, 22), (9, 14, 7), (8, 15, 8), (12, 22, 14), (7, 19, 9), (11, 23, 13), (28, 42, 29), (44, 61, 45), (46, 63, 45), (28, 47, 28), (10, 29, 9), (0, 17, 5), (5, 25, 13), (25, 45, 33), (22, 42, 30), (35, 53, 39), (96, 114, 100),...]
i.e [ (R1,G1,B1) , (R2,G2,B2),.....]

2] Ater taking text to encode, program converts every character of text into binary format.

3]  For encoding program takes text binary format list and start doing encoding like this :-
    example character 'h' and it's binary 01101000
    
    
   Main logic:-  if 1 convert pixel to even and if 0 convert pixl to odd.
   
   ![image](https://user-images.githubusercontent.com/67000746/206677859-871510d2-2fd4-4b50-85eb-5754ad54c513.png)
    
    Visual explanation below:- 
      
   ![image](https://user-images.githubusercontent.com/67000746/206677567-28f5f9d5-5559-4306-92f2-7d3a1d6678fd.png)
   
4] For decoding reverse the logic of encoding.


# How to run project -->

1] Read requirements

2] Run Steganography_stream.py

3] Write text on text area and uplaod img to encode them click on button encode. Note( Download button for downloading encode img).

4] Upload encoded img and click decode.

5] Enjoy !!!!!!!!!!!!!!!!!!!!!!!!!

 
  
    
