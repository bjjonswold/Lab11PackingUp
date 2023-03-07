'''
1. The variables at the top are to initialize objects that will be 
used to store lists later on.
2. It will go through a max of two other functions before returning to Main
3. SortList(boxes) uses another funciton putAway() to place the box in the
correct location. 
4. This declaration is stating what the location variable is equal too in the
function call itself, instead of calling it from elsewhere. 
5. Some uses of defaults include:
    A. Avoiding errors - a function will always have a parameter
    work with, even if it isn't declared in the call
    B. Simplifies calling arguments - you don't need to call the same
    parameter every time
You can call this funciton with the default by writing:
someFunction(arg1) 
'''

import csv

# What are these for?
kitchen = []
bathroom = []
livingRoom = []
bedroom = []
locations = ["kitchen", "bathroom", "living room", "bedroom"]
listOfLocations = [kitchen, bathroom, livingRoom, bedroom]

#input: fileName -- a string with  the name of a file
#output: a list of lists where each item is a separate string based on the commas in the file
def readFile(fileName):
    with open(fileName) as file:
        boxes = []
        reader = csv.reader(file)
        for line in reader:
            boxes.append(line)
    #print(f'Testing boxes: {boxes}')
    return boxes



#input: box-- a single list from the list of lists, location-- where the item should be stored
#output: locations now have appropriate boxes
def putAway(box, location="living room"):
    if location == "kitchen":
        kitchen.append(box)
    elif location == "bathroom":
        bathroom.append(box)
    elif location == "bedroom":
        bedroom.append(box)
    else:
        livingRoom.append(box)

#input: list of lists
#outptut: boxes are sorted
def sortList(boxes):
    for box in boxes:
        if (box[0] == "unknown"):
            putAway(box)
        else:
            putAway(box, box[0])

#input: nothing
#output: prints each room and what boxes are there and what they have inside
def whereBoxes():
    for i in range(4):
        print(locations[i] + ":")
        for box in listOfLocations[i]:
            items = box[3:]
            print(f"{box[2]} -- {items}")
        print()

#input: list of lists
#output: maximum amount of items in any box
def maxItems(boxes):
    #student code
    max_value = max([int(row[1]) for row in boxes])
    print(f'Testing max value: {max_value}')
    return max_value

boxes = readFile("packing.csv")
print("TESTING", maxItems(boxes))

def main():
    boxes = readFile("packing.csv")
    sortList(boxes)
    whereBoxes()
    maxItems(boxes)


if __name__ == "__main__":
    main()
