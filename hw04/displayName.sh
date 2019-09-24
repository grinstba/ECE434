#!/bin/sh
./displayOn.sh

# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# Add name to the image
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'Brock\nGrinstead' \
     $TMP_FILE

# Show the created image
sudo fbi -noverbose -T 1 $TMP_FILE