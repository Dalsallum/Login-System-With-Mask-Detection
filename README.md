# Login-System-With-Mask-Detection
Python code for Login system for employees that is connected to database. The code will check if the employee is wearing a mask or not.




In this code I used tkinter for GUI which will ask the user for his information ( id and password ).
I created a database with small table containing employee information : id, first name , last name and password .
the program will check the user input with the database, if correct it will welcome the employee and then turn on the camera to detect the mask.
If he is wearing a mask, then it will thank him for wearing the mask ( logged in ) then the program will exit. 
if not wearing a mask then the program will warn him to wear a mask then will exit so he can run it again.


There is an option ( Login as Admin )  which only the admin can login with it (specific ID and password ).
This option will log the admin to the admin window, from the admin window the admin can write sqlite code to alter the database.

For mask detection I used the code and model Balaji provided ( many thanks to him ) :

https://github.com/balajisrinivas/Face-Mask-Detection

https://www.youtube.com/watch?v=Ax6P93r32KU&t

I altered his code to suit mine.

The videos you will see are 1.5x faster, the camera launch is slow so I increased the speed of the videos.

Please if you have any questions regarding the code you can reach out to me through my email.
