function validatepassword() {
    // var name_error = document.getElementById('name_error');
    // var namecheck = document.getElementById('username').value.trim();
    var email_error = document.getElementById('email_error');
    var emailcheck = document.getElementById('email-e21e').value.trim();
    var password = document.getElementById('password_error');
    var passwordcheck = document.getElementById('password-a30d').value.trim();

    // if(namecheck === '' && emailcheck === '' && passwordcheck === '' ){
    //     name_error.innerHTML = 'Please enter your name';
    //     document.getElementById("username").style.borderColor = "red";
    //     email_error.innerHTML = 'Please enter your email id';
    //     document.getElementById("email").style.borderColor = "red";
    //     password_error .innerHTML = 'Please enter your password';
    //     document.getElementById("password").style.borderColor = "red";
    //     return false;
    // }
    //username
    // if(namecheck === ''){
    //     name_error.innerHTML = 'Please enter your name';
    //     document.getElementById("username").style.borderColor = "red";
    //     return false;
    // }
    // if (!namecheck.match(/^(?=.*[0-9])[a-zA-Z0-9!@#$%^&*]{7,15}$/)) {
    //     name_error .innerHTML = '7-15 characters[At least one numeric digit]';
    //     document.getElementById("username").style.borderColor = "red";
    //     return false;
    // }
    // if (namecheck.match(/^(?=.*[0-9])[a-zA-Z0-9!@#$%^&*]{7,15}$/)) {
    //     name_error.innerHTML = '';
    //     document.getElementById("username").style.borderColor = "Green";
    // }

    //email

    if (emailcheck === '') {
        email_error .innerHTML = 'Please enter your email id';
        document.getElementById("email-e21e").style.borderColor = "red";
        return false;
    }
    // if(!emailcheck.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
    //     email_error .innerHTML = 'Please check your email';
    //     document.getElementById("email").style.borderColor = "red";
    //     return false;
    // }
    if(emailcheck.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
        email_error .innerHTML = '';
        document.getElementById("email-e21e").style.borderColor = "Green";
    }

    //password

     if (passwordcheck === '') {
        password.innerHTML = 'Please create your password';
        document.getElementById("password").style.borderColor = "red";
        return false;
    }
    if (!passwordcheck.match(/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/)) {
        password.innerHTML = '7-15 characters[At least one numeric digit and special character]';
        document.getElementById("password").style.borderColor = "red";
        return false;
    }
    if (passwordcheck.match(/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/)) {
        password.innerHTML = '';
        document.getElementById("password").style.borderColor = "Green";
    }
}
//     const usernameValue = username.value.trim();
//     const emailValue = email.value.trim();
//     const password1Value = password1.value.trim();

//     errorCount = 0;

//     if (usernameValue == "") {
//         setError(username, 'User name cannot be empty');
//     }
//     else {
//         setSuccess(username);
//         localStorage.setItem('name', username.value);
//     }

//     //email id


//     if (emailValue == "") {
//         setError(email, 'Please enter your email');
//     }
//     else if (!isEmail(emailValue)) {
//         setError(email, 'Email id not valid');
//     }
//     else {
//         setSuccess(email);
//         localStorage.setItem('Email id', email.value);
//     }

//     //password


//     if (password1Value === '') {
//         setError(password1, 'Please enter your password');
//     }
//     else if (!password1Value.match(/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/)) {
//         setError(password1, '7-15 characters at least 1 numeric digit and special character');
//     }
//     else {
//         setSuccess(password1);
//         localStorage.setItem('Password', password1.value);

//     }

//     if (errorCount === 0) {
//         return true;
//         alert("Register successfully");
//         window.parent.location.href = "home page.html";
//     }

// }

// function setError(input, message) {
//     const formControl = input.parentElement;
//     const small = formControl.querySelector('small');
//     formControl.className = 'form-control error';
//     small.innerText = message;
//     errorCount++;
// }
// function setSuccess(input) {
//     const formControl = input.parentElement;
//     formControl.className = 'form-control valid';
//     errorCount = errorCount > 0 ? errorCount-- : 0;

//     // console.log("SUCCESS: ErrorCOunt = ", errorCount, " From = ", input);

// }
// function isEmail(email) {
//     return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email);
// }