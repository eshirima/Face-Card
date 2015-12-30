# Website
The Face, a program made during the 2015 Kent HAck Enough Competition is an app that has the ability of recognizing people and provide them with basic info of the desired person.

## Inspiration
We did a graphic recognition system last year in 2014 KHE, and this year we were inspired to do something better.

## What it does
It can get data from people's Facebook account and save it in our database. After recording several pictures from this person, our system will recognize him/her out through any camera, and display the information next to his/her head. We can recognize multiple people at the same time, so I think our system can be used in classrooms for attendance taking, meetings or parties. Since it reads data through one's camera, we can also aim the camera towards some old pictures so that it can help us recall old friends in the picture.

## How we built it
Basically it can be divided into three parts; information recording, face recognition and information display. We used Javascript to get user data through the Facebook Graph API, and save them into our online Parse Database.
We used Python along with the OpenCV library to recognize face(s), get the coordinate of each face, then get each user's respective data from our Parse database.
Finnally, displaying the information dynamically next to the person's head.

## Challenges we ran into
Teaching a machine to learn people's face is it not as easy as it sounds since slight changes of the light source deems as a huge factor to the success of the system in general.
Building a connection to the database using different types of languages and conecting the two was not easy as well inconstrast to just building and retrieving using a single language.
Finally, displaying the information dynamically is not easy as we had to keep track of each user's face throughout and calculate the best place to fully display your info.
Basically every part of the project proved to be a challenge we were willing to tackle as a team!

## Accomplishments that we're proud of
We were very happy when we finished the information grabbinng and display part, but our most exiciting moment was when all our team members' face were correctly recognized by our own system!!

## What we learned
Python is not our favorite programming language, but to build this project, we learned a lot about Python.
Opencv was the library we used last year, but facial recognition is a different field. Also Javascript API to Facebook's Graph API is also a big harvest that we got.

## What's next for Facial Recognition System
We want to optimize our algorithm to increase the recognition accuracy. We also want to encapsulate our project as a mobile app so it can be used more widely in our life.

## System Link
http://eshirima.github.io/Face-Card/
