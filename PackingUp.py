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
    return 


def main():
    boxes = readFile("packing.csv")
    sortList(boxes)
    whereBoxes()


if __name__ == "__main__":
    main()
