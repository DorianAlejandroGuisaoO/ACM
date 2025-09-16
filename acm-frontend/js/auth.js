// js/auth.js
if(localStorage.getItem("loggedIn") !== "true"){
  window.location.href = "login.html";
}
