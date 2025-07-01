<style>
    p, ul{
        line-height: 2.2rem;
    }
    ul ul{
        list-style: square;
    }
</style>

<img src="home-page.png" width="100%">

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

<li>Ensure you have python version 3 on your computer. If you do not install it by going to the official website </li>
<li>Activate a virtual environment. You can do this through this process:</li>

<ul>

- Open your command prompt.

- Navigate to the location of the project folder on your computer using the `cd` command.

- Type this code and press enter `python –m venv env`

- The virtual environment has been created in a folder “env”

- Type this code and press enter to activate it `env\scripts\activate`.

</ul>

- Install the Django framework by typing this code `pip install Django`

- Install mysqlclient by typing `pip install mysqlclient`

- Create a mysql database hosted on your localhost.

- Under the school_project folder go to the settings file and look for the database dictionary.

- Update the name, user and password variables to yours.

- Prepare migrations by typing `python manage.py makemigrations`

- Create the database tables by typing `python manage.py migrate`

- Create a super user for the system by typing `python manage.py createsupersuer`.
- Run the server for the project by typing this code `python manage.py runserver`
- Open a web browser and paste the url gotten from the server launch above.

<br>
<p> For more details on the project please check the project pdf report in the repo. </p>

<p>Below is a live demonstration of the system</p>
<video width="500" poster="home-page.png" controls>
<source src="https://youtu.be/VeWnA5CrBHo" type= "video/mkv">

</video>