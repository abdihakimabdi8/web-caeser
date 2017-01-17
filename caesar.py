
def alphabet_position(char):
  #letter = input("enter alphabet:")

  alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  balpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  for item in char:
    if item.isalpha() == False:
      alphapos = char
    elif item.isupper() == True:
      alphapos = balpha.index(item)
    else:
      alphapos = alpha.index(item)
  return alphapos

def rotate_character(char, rot):
  alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  balpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  #char = input("input char")
  #rot = int(input("number of rotations"))
  rotated_character = ""
  for i in char:
    if not i.isalpha():
      rotated_character+= i
    elif i.isupper():
      rotCharindex = (alphabet_position(char) + int(rot))%26
      rotated_character = str(balpha[rotCharindex])
    else:
      rotCharindex = (alphabet_position(char) + int(rot))%26
      rotated_character = str(alpha[rotCharindex])
  return rotated_character

def encrypt(text, rot):
  alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  balpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  ceasermessage = ""
  for char in text:
    if not char.isalpha():
      ceasermessage += char
    elif char.isupper() == True:
      newIndex = balpha.index(rotate_character(char, int(rot)))
      ceaserAlpha = str(balpha[newIndex])
      ceasermessage += ceaserAlpha
    else:
      newIndex = alpha.index(rotate_character(char, int(rot)))
      ceaserAlpha = str(alpha[newIndex])
      ceasermessage += ceaserAlpha
  return ceasermessage
