# Generate random input file for data source
# Make a HashFunction HashID()
#import random

#GLOBAL DECLARATIONS BELOW
CGPA=[] #Values
StuIDs=[] #Keys    
Courses={"CSE":200, "MSE":101, "ARC":303, "ECE":405}
StudentHashRecords = [[] for _ in range(len(StuIDs))]

def main():
#CODE BELOW TO READ THE INPUT FILE AND GENERATE TWO LISTS (1 OF KEYS AND OTHER OF VALUES)
    #CGPA=[] #Values
    #StuIDs=[] #Keys
    with open("inputPS4.txt","r") as f:
        content=f.readlines()
        for x in content:
            row=x.split("/")
            StuIDs.append(row[0])
            subrow=row[1].split()
            CGPA.append(float(subrow[0]))
    f.close()
   
 #INITIALIZE HASH TABLE
    StudentHashRecords=initializeHash()
     
   
#POPULATING THE HASH TABLE - With Collision Handling by CHAINING
  #POPULATING THE HASH TABLE - With Collision Handling by CHAINING
    for i in range(0,len(StuIDs)):
       insertStudentRec(StudentHashRecords,StuIDs[i],CGPA[i])
            
       
    with open("promptsPS4.txt","r") as f:
        content=f.readline()
        str=content.split(':')
        ThresholdCGPA=float(str[1])
        hallOfFame(StudentHashRecords,ThresholdCGPA)
    f.close()
   
   
    
# FUNCTION 1
def initializeHash():
    #CODE BELOW TO CREATE HASH TABLE AND DO HASHING 
    #Hash table created below for chaining (Points to Null and is of ideal size of StudentIDs array)
    StudentHashRecords = [[] for _ in range(len(StuIDs))]
    return StudentHashRecords

# FUNCTION 2
def insertStudentRec(StudentHashRecords,studentId,CGPA):
     # HASHING INVOKED BELOW FOR EACH STUDENT ID AND HASHTABLE BUCKET IDENTIFIED
    StudentHashedkey=HashID(studentId)
    Bucket=StudentHashRecords[StudentHashedkey]
    Bucket.append((studentId,CGPA))
 
# FUNCTION 3 HALL OF FAME
def hallOfFame(StudentHashRecords,CGPA):
    numbereligible=0
    f=open("outputPS4.txt","w+",1)
    Student_list = []
    g=open("testPS4.txt","w+",1)
    f.write("---------- hall of fame ----------" + "\n" "Input: "+ str(CGPA) + "\n") 
    for Bucket in StudentHashRecords:
        if len(Bucket) !=0:
            for kvpair in Bucket:
                k=kvpair[0] #StudID values
                v=kvpair[1] #CGPA values
                if v>CGPA:
                    numbereligible=numbereligible+1 
                    g.write(k+"/"+ str(v)+ "\n")                    
    f.write("Total eligible students:" + str(numbereligible)+ "\n")   
    f.write("Qualified students:" + "\n")
    fin=open("testPS4.txt","r")
    data=fin.read()
    fin.close()
    f=open("outputPS4.txt","a")
    f.write(data +"--------------------------------------")
    

# FUNCTION 4 DEFINITION OF NEW COURSE LIST
def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    students=0
    f=open("outputPS4.txt","w+",1)
    f.write("---------- new course candidates ----------" + "\n" "Input: "+ str(CGPA) + "\n") 
    
    
    
# FUNCTION 5 NEW COURSE LIST
def HashID(key):
    TotValue=0    
    #for i in range(0,len(key)):
    #    TotValue=TotValue+ord(key[i])
    for i in range(0,4):
        TotValue=TotValue+int(key[i])
    CourseName=key[4:7]
    CourseValue=Courses[CourseName]
    #TotValue=TotValue*CourseValue
    for i in range(7,11):
        TotValue=TotValue+int(key[i])
    TotValue= TotValue+CourseValue
    AssignedBucket=(int(TotValue) % len(StuIDs))    
    return AssignedBucket





#MAIN CALLER - IGNORE 
if __name__ == "__main__":    
      
    main()







