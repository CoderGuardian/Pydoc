def School(Class, *Student,**Subjects):
    print("Subjects Selection in Standard :", Class)
    for arg in Student:
        print("Student :", arg)
        for key, value in Subjects.items():
            print("\t%s == %s" % (key, value))
 
 
School('Aayush', 'Tom', 'Sass', 'Pat', First='Maths', Second='Physics', Third='Chemistry')
School('Pankaj', 'Aashu', 'Harsh', 'Harry', First='Accounts', Second='Economics', Third='Maths')