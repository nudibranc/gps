# gps time matcher
## Tested on python 3.6, to run, run this command in the directory containing all relevant files:
python gps.py
## Metadata in sample.txt
## Other data in platform.txt
### Change constants in python script if you change the txt file names
### Only accurate to the second
### Assumed you have exiftools https://exiftool.org/ 
### To generate metadata run this command in the directory:
exiftool -filename.jpg > sample.txt
