courses = {
    "CSCI-E7" :
    { "full_name" : "Intro to CS with Python",
        "instructors" : [ "Henry", "Foobar" ],
        "TAs" : ["Alyssa", "Apekshya", "Ben","Arpit", "Stephen"],
        "num_homeworks" : 7,
        "num_exams" : 2
    },

    "FREN-E-1b" :
    { "full_name" : "Elementary French I",
        "instructors" : [ "Taieb" ],
        "tfs" : ["Gloria", "Mona"],
        "num_homeworks" : 12,
        "num_exams" : 2
    }
}

def total_homeworks(course_list):

    # Initialized this variable to set the stage
    total_work = 0

    # Used a for loop to iterate through the keys of the course_list dictionary, with i representing each course
    for i in course_list:

        # The 'num_homeworks' keys' values are collected and then added on to total_work variable, which lets us know how much homework there is to do
        total_work += course_list[i]['num_homeworks']

    return total_work


def total_homeworks2(course_list):

    # Created a new list using list comprehension that finds the number of 'num_homeworks' by iterating through course_list
    newlist = [course_list[i]['num_homeworks'] for i in course_list]

    # Then used the sum function to add newlist up and assign them to the total_work variable
    total_work = sum(newlist)

    return total_work


# Results of both functions shown below
def main():
    print(total_homeworks(courses))
    print(total_homeworks2(courses))
main()
