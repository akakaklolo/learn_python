file_conunts={"jpg":10,"txt":14,"csv":2,"py":23}#"vòng lặp cho Dictionary: "jpg= là 1 tuple, : 10 là 1 value "
for extension in file_conunts:
    print(extension)
for ext, amout in file_conunts.items(): # "dung Iteams để truy cập vào giá trị (value) của 1 tuple trong dictionary"
    print("there are {} file with  the .{} extension ".format(amout,ext))
    print( file_conunts.keys())#"truy cập vào các phần tử trong dictionary"
    print( file_conunts.values())#"truy cập vào các giá trị của phần tử trong dictionary"
    
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animails, sound_animail in cool_beasts.items():
    print("{} have {}".format(animails,sound_animail))
#"thêm value vào keys"
def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for guest in guest_list: # Iterate over the elements in the list 
        result[guest]=0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}    