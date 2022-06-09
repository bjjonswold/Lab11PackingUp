import csv

#What are these for?
kitchen = []
bathroom = []
livingRoom = []
bedroom = []
locations = ["kitchen", "bathroom", "living room", "bedroom"]
listOfLocations = [kitchen, bathroom, livingRoom, bedroom]


def readFile(fileName):
  with open(fileName) as file:
    boxes = []
    reader = csv.reader(file)
    for line in reader:
      boxes.append(line)
  return boxes

def putAway(box, location = "living room"):
  if location == "kitchen":
    kitchen.append(box)
  elif location == "bathroom":
    bathroom.append(box)
  elif location == "bedroom":
    bedroom.append(box)
  else:
    livingRoom.append(box)
    
def sortList(boxes):
  for box in boxes:
    putAway(box, box[0])
    
def whereBoxes():
  for i in range(4):
    print(locations[i] + ":")
    for box in listOfLocations[i]:
      items = box[3:]
      print(f"{box[2]} -- {items}")
    print()

def maxItems(boxes):
    #student code
    return 
  
def main():
  boxes = readFile("packing.csv")
  sortList(boxes)
  whereBoxes()
  
if __name__ == "__main__":
  main()
