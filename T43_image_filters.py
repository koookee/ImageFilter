#Milestone 2 Image Filters. Team 43, 3/26/2020

from Cimpl import *
#---------------------------------------------------------------------------------------------------------------------------------

def red_filter()->Image:
    '''
    #author: Haoyang Dong 101151946, group 43
    Returns a filtered new image from an original image
    >>>red_filter()
    '''
    
    repeat = True # a boolean variable that makes sure that the program does not quit until the user puts in a proper image
    while repeat: # while loop that runs until the repeat boolean turns to 'False'
        
        file = choose_file() # selects the file that you want to convert
        
        try:  # a try catch that prevents the program from crashing when no image is selected
            image = load_image(file) # tries to load the image file
            show(image)
            
            for i in range(get_width(image)): # a for loop that makes the red filter go through every column
                for j in range(get_height(image)): # a for loop that makes the red filter go through every row
                    set_color(image,i,j,create_color(get_color(image,i,j)[0],0,0)) # for that pixel, reassign the green and blue components to 0 while maintaining the red rgb value
                    
            #show(image) # show the image in a window
            #print(test_filter(image))
            repeat = False # stops the while loop because the image conversion has been completed
            return(image)
            
        except: # if the try catch catches something, the following commands are executed
            print('you didn\'t select a image') 

#---------------------------------------------------------------------------------------------------------------------------------

# Assumption: There should be an image stored in the same folder as this script with the given name
def green_channel(FILENAME:Image)->Image: # function header
    """
    #author: Ajmer Thethy
    Returns a filtered new image from an original image
    >>>green_channel("riveter.jpg")
    """
    original_image = load_image(FILENAME)
    
    # a call statement for the image
    for pixel in original_image:
        
        # uses the pixels in the original photo
       
        x, y, (r, g, b) = pixel
        print (x,y,":", r,g,b)
   
    new_image = copy(original_image) 
    
    #makes a copy of the original image
    
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        new_colour = create_color( 0, g, 0) 
        
        # filters the original image and shows a blue colored poto.
        set_color (new_image, x, y, new_colour) 
        
        # saves the new color to the new image
        
    return new_image

#-----------------------------------------------------------------------------------------------------------------------------

# Assumption: There is an image stored in the same folder as this script with the given name
def blue_channel(FILENAME:Image)->Image: # function header
    """
    # Sara Habib student no: 100960043
    Returns a filtered new image from an original image
    >>>blue_channel("p1-original.png")
    """
    original_image = load_image(FILENAME)# a call statement for the image
    for pixel in original_image:# uses the pixels in the original photo
        x, y, (r, g, b) = pixel
        print (x,y,":", r,g,b)
    
    new_image = copy(original_image) #makes a copy of the original image
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        new_colour = create_color( 0,0,b) # filters the original image and shows a blue colored poto.
        set_color (new_image, x, y, new_colour) # saves the new color to the new image
        
    return new_image

#-----------------------------------------------------------------------------------------------------------------------------

def combine(red_image: Image,green_image: Image,blue_image:Image) -> Image:
    '''
    #author:Hussein El Mokdad
    combines three filters(red,green,blue) to form a new image
    >>>combine(red_image,green_image,blue_image)
    '''
    
    combined_image = copy(red_image)
    for pixel in red_image:
        x, y, (r, g, b) = pixel
        col = get_color(red_image,x,y)
        r,g,b = col
        g = pixel_color(green_image,x,y,"g")
        b = pixel_color(blue_image,x,y,"b")
        new_color = create_color(r,g,b)
        set_color(combined_image,x,y,new_color)
    show(combined_image)
    return combined_image
    

def pixel_color(img:Image,X: int,Y: int,C: str) -> int:
    '''
    #author:Hussein El Mokdad
    returns one of the RGB colors at a specific pixel
    >>>pixel_color(image,23,50,r)
    120
    '''
    if(C == "r"):
        col = get_color(img,X,Y)
        r,g,b = col
        return r        
    if(C == "g"):
        col = get_color(img,X,Y)
        r,g,b = col
        return g
    if(C == "b"):
        col = get_color(img,X,Y)
        r,g,b = col   
        return b    

#--------------------------------------------------------------------------------------------------------------------------------

def two_tone(img: Image, str1: str, str2: str) -> Image:
    '''
    Author:Hussein El Mokdad
    Modifies the pixels in an image to use the RGB values of either 
    one of the colors from the two string parameters. The brightness
    of each pixel determines which color they'll be replaced by.
    If it's less than 128, it'll be replaced by the first color.
    If it's more than 128, it'll be replaced by the second color.
    >>>two_tone(image,"black","white")
    '''
    check_color(str1)
    new_img = copy(img)
    for pixel in new_img:
        x, y, (r, g , b) = pixel
        brightness = (r + g + b) / 3
        if brightness < 128:
            r,g,b = check_color(str1)
            new_color = create_color(r,g,b)
            set_color(new_img,x,y,new_color)
        else:
            r,g,b = check_color(str2)
            new_color = create_color(r,g,b)
            set_color(new_img,x,y,new_color) 
    
    return(new_img)

def check_color(string: str) -> tuple:
    if string == "black":
        return (0,0,0)
    elif string == "white":
        return (255,255,255)
    elif string == "red":
        return (255,0,0)
    elif string == "lime":
        return (0,255,0)
    elif string == "blue":
        return (0,0,255)
    elif string == "yellow":
        return (255,255,0)
    elif string == "cyan":
        return (0,255,255)
    elif string == "magenta":
        return (255,0,255)
    elif string == "gray":
        return (128,128,128)
    else:
        return "Color not found"
#--------------------------------------------------------------------------------------------------------------------------------

def three_tone(img: Image, str1: str, str2: str, str3: Image) -> Image:
    '''
    Author:Hussein El Mokdad
    Modifies the pixels in an image to use the RGB values of either 
    one of the colors from the three string parameters. The 
    brightness of each pixel determines which color they'll
    be replaced by. If it's less than 85, it'll be the 
    first color, between 85 and 171 will be the second
    color, and above 171 will be the third color.
    >>>three_tone(image,"black","white")
    '''
    check_color(str1)
    new_img = copy(img)
    for pixel in new_img:
        x, y, (r, g , b) = pixel
        brightness = (r + g + b) / 3
        if brightness < 85:
            r,g,b = check_color(str1)
            new_color = create_color(r,g,b)
            set_color(new_img,x,y,new_color)
        elif brightness < 171:
            r,g,b = check_color(str2)
            new_color = create_color(r,g,b)
            set_color(new_img,x,y,new_color) 
        else:
            r,g,b = check_color(str3)
            new_color = create_color(r,g,b)
            set_color(new_img,x,y,new_color)            
            
    return(new_img)

#--------------------------------------------------------------------------------------------------------------------------------

def flip_vertical(image: Image) -> Image:
    '''
    Author:Hussein El Mokdad
    Returns an image that's flipped around its vertical y axis. The colors
    of each pixel are swapped with the colors of the respective pixel
    on the opposite side.
    >>>flip_vertical(img)
    '''
    for pixel in image:
        x, y, (r,g,b) = pixel
        x1 = (image.get_width()-1) - x 
        if x<x1:
            temp_color = get_color(image,x,y)
            temp_color1 = get_color(image,x1,y)
            set_color(image,x,y,temp_color1)
            set_color(image,x1,y,temp_color)
    return(image)

#--------------------------------------------------------------------------------------------------------------------------------

def flip_horizontal(image: Image) -> Image:
    '''
    Author:Ajmer Thethy
    '''
    for pixel in image:
        x, y, (r,g,b) = pixel
        y1 = (image.get_height()-1) - y 
        if y<y1:
            temp_color = get_color(image,x,y)
            temp_color1 = get_color(image,x,y1)
            set_color(image,x,y,temp_color1)
            set_color(image,x,y1,temp_color)
    return image

#--------------------------------------------------------------------------------------------------------------------------------

def detect_edge_better (pic:Image,threshold) -> Image:
    """
    Author:Haoyang Dong
    An upgraded version of the edge detection filter, extending from the 
    latter by taking another pixel into consideration when checking the contrast
    between them. This filter aims to modify images to make them look like 
    pencil sketches by changing all pixels to either white or black depending on
    the contrast between pixels. It takes in a image and returns the modified 
    image.
    
    detect_edge_better(image1)
    >>>*shows pencil like version of image1
    
    """    
    threshold = int(threshold)
    
    for i in range(get_width(pic)): # a for loop that makes the filter go through every column
        for j in range(get_height(pic)): # a for loop that makes the filter go through every row
            
            if j == int(get_height(pic))-1 or i == int(get_width(pic))-1: #makes an exception for the right most column and the bottom most row to prevent out of index errors
                result = False
            else:
                result = pixel_contrast(pic,i,j,threshold)
            
            if result: # if the pixel is well contrasted with its surrounding pixels, set that pixel to black, else to white
                set_color(pic,i,j,create_color(0,0,0))
            else:
                set_color(pic,i,j,create_color(255,255,255))
                
    return pic

def pixel_contrast(pic: Image, i: int, j:int,threshold:int) -> bool:
    """ a function that takes in a picture and the coordinate to a specific
    pixel to compare its contrast with other nearby pixels in order to determine
    whether this pixel is contrasted or not as a boolean return.
    
    pixel_contrast(image1, 0,0,30)
    >>>True
    """

    
    
    if abs(sum(get_color(pic,i,j))/3 - sum(get_color(pic,i,j+1))/3) >= threshold or abs(sum(get_color(pic,i,j))/3 - sum(get_color(pic,i+1,j))/3) >= threshold: # checks if the overall brightness of the pixel is different enough compared to the pixel to the right and below it
        return True
    else:
        return False
    
#--------------------------------------------------------------------------------------------------------------------------------

def sepia_filter(pic: Image):
    """ 
    Author:Haoyang Dong
    the sepia filter takes a image, greys it and also adds a yellowish tint to
    it to make it look aged. It takes in a image and returns a modified image.
    
    sepia_filter(image)
    >>>*old looking photo
    
    """
    
    for i in range(get_width(pic)): # a for loop that makes the filter go through every column
        for j in range(get_height(pic)): # a for loop that makes the filter go through every row
            greyed = sum(get_color(pic,i,j))/3
            set_color(pic,i,j,create_color(greyed*1.1,greyed,greyed*0.9)) # for that pixel, assign all of rgb to the same value before raising r by a little and lowing b by a little  
            
    return pic

#--------------------------------------------------------------------------------------------------------------------------------

def extreme_contrast(pic: Image) -> Image:
    """
    Author:Sara Habib
    increase the contrast of a image by setting all rgb value under 127 to 0
    and everything over 128 to 255.
    
    extreme_contrast(image)
    >>>*a very contrasted image
    """
    
    
    for i in range(get_width(pic)): # a for loop that makes the filter go through every column
        for j in range(get_height(pic)): # a for loop that makes the filter go through every row
            r,g,b = get_color(pic,i,j)
            
            if r <128: # checks if it's 0 or 255 that gets assigned to r
                r = 0
            else:
                r = 255
            
            if g < 128: # checks if it's 0 or 255 that gets assigned to g
                g = 0
            else:
                g = 255
            
            if b < 128: # checks if it's 0 or 255 that gets assigned to b
                b = 0
            else:
                b = 255
            
            set_color(pic,i,j,create_color(r,g,b)) # for that pixel, set rgb values to the new contrasted values  
            
    return pic

#--------------------------------------------------------------------------------------------------------------------------------

def posterize(image:Image) -> Image:
    '''
    Author:Ajmer Thethy
    Returns the posterized filtered image.
    >>>posterize(image)
    '''
   
    new_image = copy(image)
   
    for pixel in image:# uses the pixels in the original photo
        x, y, (r, g, b) = pixel
        r1,g1,b1 = _adjust_component(r,g,b)
        new_color = create_color(r1,g1,b1) # new filter to a variable is set
        set_color(new_image, x, y, new_color) #new color is saved on the new copied image of the original    
                    
    return new_image                

def _adjust_component(r:int,g:int,b:int) -> list:
   
    lst=[r,g,b]
    new_list=[]
    for i in lst:
        if 0<=i<=63:
            new_list.append(31)
        elif 64<=i<=127:          
            new_list.append(95)
        elif 128<=i<=191:  
            new_list.append(159)
        elif 192<=i<=255:
            new_list.append(223)
    return new_list

#--------------------------------------------------------------------------------------------------------------------------------

def detect_edges(image: Image, threshold: float)-> Image:
    """
    Author:Sara Habib
    Returns a copy of the original image with a the edge detection filter applied to it which looks like a pencil sketch.
    
    We use a threshold of value=10
    
    >>>detect_edges("p1-original.png",10)
    """
    threshold = int(threshold)
    original_image = copy(image)# a call statement for the image
    for pixel in original_image:# uses the pixels in the original photo
        x, y, (r, g, b) = pixel    
            
    new_image=copy(original_image)
    black=create_color(0,0,0)#sets a variable black to rgb color
    white=create_color(255,255,255)#sets a variable white to rgb color
    
    for y in range (get_height(original_image)-1):
        for x in range (get_width(original_image)):
            (r,g,b)=get_color(original_image,x,y)#  pixel positions 
            (r2,g2,b2)=get_color(original_image,x,y+1)
            contrast=abs((r+g+b)//3-(r2+g2+b2)//3)# calculate the contrast value
            if contrast > threshold:# checks if the conrtast value is greater than the threshold
                set_color(new_image,x,y,black)#the pixel color is set to black when the contrast is high
            else:
                set_color(new_image,x,y,white)#the pixel is set to white when the contrast is low
                
    #show(original_image)
    #show(new_image)
    return (new_image) #returns the new image
    
    
#detect_edges("p2-original.jpg",10)

#--------------------------------------------------------------------------------------------------------------------------------

