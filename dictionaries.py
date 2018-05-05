lst = ["A", "B", "C"]

item = {"key": 100}
#dictionary name key
item2 = {"name": "McKenzi"}
print(item["key"])
print(item2["name"])

# dictionay can contain multiple pairs of info

hero = {"name": "Iron Man", "nationality": "United States"}

item3 = {"bag": ["laptop", "usb", "food"], "pocket": [5.00,1.00,"gum"],
"reddit": {"key": [1,2,3,4]}}

print(item3["bag"])
print(item3["pocket"])
print(item3["reddit"]["key"][3])

# activity - info in dictionarie
dictionary = {"name": "McKenzi", "age": 22, "hobbies": ["sleep", "tv", "pizza"], "times": {"Monday": 5, "Tuesday": 6, 
"Thursday": 7}}

print(dictionary["name"])
print(len(dictionary["hobbies"]))
print(dictionary["times"]["Monday"])

for hobbies in dictionary["hobbies"]:
    print(hobbies)
#for times in dictionary["times"]:
    #print(times + " " str(dictionary["times"][times]))
    #print(time + " " + time.)