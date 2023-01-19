// VARIABLES - TASK 1

// let dayOfWeek = 'Monday';
// console.log(dayOfWeek);
// dayOfWeek = 'Friday';
// console.log(`I can\'t wait for ${dayOfWeek}!`);



// VARIABLES - TASK 2

// let animalInput = prompt('What is your favorite animal? ').toLowerCase();
// let colorInput = prompt('What is your favorite color? ').toLowerCase();

// // Checks if letter is a vowel in order to send a gramatically correct sentence back
// function isVowel(letter) {
//     let vowels = 'aeiou';

//     for (let i = 0; i <= vowels.length; i++) {
//         if (letter === vowels[i]) {
//             return true
//         }
//     }
//     return false;
// }

// if (isVowel(colorInput[0])) {
//     console.log(`I've never seen an ${colorInput} ${animalInput}!`);
// }
// else {
//     console.log(`I've never seen a ${colorInput} ${animalInput}!`);
// }



// CONDITIONALS - TASK 1

// Sausage Egg & Cheese Croissant, Quesadillas, Nashville Hot Chicken
// let timeOfDay = 2000;
// let meal;

// if (timeOfDay < 1200) {
//     meal = 'Sausage Egg & Cheese Croissant';
// }
// else if (timeOfDay < 1700) {
//     meal = 'Quesadillas';
// }
// else {
//     meal = 'Nashville Hot Chicken';
// }

// console.log(meal);



// CONDITIONALS - TASK 2

// let randomNumZeroToTen = Math.floor(Math.random() * 10);

// if (randomNumZeroToTen < 3) {
//     console.log('Beatles');
// }
// else if (randomNumZeroToTen < 6) {
//     console.log('Stones');
// }
// else if (randomNumZeroToTen < 9) {
//     console.log('Floyd');
// }
// else {
//     console.log('Hendrix');
// }



// FOR LOOPS - TASK 1

// for (let i = 0; i < 7; i++) {
//     console.log('JavaScript is cool!');
// }



// FOR LOOPS - TASK 2

// for (let i = 0; i < 11; i++) {
//     console.log(i);
// }



// FOR LOOPS - TASK 3 

// for (let i = 0; i < 5; i++) {
//     console.log('hello');
//     console.log('goodbye');
// }



// FUNCTIONS - TASK 1

// function printMovieName(movie) {
//     console.log(movie);
// }

// printMovieName('Interstellar');



// FUNCTIONS - TASK 2

// function favBand(favBand) {
//     return favBand;
// }

// let myFavBand = favBand('Sublime');
// console.log(myFavBand);



// // FUNCTIONS - TASK 3

// function concertDisplay(musicalAct) {
//     let myStreet = prompt('What street do you live on? ');
//     console.log(`It would be great if ${musicalAct} played a show on ${myStreet}!`);
// }

// concertDisplay(myFavBand);



// ARRAYS - TASK 1

// let desktopItems = ['desk', 'lamp', 'computer'];
// console.log(desktopItems[1]);
// desktopItems.push('Infinity Gauntlet');

// for (let item in desktopItems) {
//     console.log(desktopItems[item]);
// }



// BONUS - TASK 1

// let magicNumber = Math.floor(Math.random() * 100);
// let guess = 0;


// while (guess != magicNumber) {
//     guess = prompt('Guess the magic number! ');
//     if (guess < magicNumber) {
//         console.log('Too low!');
//     }
//     else {
//         console.log('Too high!');
//     }
//     if (Math.abs(magicNumber - guess) < 10) {
//         console.log('Getting warmer!');
//     }
// }

// console.log(`Magic Number: ${magicNumber}. Congratulations! You guessed the magic number!`);