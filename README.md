# Result Tracking System for University students and Parents.
<p>Parents have no direct access to their children results. They have to wait for their children to send it to them and that is not guaranteed as the children may not want to because of their performance. Students have to see their Exam officers directly anytime they need to check their results. Such process is time consuming and hectic for both the Students and the Exam officers. This project developed a result tracking system to solve these problems. Object Oriented Analysis and Design Methodology was used to analyze and design the system using various UML diagrams. The project was implemented on a Windows 10 operating system using Visual Studio Code as the IDE.  MySQL was used to handle the database. HTML, CSS, Python and the Django framework were the languages used to develop the system. The system would be beneficial to Students, Parents or Guardians and the Examination Officer</p>

## Statement of the Problem
<ul>
<li>Parents and Guardians may have to go physically to the university to ask lecturers or administrators for their children’s results.</li>
<li>Parents and Guardians have no direct access to their children’s results.</li>
<li>Students may send their parents forged results.</li>
<li>Students may lie that their results have not been published.</li>
</ul>

## Objectives
<ul>
<li>Create an interface to enable Parents, Guardians and Students to login and access the system. </li>
<li>Design the result tracking system.</li>
<li>Design the result tracking system.</li>
<li>Students may lie that their results have not been published.</li>
</ul>

## User Manual
<ul>
<li>Ensure you have python version 3 on your computer. If you do not install it by going to the official website </li>
<li>Activate a virtual environment. You can do this through this process:</li>
<ul>
<li>Open your command prompt.</li>
<li>Navigate to the location of the project folder on your computer using the “cd” command.</li>
<li>Type this code and press enter “python –m venv env”</li>
<li> The virtual environment has been created in a folder “env” </li>
<li> Type this code and press enter to activate it “env\scripts\activate”.</li>
</ul>
<li>Install the Django framework by typing this code “pip install Django” </li>
<li>Install mysqlclient by typing “pip install mysqlclient” </li>
<li> Create a mysql database hosted on your localhost </li>
<li> Under the school_project folder go to the settings file and look for the database dictionary </li>
<li>Update the name, user and password variables to yours.</li>
<li> Prepare migrations by typing “python manage.py makemigrations” </li>
<li> Create the database tables by typing “python manage.py migrate” </li>
<li> Create a super user for the system by typing “python manage.py createsupersuer”. </li>
<li> Run the server for the project by typing this code “python manage.py runserver” </li>
<li> Open a web browser and paste the url gotten from the server launch above </li>
</ul>
<br>
<div>
Once the browser is open a Student should register through the sign page. He or she would be required to provide his or her registration number, password, first name, last name, a password, phone number, his or her parent’s name, email and phone number. If all the credentials provided are of correct type then both the Student and Parent will be registered on the system. The Parent would receive his or her password via email. After signing up the user would be directed to the login page. The Student or Parent or Exam officer should input his or her username and password in order to login. If the credentials are correct the user will be logged in and directed to the home page. If the user is the exam officer, the home page would have two buttons that leads to other pages for result updating and result uploading respectively. If the Exam officer wants to upload student results he or she should click the “upload result” button. He or she will be directed to a search page where student’s registration numbers can be searched. The Exam officer can search for the student that he or she wants to upload a result for. Upon searching a list of registration numbers that matches the search input is returned. The Exam officer can now select the number he or she wants to upload result for by clicking on it. After clicking on the registration the exam officer would be directed to the upload result page. The Exam officer would be required to provide the details of the result such as the course, grade, score, semester and session of the result. Once provided the exam officer should click the upload button to upload the results. Once the upload is successful an email would be sent to the Student’s Parent informing him or her about the new result published and the exam officer would be redirected to the search page to make another upload. If the Exam officer wants to update n result he or she should click on the home page menu. The Exam officer would now be able to see the “update results” button. If clicked the exam officer would be redirected to the update page where he or she can search for a particular result and make changes.
If it is a Student or Parent that logs in, the home page would have a “view results” button. When clicked the user would be directed to a page that requests them to choose the level and semester result to be viewed. If the level and semester is selected the user would be directed to a page that shows all the available results of the student for that semester.
</div>