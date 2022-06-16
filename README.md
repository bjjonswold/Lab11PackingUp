# Lab11PackingUp
complex data: lists within lists, etc (warmup)

# In PackingUp.py is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input.

Note: The format for each list is as follows: \[location, number of items, name of box, item, item, item...]

# Step One
Answer the following questions about the code provided as comments in the code:
1. After reading the code, what do you think the purpose of the variables at the top is? Where are they used?
2. Code trace for main. What is the highest number of functions that it goes through before getting back to main?
3. How does sortList(boxes) use other functions to simplify the work?
4. What is happening in the putAway() declaration? What is location = "living room"?
5. What are some uses of defaults and how would we call something like someFunction(arg1, arg2 = "default") if we want to use the default?

# Step Two: Coding: maxItems(boxes)
Find the function `maxItems(boxes)`. Code maxItems(boxes) such that it returns the maximum number of items any of the boxes has.

**NOTE: There is an entry that has the number of items in the box**
```
For example, if we used the list from reading "packing.csv", we should get 7.
```
# Step 3: Test maxItems(boxes)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().
```python
boxes = readFile("packing.csv")
print("TESTING", maxItems(boxes)) 
```
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Lists of Lists
Like in this lab, lists of lists are a lot like boxes in boxes. If it helps to visualize them as actual lists, picture your notes or powerpoints where you may have a big header (the outer list) and beneath it have several sub-headers (the inner lists) with information under them (the data in the inner lists). Because of this, in order to index into these lists, we have to go through each layer of list, like opening one box and then another. 

For example, with the list 
```python
lst = [[1, 2, 3], [4 , 5, 6]]
```
In order to index to 5, we would index it like this: 
```
lst\[1]\[1] or (lst\[1])\[1]
```
To read it left to right, we are getting the list in lst at index 1 (\[4, 5, 6]) and then getting the item in that list at index 1 (5).

# Reminder on Finding the Max
When writing your function for finding the max, picture yourself being told a series of numbers with a  blindfold on. You don't know how many numbers are left, nor do you know if the number you currently think is the max is the true max **until you reach the end**. Finding the max with a computer is the same way. We will only know the current max out of what we have seen so far at any given moment. As such, you will likely need a variable that updates with whatever the new current max is.
