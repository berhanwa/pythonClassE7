courses = {
    "CSCI-E7" :
    { "full_name" : "Intro to CS with Python",
        "instructors" : [ "Henry", "Foobar" ],
        "TAs" : ["Alyssa", "Apekshya", "Ben",
        "Arpit", "Stephen"],
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

def total_homeworks(course):
    for i in course:

