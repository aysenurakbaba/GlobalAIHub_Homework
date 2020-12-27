name = str (input ( "Your Name: " ))
surname = str (input ( "Your surname: " ))
age = int (input ( "Your age: " ))
birth_year = int (input ( "Your date of birth(just year): " ))


if( age< 18 ) or birth_year < 2002 :
    print("Ypu can't go out")
else:
    print( " Ypu can go out" )