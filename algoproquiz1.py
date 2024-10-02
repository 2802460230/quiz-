class Binusmaya:
    def __init(self):
        self.Lecturers = []
        self.Classes = []
        self.Schedules = []

    def SetLecturers(self):
        LecturerName = input(str("Give LecturerName"))
        LecturerSubj = input(str("Give LecturerSubj"))
        LecturerID = input(str("Give LecturerID"))

        Lecturer = {"name" : LecturerName, "LecturerSubj" : LecturerSubj, "LecturerID" : LecturerID}
        Flag = True
        for x in range(len(self.lecturers)):
            for y in range(3):
                if self.Lecturers[x][y] == Lecturer[y]:
                    print("Denied")
                    Flag = False

        if Flag == True:
            self.Lecturers.append(Lecturer)

    def RemoveLecturers(self):
        LecturerID = input("Give LecturerID?")
        for x in range(len(self.Lecturers)):
            if LecturerID == self.Lecturers[x][2]:
                self.Lecturers.pop(x)
    
    def SetClass(self):
        Flag = True
        ClassCode = input("Give Class")
        for x in range(len(self.Classes)):
            if ClassCode == self.Classes[x]:
                Flag = False

        if Flag == True:
            self.Classes.append(ClassCode)

    def RemoveClass(self):
        Classcode = input("Give Class")
        for x in range(len(self.Classes)):
            if Classcode == self.Classes[x]:
                self.Classes.pop(x)

    def SetSchedule(self):
        Classcode = input("Give Class")
        Time = input("Give Time")
        Subj = input("Give Subject")
        for x in range(len(self.Lecturers)):
            if Subj == self.Lecturers[x][1]:
                LecturerName = self.Lecturers[x][0]
        Tuple = (Time,Classcode,Subj,LecturerName)
        self.Schedules.append(Tuple)

            





