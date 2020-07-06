# Data Encoder

Python Version: 3.x

### Instructions to run
```
python main.py [-h] [-e string [string ...]] [-d int [int ...]]
optional arguments:
  -h, --help                                              Help message
  -e string [string ...], --encode string [string ...]    Pass string to encode.
  -d int [int ...], --decode int [int ...]                Pass array of integers to decode.
```

### Encoder
Encodes strings by taking 4 characters at a time and returns an array of encoded integers representing original string.

### Decoder
Decodes an encoded integer array and returns the original string.
