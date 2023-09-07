def main():
    fileData= open("students.txt",'r')
    students = fileData.readlines()
    fileData.close()
    fileOutput= open("output.txt","a")
        #print(students)
    for s in students:
           #print(s)
        parts=s.split(',')
        gpa =float(parts[3])
        fileOutput.write(parts[1]+"'s GPS is "+str( gpa)+"\n")
        print(gpa)



main()