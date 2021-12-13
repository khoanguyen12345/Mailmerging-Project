# Mailmerging-Project
This project aims to help the MUN team with mailmerging. It takes in a .csv file and outputs a .pdf that contains the mailmerged result of all the names in the .csv file. There are 3 modes for either nametags, certificates or labels.

Updates:
- Bug fixes are now done! (please tag any bugs if you find any)
- This program has been ported to MacOS. I no longer have access to a Windows computer so I cannot test the program on Windows.
- mac-version made default branch and main will be fixed when I get my Windows laptop back (June 2022)
- JUST IN TIME FOR MUN!


How to use:
1. Insert .csv file
2. Enter in the fields of the user interface (use <> when mentioning fields in .csv file)
3. Press Browse and search for nametags/labels/certificates (samples included in localresources folder)
4. If font size or positioning needs to be changed, see new preview by pressing update preview button
5. Press Save As PDF
6. Look inside the folder containing app.py. The pdf should be there.

Notes:
- localresources folder has designs for nametags/labels/certificates and a CSV so you can easily test the program
- Many thanks to official tkinter documentation, PIL documentation and StackOverflow for pointing me in the right direction!
