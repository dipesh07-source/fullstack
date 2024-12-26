let myform= document.getElementById("form_register")

addEventListener('submit', function (event) {
    // Prevent form submission
    event.preventDefault();
    let myUsername1 = document.getElementById('username');
    let myemail = document.getElementById('email');
    let mypassword = document.getElementById('password');
    let myaddress = document.getElementById('address'); 
  
    console.log(myUsername1.value);
    console.log(myemail.value);
    console.log(mypassword.value);
    console.log(myaddress.value);
  })
