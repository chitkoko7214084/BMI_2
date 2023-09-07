def main():
    finalExamScores =[100, 82, 93, 81, 55, 72]
    finalExamScores= {
        "Alice":100,
        "BoB":82,
        "Carol": 81,
        "Dave" :81,
        "Eve" :55,
        "Frank":72,
    }
    #print(finalExamScores["Eve"])
    finalExamScores["Eve"]=57
    #print(finalExamScores["Eve"])

   # for key,value in finalExamScores.items():
       # print(value)
    #for v in finalExamScores.values():
        #print(v)
    #for k in finalExamScores.keys():
        #print(k)






    alice={
        "firstNane":"Alice",
           "LastName":"Smith",
           "major": "Chemistry",
           "gpa":3.92,
           "courses": ["CS 120", "CS 124", "MATH 165"]
        }
    bob={
        "firstNane":"bob",
           "LastName":"Jones",
           "major": "Physics",
           "gpa":3.3,
           "courses": ["CS 222", "CS 124", "MATH 166"]
        }
    
    print(alice["courses"][2])
    for c in bob["courses"]:
        print(c)




main()