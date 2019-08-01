# SteganographyLSB Tool
*by AngelinG*

Steganography Tool help us to hide a message into an image.
It uses LSB in order to modify the least significant bits color values of image's pixels.
## Requirements
- python 3.+
- [Pillow](https://pillow.readthedocs.io/en/latest/installation.html#basic-installation) Library

## Usage
steganography.py (-e | -d) [-f F | -s S] [-sv SAVE] [-v] img

In a simple command line an image can be written (-e flag) or read (-d flag).
In case of encode, a File's Path or a String have to be provided, it must be specified with a flag *(see optional arguments)*. Furthermore, the name of the resulting image can be chosen, by default it's named *lsb_enc*.

### Arguments
+ img Image's Path (-d | -e also required)
+ -e LSB to Image
+ -d LSB from Image

#### Optional arguments

Flag | Description
---- | ----
-h, --help | help
-f F | File's Path
-s S | String
-sv SAVE, --save SAVE | Save image as...
-v, --verbose | output verbosity

### Examples
The next lines must be written in a Command line.
#### Encoding
> python3 steganography.py -e example.png -s "Example" -sv "save_lsb" -v

 Some flags can be changed *(see optional arguments)*.

#### Decoding
> python3 steganography.py -d example.png

It doesn't need any args else.
