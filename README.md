# Volume-widget
Volume widget is a program, which shows system volume levels.

The program needs pulseaudio, alsa-utils, python3 and python-pyqt5 as dependencies. Note that dependencies might be different depending on your distribution.

#Volume widget Copyright (c) 2017 JJ Posti <techtimejourney.net>
#Volume widget comes with ABSOLUTELY NO WARRANTY;
#for details see: http://www.gnu.org/copyleft/gpl.html.
#This is free software, and you are welcome to redistribute it under
#GPL Version 2, June 1991″

Here are some screenshots
_____
![silence x16266](https://user-images.githubusercontent.com/29865797/29626067-3fe0f57e-8836-11e7-9475-3c510c5e9ad5.jpg)
____
![medvolume](https://user-images.githubusercontent.com/29865797/29626078-4c6f3db4-8836-11e7-8303-a71dc2779f5f.jpg)
______
![warning x16266](https://user-images.githubusercontent.com/29865797/29626095-59a1b5fc-8836-11e7-8310-e4f11d50c504.jpg)
_____

By default I have set Volume widget to a fixed position. If the position I have chosen does not work for you, then look at the code and change the coordinates. As always, the code is commented and easy to follow.  I have also set Volume widget to ignore the close event. ALT+F4 will not work by default.  If you need that functionality then comment out these lines

#Ignore ALT+F4. We want to avoid accidental closing. </br>
def closeEvent(self, event): </br>
event.ignore()
_____

Executing:

After downloading, decompress the archive and cd into the resulted  directory.

If needed, make files executable:

chmod +x filename.py

OR

chmod +x filename.sh

Run with: python filename_location.py
_____________
Original entry is at: http://www.techtimejourney.net/volume-widget-is-released/
