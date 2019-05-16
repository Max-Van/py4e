class Student :
    StudentNumber=0
    StudentName=''

    def set_StudentNumber(self,stunum) :
        self.StudentNumber=stunum

    def set_StudentName(self,stuname) :
        self.StudentName=stuname

    def get_StudentNumber(self,stunum) :
        return self.StudentNumber

    def get_StudentName(self,stuname) :
        return self.StudentName


student1 = Student ()

student1.StudentNumber=1
student1.StudentName='max'

print (student1.StudentNumber)
print (student1.StudentName)
