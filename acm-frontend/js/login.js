// js/login.js
document.getElementById("loginForm").addEventListener("submit", function(e){
  e.preventDefault();
  const user = document.getElementById("username").value.trim();
  const pass = document.getElementById("password").value.trim();

  // credenciales simuladas
  if(user === "admin" && pass === "1234"){
    localStorage.setItem("loggedIn", "true");
    window.location.href = "chat.html"; // redirige al chat
  } else {
    alert("Usuario o contraseña incorrectos");
  }
});