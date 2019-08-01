from PIL import Image
from os import system
import argparse

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

def writeLSB(img, text, name):
	try:
		im = Image.open(img)
		px = im.load()
		width, height = im.size
	except:
		exit("An unexpected error has occurred, unable to open the image...\nTry again")
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
	exit("Try using a larger image...\nTry again")

def readLSB(img):
	s = ""
	try:
		im = Image.open(img)
		px = im.load()
		width, height = im.size
	except:
		exit("An unexpected error has occurred, unable to open the image...\nTry again")
	for y in range(height):
		for x in range(width):
			for i in range(3):
				s += bin(px[x, y][i])[-1]
				if len(s) % 8 == 0 and s[-8:] == SEP:
					print
					return s[:-8]
	print("The message may be incomplete...")
	return s

def encode(img, text, verbose, save="lsb_enc"):
	if verbose:
		print("Encoding...\n")
	ext = img.split(".")
	name = save + "." + ext[-1]
	writeLSB(img, dec2bin(text) + SEP, name)
	print("   - Saved as:\n", name, sep="")
	if verbose:
		print("\nFinishing...")

def decode(img, verbose):
	if verbose:
		print("Decoding...\n")
	print("   - Message:")
	print(bin2dec(readLSB(img)))
	if verbose:
		print("\nFinishing...")

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
                           .##               SteganographyLSB
                      #######'             github.com/JAngel-98
    """)

	parser = argparse.ArgumentParser(description="SteganographyLSB")
	LSB = parser.add_mutually_exclusive_group(required=True)
	LSB.add_argument('-e', help="LSB to Image", action="store_true")
	LSB.add_argument('-d', help="LSB from Image", action="store_true")
	parser.add_argument("img", help="Image's Path (-d | -e required)")
	groupDec = parser.add_mutually_exclusive_group()
	groupDec.add_argument("-f", help="File's Path")
	groupDec.add_argument("-s", help="String")
	parser.add_argument("-sv", "--save", help="Save as...")
	parser.add_argument("-v", "--verbose", help="output verbosity", action="store_true")
	args = parser.parse_args()

	if args.f == None and args.s == None and args.e:
		exit("Encoding LSB: '-f' or '-s' args required")

	img = args.img
	if args.e:
		#============= Encoding =============
		if args.f != None:
			try:
				text = file2str(args.f)
			except:
				exit("An unexpected error has occurred, unable to read the file...")
				print("Try again")
		else:
			text = args.s
		if args.save != None:
			encode(img, text, args.verbose, args.save)
		else:
			encode(img, text, args.verbose)
	else:
		#============= Decoding =============
		decode(img, args.verbose)

if __name__ == "__main__":
	main()
