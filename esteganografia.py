from PIL import Image
from os import system

SEP = "11111111"

def file2str(dr):
	with open(dr) as file:
		return file.read()

def dec2bin(strg):
	s = ""
	for i in strg:
		s += "{:08b}".format(ord(i))
	return s

def bin2dec(strg):
	s = ""
	for i in range(0, len(strg), 8):
		s += chr(int(strg[i : i + 8], 2))
	return s

def writeLSB(im, text, name):
	px = im.load()
	width, height = im.size
	c = 0
	fin = False
	for y in range(height):
		for x in range(width):
			val = []
			for i in range(3):
				if c >= len(text):
					val.append(int(px[x, y][i]))
					fin = True
				else:
					val.append(int("{:08b}".format(px[x, y][i])[:7] + text[c], 2))
				c += 1
			px[x, y] = tuple(val)
			if fin:
				im.save(name)
				return

def readLSB(im):
	s = ""
	px = im.load()
	width, height = im.size
	for y in range(height):
		for x in range(width):
			for i in range(3):
				s += bin(px[x, y][i])[-1]
				if len(s) % 8 == 0 and s[-8:] == SEP:
					print
					return s[:-8]
	return s

def encode(img, file):
	print("Encoding...\n")
	ext = img.split(".")
	name = "encoded." + ext[-1]
	im = Image.open(img)
	text = file2str(file)
	writeLSB(im, dec2bin(text) + SEP, name)
	print("   - Saved as:\n", name, "\n\nFinished...", sep="")

def decode(img):
	print("Decoding...\n")
	im = Image.open(img)
	print("   - Message:")
	print(bin2dec(readLSB(im)))
	print("\nFinished...")

def main():
	system("clear")
	print("""
     .#.                               ##             .#######. 
    /# #\\                              ##             ###    ## 
    ## ##                              ## ##          ##        
   /#   #\\   ##                        ##    ##       ##        
   ##   ##   ## ####. .######. .#####. ## ## ## ####. ##  ##### 
  /#######\\  ###  ### ##'  '## ##   ## ## ## ###  ### ##  ##### 
  ##     ##  ##    ## ##    ## ####### ## ## ##    ## ##     ## 
 /##     ##\\ ##    ## ##.  .## ##      ## ## ##    ## ###    ## 
 ##       ## ##    ## '####### '###### ## ## ##    ## '######## 
                            ##                               ## 
                           .##                 Steganigraphy    
                      #######'             github.com/JAngel-98 
    """)

	print("1. Encode")
	print("2. Decode")
	answ = int(input(" => "))
	if(answ == 1):
		print("\n\n ============= Encode =============")
		img = input("Image: ")
		txt = input("File: ")
		encode(img, txt)
	elif(answ == 2):
		print("\n\n ============= Decode =============")
		img = input("Image: ")
		decode(img)
	else:
		print("Error")

if __name__ == "__main__":
	main()