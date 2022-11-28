import sys

def base64decode(s):
  i = 0
  base64 = decoded = ''
  base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  
  # Replace padding with "A" characters so the decoder can process the string, and save the padding length for later
  if s[-2:] == '==':
    s = s[0:-2] + "AA"
    padd = 2
  elif s[-1:] == '=':
    s = s[0:-1] + "A"
    padd = 1
  else:
    padd = 0
  
  # Take 4 characters at a time 
  while i < len(s):
    d = 0
    for j in range(0,4,1):
      
      d += base64chars.index( s[i] ) << (18 - j * 6)
      i += 1
    
    # Convert the 4 chars back to ASCII
    decoded += chr( (d >> 16 ) & 255 )
    decoded += chr( (d >> 8 ) & 255 )
    decoded += chr( d & 255 )
  
  # Remove padding
  decoded = decoded[0:len( decoded ) - padd]
  
  # Print the Base64 encoded result
  print (decoded)

base64decode(sys.argv[1])
