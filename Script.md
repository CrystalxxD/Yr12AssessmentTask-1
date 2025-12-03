## <ins>**Script**</ins>
**1. Web Form Validation:**
This video will explain how the webpage works.

In index.html begins by setting up a basic webpage with a title that says “Register”. Inside the head section, it links to an external JavaScript file called script.js, which means the behaviour of the form will be controlled by that file. It also links to the CSS file which controls the style of the webpage

Inside the body, the HTML contains two main sections. The first one is a division called formDiv. This division holds the registration form that the user interacts with. At the top is a heading that says “Register”, followed by the actual form. The form includes four fields: a text field for the user's name, another for the email, a date selector for the date of birth, and a password field for the user’s chosen password. The form has an onsubmit attribute that tells the browser to call a function named submitForm when the user presses the submit button. This means the form does not automatically reload the page; instead, it hands control over to the JavaScript.

Below the form is a second division called infoDiv. This section starts off hidden, and its job is to display the user's information after the form has been successfully filled out and validated.

In the JavaScript file. The key function is submitForm, and it begins by stopping the default behaviour of the form, which would normally refresh the page. This allows the script to check the user’s input without losing anything.

The function then reads the values from all four input boxes using their IDs. The name and email are cleaned with the trim method so accidental spaces don’t interfere.

Next, the script performs several checks. The first check ensures that none of the fields are left empty. If the user tries to submit the form with missing information, an alert appears asking them to fill in everything.

The next check focuses on the email. It verifies that the email contains an @ symbol and a dot, which are basic requirements for a valid email format. If either is missing, the user is told to enter a valid email address.

After that, the password is checked. The script ensures that the password is at least eight characters long. Then it uses regular expressions to confirm that the password contains at least one letter and at least one number. If the password doesn’t meet these rules, the script stops and alerts the user.

If all validation passes, the formDiv is hidden by changing its display style. Then the script updates the infoDiv with a formatted summary of the user’s name, email, and date of birth, and finally makes this section visible. This allows the user to clearly see the information they submitted.

In the CSS file the body of the page is centred using flexbox so the form appears in the middle of the screen. A soft gradient background is applied to give the page a clean, modern look.

The form itself sits inside a styled container called formDiv. This box uses a white background, rounded corners, padding, and a subtle shadow to separate it from the rest of the page and make it stand out visually.

The input fields such as text, date, and password are styled to be the full width of the form. They have consistent padding, rounded corners, and a light border. When the user clicks into an input, the field highlights with a blue border and a shadow so it is clear which part of the form is active.

The submit button uses the accent colour from the theme. It has bold text, rounded corners, and a clean hover feel, making it clear and easy to interact with.

The infoDiv section, which displays the user’s details after the form is submitted, is styled in a similar way to the form box. It remains hidden until the JavaScript activates it.

**2. SQL Database Query**
This video is about SQL Script.

The first section creates a table called RestaurantReservation. It includes six fields. The first field, ReservationID, is an integer that works as the primary key, meaning each reservation must have a unique ID. Next is UserName, which stores the name of the person who made the booking, followed by UserEmail, which stores their email address. The table also includes ReservationDate, which records the date of the booking, and Time, which records the time of the reservation. The last field is NumberOfGuests, which tracks how many people are included in the reservation.

The second section inputs the people that have booked the restaurant, with the email, reservation date, time and number of guests.

The third section runs a query where it selects the people who booked the reservation from 7-8 o’clock. It then puts the rows into one table to view.

The fourth section runs another query which calculates the amount of guests booked between September 13th and September 25th. The result is a single number under the label of TotalGuest. 

This script connects to the Restaurant_Reservation database and then runs two SQL queries. When the connection is created, the program sets up a cursor that is used to send commands to the database. The first query selects every reservation where the recorded time is between 7:00 pm and 8:00 pm. The cursor fetches all matching rows and prints them so the user can see which people booked within that hour.
After that, the second query runs a calculation using the SUM function on the NumberOfGuests field. It selects all bookings between the thirteenth and twenty-fifth of September and adds together the total number of guests across those reservations. The script retrieves that single result and prints it. Once both queries are complete, the program closes the database connection to finish the process.

**3. Python Security Script**
In this video, I’m going to explain how the python security script

There is two parts to the code the first part is a function and the second part is testing the function

The first line defines a function called validate_username

Inside the function there is three conditions

The first conditions checks if the username is less than 10 characters. If it is invalid it prints Username too long

The second condition checks if the username is only letters and numbers. If it is invalid it prints Username must contain only letters and numbers.

The third condition checks whether the username contains a greater-than or a less-than sign. If it is invalid it prints Username cannot contain '<' or '>' characters.

If all conditions are true than it will print username is valid

The Second part is where the username are tested.

The first section has a multiple predetermined usernames. Some are valid while others are invalid

The second part allows you to manually insert username for example if you enter hi it would be valid however if I add an less than sign it would become invalid. Similarly if I add a dollar sign it would also be invalid. Two exit the loop you type quit
