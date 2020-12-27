your_name =  "Ayşenur"
your_surname = "Akbaba"

input_test = 0
while True:

    if input_test < 3 :
        name_input = str ( input ( "Your Name: " ) )
        surname_input = str ( input ( "Your surname: " ) )

        if ( name_input != your_name and surname_input != your_surname):
            print( "Your name and surname are uncorrect. Try again \n" )
        elif ( name_input != your_name and surname_input == your_surname):
            print ( "Your name is uncorrect. Try again \n" )
        elif ( name_input == your_name and surname_input != your_surname):
            print ( "Your surname is uncorrect. Try again \n" )
        elif ( name_input == your_name and surname_input == your_surname):
            print("WELCOME \n")

            print( "Please write your lessons")

            lessons = []

            lesson_input1 = str ( input ( "Lesson 1: \n " ) )
            lesson_input2 = str ( input ( "Lesson 2: \n " ) )
            lesson_input3 = str ( input ( "Lesson 3: \n " ) )
            lesson_input4 = str ( input ( "Lesson 4: \n " ) )
            lesson_input5 = str ( input ( "Lesson 5: \n " ) )

            lessons.append ( lesson_input1 )
            lessons.append ( lesson_input2 )
            lessons.append ( lesson_input3 )
            lessons.append ( lesson_input4 )
            lessons.append ( lesson_input5 )

            null_point = lessons.count("")

            if null_point > 2 :
                print( "You should write at least 3 leassons " )
                break
            else :

                print ( lessons )
                print(" Please write the lesson you want to calculate \n ")

                grade_lesson = str ( input ( "Lesson: \n " ) )

                if grade_lesson in lessons :

                    midterm = input ( "Midterm Exam: " )
                    final = input ( "Final Exam: " )
                    project = input ( "Project Exam: " )

                    try :
                        midterm_int = int ( midterm )
                        final_int = int ( final )
                        project_int = int ( project )

                    except ValueError as error:
                        print ( "Error!!!" )


                    calculation = {"Midterm": 30 , "final": 50 , "Project" : 20 }
                    print( calculation)

                    grade = ( ( midterm_int * 30 ) / 100 ) + ( ( final_int * 50 ) / 100 ) + ( ( project_int * 20 ) / 100 )

                    print(grade)

                    if (grade > 90 and grade <= 100):
                        print ( "AA" )
                    elif (grade > 70 and grade <= 90):
                        print ( "BB" )
                    elif (grade > 50 and grade <= 70):
                        print ( "CC" )
                    elif (grade < 50 and grade >= 30): \
                            print ( "DD" )
                    elif (grade < 30 and grade >= 0):
                        print ( "FF  -  FAIL" )
                    else:
                        print ( "INVALID NOTE" )
                else:
                    print( "Please check " )

        input_test += 1

    else:
        print ( "Please try again later \n" )
        break
