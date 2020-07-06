# Imports
from EncoderDecoder import EncoderDecoder
import argparse
import sys

# Set up Encoder/Decoder object.
ed = EncoderDecoder()

# Set up parser object and arguments.
parser = argparse.ArgumentParser(description='Encode/Decode your data.')
parser.add_argument('-e', '--encode', metavar='string', type=str, nargs='+',
										help='A string to encode.')
parser.add_argument('-d','--decode', metavar='int', type=int, nargs='+',
                    help='Array of integers to decode into a sentence.')
# Handling no input.
if len(sys.argv)==1:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

# Decode
if(args.decode):
	try:
		print(ed.decode(args.decode))
	except:
		print("Invalid Decoder input.")
# Encode
if(args.encode):
	try:
		encoded_list = ed.encode(' '.join(args.encode))
		print(*encoded_list)
	except:
		print("Invalid Encoder input.")