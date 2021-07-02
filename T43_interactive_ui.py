# Team 43
# Milestone 3, Interactive UI
# Submission date: 2 April 2020
# Authors: Hussein El Mokdad and Sara Habib

from Cimpl import *
from T43_image_filters import *

input_prompt1="L)oad image  S)ave-as \n2)-tone 3)-tone  X)treme contrast "  
input_prompt2="T)int sepia  P)osterize\nE)dge detect  I)mproved edge detect " 
input_prompt3="V)ertical flip  H)orizontal flip\nQ)uit\n: "
input_prompt = input_prompt1 + input_prompt2 + input_prompt3
#Makes the code look more readable than putting them all in one line

def is_x_in_list(x: str) -> bool:
    '''
    Checks to see whether the user input exists as a command.
    
    >>>is_x_in_list("t")
    True
    >>>is_x_in_list("J")
    False
    '''
    lst = ["2","3","x","X","t","T","p","P","e","E","i","I","v","V","h","H"]
    for i in lst:
        if i == x:
            return True
    return False


def load_the_image() -> Image:
    '''
    Shows and retuns the selected image from the dialog box
    >>>load_the_image()
    '''
    #The dialog box for choosing a file will be behind Wing
    #Minimze Wing to be able to select a file
    image = load_image(choose_file())
    show(image)
    return image  

def filter_the_image(x:str,image: Image) -> Image:
    '''
    Depending on what filter the user calls, the returned image
    will be filtered and shown to the user.
    
    >>>filter_the_image("v",image)
    
    >>>filter_the_image("E",image)
    threshold? 30
    
    '''
    if x=="V" or x=="v":
        picture = flip_vertical(image)
        show(picture)
    elif x=="H" or x=="h":
        picture = flip_horizontal(image)
        show(picture)
    elif x=="X" or x=="x":
        picture = extreme_contrast(image)
        show(picture)    
    elif x=="T" or x=="t":
        picture = sepia_filter(image)
        show(picture)
    elif x=="P" or x=="p":
        picture = posterize(image)
        show(picture)    
    elif x=="E" or x=="e":
        threshold = input("Threshold?: ")
        picture = detect_edges(image, threshold)
        show(picture)  
    elif x=="I" or x=="i":
        threshold = input("Threshold?: ")
        picture = detect_edge_better(image, threshold)
        show(picture)
    elif x == "2":
        color1 = input("Please enter the first color: ")
        color2 = input("Please enter the second color: ")
        picture = two_tone(image,color1,color2)
        show(picture)
    elif x == "3":
        color1 = input("Please enter the first color: ")
        color2 = input("Please enter the second color: ")
        color3 = input("Please enter the third color: ")
        picture = three_tone(image,color1,color2,color3)
        show(picture)    
    return picture
    

switch = True #Interface will keep looping until user presses Q or q
image_loaded = False #Image hasn't been selected yet

while switch:
    
    x=input(input_prompt)
    print("")
    
    if x=="L" or x=="l":
        image = load_the_image()
        image_loaded = True     
        
    elif image_loaded and is_x_in_list(x):   
        image = filter_the_image(x,image)       
        
    elif x == "Q" or x=="q":  
        switch = False   
        
    elif is_x_in_list(x) and not(image_loaded):
        print("No image loaded \n")  
        
    elif x == "S" or x == "s":
        save_as(image)
        
    else:
        print("No such command \n")
    
 




    
    