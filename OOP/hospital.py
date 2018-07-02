class Patient(object):
    def __init__(self, idx, name, allergies):
        self.id = idx
        self.name = name
        self.allergies = allergies
        self.bed_number = None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.bed_number = []
        self.population = len(self.bed_number)
    def admit(self, patient, number):
        if self.population == self.capacity:
            patient.bed_number = None
            print "Hospital is full"
            print (str(patient.name), " can't come in.")
        else:     
            self.patients.append(patient.name)
            self.bed_number.append(number)
            self.population = len(self.bed_number)
        return self
    def discharge(self, patient):
        the_id = self.patients.index(patient.name)
        self.patients.pop(the_id) 
        patient.bed_number = None
        self.bed_number.pop(the_id)
        self.population = len(self.bed_number)
        return self
    def info(self):
        print("Hospital Name is "+ self.name)
        print("Population is "+ str(self.population))
        print("Patients are: "+ str(self.patients))
        print("Occupied beds are: " + str(self.bed_number))

hospital1 = Hospital("Nana", 2)
hospital2 = Hospital("Awesome", 150)

patient1 = Patient(64512, "Martin", ["Kevin","Jeff"])
patient2 = Patient(12345,"Andre", ["stuff", "nice"])
patient3 = Patient(73911,"Alex", ["alle"])
patient4 = Patient(56283, "Sonia", ["quee", "bop", "lan"])
patient5 = Patient(57940, "Mustafa", [])

hospital1.admit(patient1, 112).admit(patient2,114).info()
print
hospital1.admit(patient3, 115)
print
hospital1.info()
print
hospital1.discharge(patient2).info()
print
hospital2.admit(patient2,221).admit(patient4,222).admit(patient5,223).info()


