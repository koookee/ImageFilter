ReadMe for Picture Filter version 1.0 4/6/2020
Copyright 2020 Hussein El Mokdad, Ajmer Thethy, Sara Habib, and Haoyang Dong

Contact info:
Email: husseinelmokdad@cmail.carleton.ca
Phone: +1 (343) 111-1111



Installation:
_____________


Python 3.8 or later must be installed.

Following external modules are used:

-Cimpl (Carleton Image Manipulation Python Library) version 1.04 or later.

-T43_image_filters version 1.0 or later.

Optional: Install and use Wing 101 version 7.1 or later.


Description:
____________



- The project contains a program that prompts the user to load an image. The user can choose the type of filter.
 After each filter the result is shown and the user can apply other filters if desried. Upon completion, the user
 can save the image and quit at any time. 



- The project is made up of three files:



T43_image_filters        T43_interactive_ui       T43_batch_ui




Usage:
______

For version 1.0

> python T43_batch_ui.py

Before running the program, the user must ensure that the 'T43_image_filters.py' file, 
'Cimpl.py' file, the desired command txt file, and the desired images are in the same folder
as the batchUI file. Otherwise, the program will crash due to import errors. Once the batchUI
file is executed, the user will be prompted for a command txt file. Simply type in the full name 
of the file, including the '.txt' at the end and hit enter. The command txt should be structured
properly and written with the appropriate syntaxes; if anything is amiss with the command txt
file, the batchUI will inform the user that there was something wrong and asks for a txt file again.
The proper way of writing a command txt file is the following...

"the full name of the image you want to modify, complete with file type" *space* "the full name of what the modified image should be saved as, complete with file type" *space* "filter type" *space* "filter type"...

The above mentioned filters types are single letters or numbers that represent what image 
manipulation techniques are to be used on the original image. 2 means two-tone, 3 is three-
tone, x or X for extreme contrast, s or S for sepia tint, p or P for posterization, e or E
for normal edge detection, i or I for improved edge detection, v or V for vertical flip, and
finally h or H for horizontal flip. Each line in the txt file is for modifying one image, so 
it is possible to modify several images at once if you have multiple lines of commands. You
will be able to find the end products inside the same folder as the original images under 
the new names you assigned to them in the command txt file if everything was done correctly.

For version 1.0

> python T43_interactive_ui.py

Ensure that the T43_interactive_ui file is in the same directory as the Cimpl file. The reason behind this is
because the program imports functions from both these files. Upon the execution of the program, the user will
have multiple commands to choose from. The user is supposed to load an image first by entering "l" or "L" 
(Commands are not case sensitive). If the user tries to apply a filter without loading an image first, they'll 
be prompted with the "No image loaded" error message. Once the user selects an image, they can apply any of the
filters shown on the screen by calling their respective commands. Keep in mind that the image modification does 
stack with multiple filters. If the user is satisfied with the image, they can save it using the built in save command.

All commands should be visible when the user runs the programs. 

Credits:
________

Hussein El Mokdad, author for: 
-T43_interactive_ui: is_x_in_list, load_the_image, filter_the_image
-T43_image_filters: combine, two_tone, three_tone, flip_vertical

Haoyang Dong, author for:
-T43_batch_ui: main
-T43_image_filters: red_filter, detect_edge_better, sepia_filter

Ajmer Thethy, author for:
-T43_batch_ui: execute
-T43_image_filters: green_channel, posterize, flip_horizontal

Sara Habib, author for:
-T43_image_filters: blue_channel, detect_edges, extreme_contrast
