## <ins>**Script**</ins>
**1. Web Form Validation:**
Index.html sets up a webpage with the title Register. Inside the head section, it links to two files, Script.js and Style.css. 

Inside the body, the HTML has two sections. The first one, called formdiv, is where the registration form that the user interacts with is located. The top is a heading called register, followed by the actual form. The form has 4 parts. The first is for the name, then the email, then the date of birth and finally the password.

Below the form is a second division called infoDiv. The section starts hidden, and it displays the user's information after the form has been successfully filled out and checked

In the JavaScript file, there is a function called submitform, which stops the default action of refreshing the page. 

The function then reads the values from all four input boxes using their IDs. The name and email are cleaned with the trim method, which stops errors from accidental spaces.

The script then checks the fields. It first checks that none of the fields are left empty, then it checks if the email is in the correct format with an @ symbol and a dot. After that, the password is checked to see if it is eight characters long and contains at least one letter and one number. If all validation passes, the formdiv becomes hidden and infodiv becomes visible, showing the user's information. 

In the CSS file, the body of the page is centred with the form in a container called formDiv. The container has a white background, rounded corners and a shadow to separate it from the rest of the page.

The input fields have rounded corners and light borders as well, and they will highlight the field that the user has pressed.

The submit button has bold text, rounded corners and colour which makes it stand out from the page.

The infoDiv is styled in a similar way to the formDiv and remains hidden until JavaScript activates it.


**2. SQL Database Query**
The first section creates a table called RestaurantReservation. It has six fields called ReservationId (which is the primary key), Username, Useremail, Reservation date, Time and NumberOfGusets

The second section inputs the people who have booked the restaurant, with the email, reservation date, time and number of guests.

The third section runs a query, which selects the people who booked the restaurant from 7-8 o’clock. It then puts the rows into one table to view.

The fourth section runs another query, which calculates the number of guests booked between September 13th and September 25th. The result is a single number under the label of TotalGuest. 

This is what the restaurant database looks like after inserting the people who booked a reservation. With email, date, time and number of guest

In the Python file, it connects to the Restaurant_Reservation database and runs two SQL queries. The program sets up a cursor that is used to send commands to the database. The first query is the select the people who booked the restaurant from 7-8. The cursor fetches all matching rows and prints them so the user can see which people booked within that hour. 

The second query calculates the total number of guests booked from the 13th to the 25th of September using the sum function. The script retrieves that single result and prints it. Once both queries are complete, the program closes the database connection to finish the process.


**3. Python Security Script**
There are two parts to the code: the first part is a function, and the second part is testing the function

The first line defines a function called validate_username

Inside the function, there are three conditions

The first condition checks if the username is 10 or more characters long. The second condition checks if the username only contains letters and numbers. The third condition checks if  the username doesn't contains a greater-than or a less-than sign. If all conditions are true, then it will print username is valid

The Second part is where the usernames are tested.

The first section has multiple predetermined usernames. Some are valid while others are invalid. For example, Usernameistoolong prints out Username Too Long, but JohnDoe and 1234 are valid.

The second part allows you to manually insert a username, for example, if you enter hi, it would be valid; however, if I add a less-than sign, it would become invalid. Similarly, if I add a dollar sign, it would also be invalid. To exit the loop, you type quit.