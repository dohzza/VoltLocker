
console.log("using register.js");

//need to set up using URL's for this to work
import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js';
import { getDatabase, ref, push, get, child} from 'https://www.gstatic.com/firebasejs/10.8.1/firebase-database.js';

const firebaseConfig = {
    databaseURL: "https://voltlockerapp-default-rtdb.firebaseio.com/"
};


const app = initializeApp(firebaseConfig);
//console.log(app);
const database = getDatabase(app);
const SInfoInDatabase = ref(database, "StudentInfo");


const formFirstName = document.getElementById("inputFname");
const formLastName = document.getElementById("inputLname");
const formStudentID = document.getElementById("inputSid");
const registerForm = document.getElementById("registerFormID");

/*
// Function to check if a value exists in the database
function checkValueInDatabase(valueToCheck) {
  
    console.log("Checking for value...");
    // Use once() method to read the data once
    SInfoInDatabase.once('value').then(function(snapshot) {
    //get(child(database,'StudentInfo')).then((snapshot) => {
      console.log("in get");
      if (snapshot.exists()) {
        // Data exists, now check if the valueToCheck exists
        var data = snapshot.val();
        if (Object.values(data).includes(valueToCheck)) {
          console.log("Value exists in the database.");
        } else {
          console.log("Value does not exist in the database.");
        }
      } else {
        console.log("No data found in the database.");
      }
    }, function(error) {
      console.error("Error reading data:", error);
    });
    console.log("past get");
  }
*/
registerForm.addEventListener("submit", function()
{

    console.log("\nRegister: submitting...");
    const fNameValue = formFirstName.value;
    const lNameValue = formLastName.value;
    const SidValue = formStudentID.value;

    //Call function to check if sID already has battery checked out
    //checkValueInDatabase(SidValue);

    console.log("First Name: " + fNameValue + "\nLast Name: " + lNameValue + "\nStudent ID #" + SidValue + "\n");

    //Format: push({created reference value},{what to push to database})
    push(SInfoInDatabase, {
        StudentID: SidValue,
        FirstName: fNameValue,
        LastName: lNameValue
    });

    console.log(SidValue + ' added to database');
});


