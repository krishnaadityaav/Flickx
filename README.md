**Project Documentation**
****Project Overview****
Users can create and join chat rooms using the web chat application, which is built on Django. The programme allows two different sorts of rooms: password-protected private rooms and open, public rooms that anybody can enter. To use the app, users must provide their login and email address. The Django email library is also used by the app to let owners email invitations to other users.
****Project Details****
a. Project Name: Django Web Chat App b. Project Version: 1.0
c. Project Author: [M.Lakshmi Jotsna , B.Raj Kishore, T.Amrutha Varshini]
d. Date: [27-06-2023]
****Technologies Used****
a. Django Framework:
Version: 4.1.7
Description: A high-level Python web framework that simplifies the development of web applications.
Usage: Used as the core framework for building the web chat app.
b. Django email library:
Version: 4.1.7
Description: A module provided by Django for sending emails within applications.
Usage: Utilized to send invitations from owners to other users via email.
****Installation Instructions****
To install and set up the Django Web Chat App, follow these steps:
Clone the project repository from [https://github.com/KI-2003/Summer-project].
Install Python 3.9 or above if not already installed.
Create a virtual environment using virtualenv or venv.
Activate the virtual environment.
Install the required dependencies using pip install -r requirements.txt.
Configure the database settings in the settings.py file.
Run database migrations using python manage.py migrate.
Start the development server using python manage.py runserver.
Access the web chat app in your web browser at http://localhost:8000.
****Usage Guide****
a. User Registration and Login:
Visit the web chat app's homepage.
Click on the "Signup" button and provide your email and username to create an account.
Alternatively, if you already have an account, click on the "Login" button and enter your credentials.
b. Room Creation and Joining:
After logging in, you will be redirected to the dashboard.
To create a room, click on the "Create Room" button in "My Rooms" category.
Choose the room type (private or public).
Set a password if it's a private room.
Submit the form to create the room.
To join a room, click on the "Join Room" button and enter the room ID.
If it's a private room, enter the password to join.
c. Sending Invitations:
As an owner of a private room, you can send invitations to other users.
Navigate to the room details page.
Enter the email addresses of the users you want to invite.
Click on the "Send Invitations" button.
The selected users will receive an email invitation to join the room.
Project Structure
The project structure follows the standard Django application structure. The important directories and files are as follows:
manage.py: Entry point for running administrative commands.
djangochat/:
settings.py: Contains the project's settings, including database configurations and third-party library integrations.
urls.py: Defines the URL patterns for the project's views.
views.py: Contains the logic for handling HTTP requests and rendering templates.
models.py: Defines the database models for the chat app.
routing.py:  Mapping the URL directly to the code that creates the webpage.
templates/: Contains HTML templates for rendering web pages.
static/: Contains static files such as CSS and JavaScript.
Dependencies
Django: 4.1.7
Django email library (SMTP): 4.1.7
Troubleshooting
Common issues and their solutions:
Issue: Database connection error. Solution: Check the database settings in settings.py and ensure the database server is running.
Issue: Email invitations are not being sent. Solution: Verify that the email configurations in settings.py are correct, including SMTP server settings and authentication details.
//Support and Contact
For any support or inquiries, please contact us via mail.
Mail id: headmail0607@gmail.com
//Acknowledgments
We would like to acknowledge the Django community for their excellent framework and the developers of the Django email library for their contribution.
