# Website
The Face, a program made during the 2015 Kent HAck Enough Competition is a app that has the ability of recognizing people and provide them with basic info of the desired person.

## Inspiration
We did a graphic recognize system last year in KHE, and this year we want to do something better.

## What it does
It can get data from people's facebook account, save them in our database. After recording several pictures from this person, our system will recognize him/her out through camera, and display the information next to his/her head. We can recognize multiple people at the same time, so I think our system can be used in classroom, meeting or party. Since it read data through camera, we can also aim camera at some old pictures so that it can help us recall old friends in the picture.

## How I built it
Basically it can be divided into three part, information record, face recognize and information display. We used javascript to get data from facebook, and save them into our online database parse. We used python and opencv library to recognize faces, get the coordinate of each face, then get data from database, and display the information dynamically next to the person's head.

## Challenges I ran into
Teaching a machine to learn people's face it not very easy. Building a connection to database it not easy, and display the information dynamically is not easy. Basically every part is a challenge for us.

## Accomplishments that I'm proud of
We were very happy when we finished the information grab part and information display part, but our most exited moment was when all our team members' face were correctly recognized by our system.

## What I learned
Python is not our favorite programming language, but to build this project, we learned a lot about python. Opencv was the library we used last year, but facial recognition is a different field. Also javascript API to facebook is also a big harvest that we got.

## What's next for Facial Recognition System
We want to optimize our algorithm to increase the accuracy of recognition. We also want to encapsulate our project as a mobile app so it can be used more widely in our life.
