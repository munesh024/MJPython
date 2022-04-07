from PIL import Image, ImageDraw,ImageFont

def image_processing(data) :
    img = Image.open("D:\python_assignment_22\empty.jpeg")            #path of the image file
    d = ImageDraw.Draw(img)
    width_size = img.size[0]/2-130                            #image width size where text has to be inserted
    height_size = img.size[1]/2-60                            #image height size where text has to be inserted
    fnt= ImageFont.truetype("segoeuib.ttf",32)                #Text font type and its font size
    d.text((width_size,height_size),data, font=fnt ,fill=(0,0,0))   
    img.save('updated.png')                                   #saving the image with the specified name    
    return None 
    

print("enter the string to write into the image")
data = input("enter now\t")
while True :
    if len(data)>39 :
        print("\n")
        print("*"*64)
        print("* length of the string is too long to fit into the given space *".upper())
        print("*"*64)
        print("\n")
        print("enter the string to write into the image")
        data = input("enter now\t")
        continue
    else :
        image_processing(data.title())
        print("\nData inserted into the image successfully".upper())
        break