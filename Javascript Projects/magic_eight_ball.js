// User's Name
let userName = "Rishi";
 
// Introduction Statement
userName ? console.log(`Hello, ${userName}!`) : console.log(`Hello!`);
 
// Question Asked
const userQuestion = "Is today a good day?";
console.log(`${userName}, your question is \"${userQuestion}\"`);
 
// Control Flow With Random Number Method
let randomNumber = Math.floor(Math.random() * 8);
let eightBall = "";
 
// Control Flow
switch (randomNumber) {
 case 0:
   eightBall = "It is certain";
   break;
 
 case 1:
   eightBall = "It is decidely so";
   break;
 
 case 2:
   eightBall = "Reply hazy try again";
   break;
 
 case 3:
   eightBall = "Cannot predict now";
