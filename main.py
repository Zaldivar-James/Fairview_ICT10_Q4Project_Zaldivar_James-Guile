from pyscript import display, document

#For page 1
#Lists for pre-existing classmates
classmate_list = ["JUSIS!!!", "Paus", "Buggy", "Verg", "Jia", "Xichun"]
sect_list = ["Emerald", "Ruby", "Sapphire", "Topaz", "Jade", "Onyx"]
subj_list = ["PE", "Science", "Math", "Social Studies", "CAT", "ICT"]

class Classmate():
        # Gives the attributes of the class
        def __init__(self, name, section, subject):
            self.name = name # Attribute
            self.section = section # Attribute
            self.subject = subject # Attribute

        # Creates the "introduce" function, which is supposed to display each of the students
        def introduce(self):
            display(f"Hi! My name is {self.name}. I am from the section of {self.section}, and my favorite subject is {self.subject}. Nice to meet you!", target="output1")

def show_classlist(e):
    # Leaves the HTML blank at first. 
    document.getElementById("output1").innerHTML = ""

    student = []

    for i in range(len(classmate_list)):
        student.append(Classmate(
            name=classmate_list[i],
            section=sect_list[i],
            subject=subj_list[i]
        ))

#Introducing each of the students
    for s in student:
        s.introduce()


def student_add(e):
    # Append the values to the list
    classmate_list.append(document.getElementById("name").value)
    sect_list.append(document.getElementById("sect").value)
    subj_list.append(document.getElementById("subj").value)

#For Page 2
import numpy as np
import matplotlib.pyplot as plt

absence_counts = [0, 0, 0, 0, 0]
def show_graph(e):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    selectedday = document.getElementById("day").value
    absences = int(document.getElementById("absences").value)
    dayindex = days.index(selectedday)
    absence_counts[dayindex] = absences

    plt.clf()
    np_days = np.arange(len(days))
    np_counts = np.array(absence_counts)
    plt.title("Absences by Day")
    plt.plot(np_days, np_counts, marker='o')
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Absences")
    plt.grid(True)
    plt.show()