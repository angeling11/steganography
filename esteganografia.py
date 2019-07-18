from PIL import Image

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

def readLSB(im):
	s = ""
	px = im.load()
	width, height = im.size
	#print(height, width)
	for y in range(height):
		for x in range(width):
			for i in range(3):
				#print("{:08b}".format(px[x, y][i]), end=" ")
				s += bin(px[x, y][i])[-1]
				if len(s) % 8 == 0 and s[-8 : -1] == SEP:
					return s
		#print()
	return s

def encode(img, file):
	print("Encoding...\n")
	print("Finished...\nSaved as:")

def decode(img):
	print("Decoding...\n")
	im = Image.open(img)
	print("Message:")
	print(bin2dec(readLSB(im)))

encode("fox.png", "file")
decode("fox.png")
#print(dec2bin(file2str("file")))
#print(bin2dec(dec2bin(file2str("file"))))