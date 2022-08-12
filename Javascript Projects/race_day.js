// Race Number
let raceNumber = Math.floor(Math.random() * 1000);
 
// Registrant's Time of Registration and Age
// Changeable Information
const Earlyregistrant = true;
const registrantAge = 19;
 
// Early Adult Registrant
if (Earlyregistrant == true && registrantAge > 18) {
 raceNumber += 1000;
}
 
// Control Flow - Checking Individual Racers
if (Earlyregistrant == true && registrantAge > 18) {
 console.log(`You will race at 9:30 am. Your racenumber is ${raceNumber}.`);
} else if (Earlyregistrant == false && registrantAge > 18) {
 console.log(`You will race at 11:00 am. Your racenumber is ${raceNumber}.`);
} else if (registrantAge < 18) {
 console.log(`You will race at 12:30 am. Your racenumber is ${raceNumber}.`);
} else {
 console.log("Please go see the registration desk for more information. Thank you.")
}
