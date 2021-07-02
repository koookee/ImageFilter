#Milestone 3 BatchUI. Team 43, 3/28/2020
#BatchUI by Haoyang Dong and Ajmer Thethy

from T43_image_filters import * 
from Cimpl import * # import the Cimpl image processing library

def execute(f1, f2, filters):
    """
    Author: Ajmer Thethy
    Applies the filters to the image 'f1' and saves it as image f2 after 
    completion of task.
    
    execute('img1.png', 'img2.png', ['E', 'X'])
    >>>
    *you will find img2.png in the same folder as img1.png, but it will have the
    edge detection and extreme contrast filtes applied to it.
    """
    
    
    img = load_image(f1)
    
    for i in filters: #goes through every single filter that the filters list contains
        
        if i == '2': #check if two-tone filter should be applied
            img = two_tone(img, 'yellow', 'cyan')
            
        elif i == '3': #check if three-tone filter should be applied
            img = three_tone(img, 'yellow','magenta','cyan')
            
        elif i == 'X' or i == 'x': #check if the extreme contrast filter should be applied
            img = extreme_contrast(img)
            
        elif i == 'S' or i == "s": #check if the sepia filter should be applied
            img = sepia_filter(img)

        elif i == 'P' or i == "p": #check if the posterize filter should be applied
            img = posterize(img)

        elif i == 'E' or i == "e": #check if the edge detection filter should be applied
            img = detect_edges(img, 10)

        elif i == 'I' or i == "i": #check if the better edge detection filter should be applied
            img = detect_edge_better(img, 10)

        elif i == 'V' or i == "v": #chekc if the vertical flip filter should be applied
            img = flip_vertical(img)

        elif i == 'H' or i == "h": #check if the horizontal flip filter should be applied
            img = flip_horizontal(img)
                
    show(img)

    save_as(img,f2) #saves the image as desingated


def main():
    """
    Author: Haoyang Dong
    
    The main body function of the batchUI, it prompts the user for a txt file 
    and reads the contents of that txt file for instructions on img manipulations
    
    
    """
    
    repeat = True # a boolean variable that makes sure that the program does not quit until the user puts in a proper txt file
    while repeat: # while loop that runs until the repeat boolean turns to 'False'
        
        filename = input('what file do you want to open, only txt files accepted: ')
        
        try:  # a try catch that prevents the program from crashing when an incorrect file is selected
            file = open(filename)
            
            for line in file: # a for loop that goes through every line in the txt file
                counter = 0
                img1_name = ''
                img2_name = ''
                filters = []
                spaces = []
                
                for char in line: # a for loop that goes through every character on the above mentioned line
                    
                    if img1_name == '' and char == ' ' : # takes in the first object by finding the space character that came after that object
                        img1_name = line[0:counter]
                        spaces.append(counter)
                        
                    elif img2_name == '' and char == ' ': # takes in the second object by finding the second space character
                        img2_name = line[spaces[0]+1: counter]
                        spaces.append(counter)
                        
                    elif char == ' ': # all other space characters will be preceed by a filter command
                        filters.append(line[counter-1])
                        
                    if counter == len(line)-2: # a special case for the last filter command since it won't have a space after it
                        
                        if line[len(line)-1] == '\n': # if there are multiple lines in the file, the end character on a line will actually be '\n', this checks if that is the case and corrects it
                            filters.append(line[len(line)-2])
                            
                        else:
                            filters.append(line[len(line)-1]) 
                    
                    counter+=1

                execute(img1_name, img2_name, filters)
                
            repeat = False # stops the while loop because the image conversion has been completed
            file.close() # closes the file
            
        except: # if the try catch catches something, the following commands are executed
            print('you did something wrong there') 
         
         
if __name__ == "__main__": # runs the main body function only if this file is ran, not if it gets imported to another file
    main()
    
