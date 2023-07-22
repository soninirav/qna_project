# QnA Web App

Welcome to the QnA Web App - an interactive platform powered by Django framework! Engage in meaningful discussions with features like asking questions, commenting on answers, exploring trending questions, managing your asked questions, and even deleting them if needed. With secure sign-in and sign-up functionalities, connect with a community of knowledge seekers and experts to enhance your learning experience.

### Home Page 
Explore a comprehensive list of all questions asked by other users on this website.
### Sign up 
Sign up page for users.
### Login 
Login Page for users.
After login users will be redirected to Home Page.
### Ask Quesetion
The page offers users the ability to ask their question with detailed description.
### Reply 
Where the currently logged-in user can answer to any of the listed questions.
### My Questions
Where currently loggedin user can see all his/her previously asked questions on site.
### My Answers
Where currently logged in user can see all his reply on listed questions.
### Logout 
Logout functionality for users.

### APIs

`/` : Return the home page

`login/` : Logging In

`logout/` : Logging Out

`register/` : Save user details to database

`user/question/create/` :  Save question title and description to database

`user/question/<int:pk>/update/` : Update question title and description

`user/answer/<int:pk>/update/`:  Update answer

`user/question/<int:pk>/delete/` : Delete the specific question if the question was created by currently logged in user.

`user/answer/<int:pk>/delete/` : Delete the specific answer if the answer was given by currently logged in user.

`user/question/myquestion/` : List all the questions asked by currrently logged in user.

`user/myanswer/` : List all the replies given by currently logged in user.

`user/question/<int:pk>/answer/` : save reply to current question to DB.

## **DEMO**
#### YouTube Link: https://youtu.be/etH1YJ9Vp40

