massage = input ("Enter your tex :  ") 
key = int(input("Enter key to Cryptography: "))
for i in massage:
  num = ord(i)
  num += key
  translated = " "
  translated += chr(num)
  print(translated)