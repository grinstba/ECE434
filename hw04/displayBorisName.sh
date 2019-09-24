#!/bin/sh

# Configure LCD
./displayOn.sh

# Make a blank image
SIZE=100x60
TMP_FILE=/tmp/frame.png

# Add text to temp image
convert -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'Brock\nGrinstead' \
     $TMP_FILE
     
# Combine two images into one
composite -geometry +50+100 $TMP_FILE BorisTux.jpg BorisTuxName.jpg

# Show the combined image
sudo fbi -noverbose -T 1 -a BorisTuxName.jpg