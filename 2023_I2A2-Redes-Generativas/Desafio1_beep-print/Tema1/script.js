// Array para armazenar os usuários cadastrados
var users = [];

// Função para verificar se um usuário já está cadastrado
function isUserRegistered(email) {
    return users.some(function(user) {
        return user.email === email;
    });
}

// Função para registrar um novo usuário
function registerUser(email, password) {
    var user = {
        email: email,
        password: password
    };
    
    users.push(user);
    
    console.log("Novo usuário registrado:", user);
}

// Função para efetuar login
function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Lógica de verificação do usuário e senha
    // Aqui você pode substituir pela lógica de autenticação real
    if (username === "usuario" && password === "senha") {
        // Limpa os campos de login
        document.getElementById("username").value = "";
        document.getElementById("password").value = "";
        
        // Redirecionar para a página de produtos
        window.location.href = "products.html";
    } else {
        alert("Usuário ou senha inválidos.");
    }
}

// Função para redirecionar para a página de "Esqueci minha senha"
function navigateToForgotPassword() {
    window.location.href = "forgotpassword.html";
}

// Função para enviar e-mail de redefinição de senha
function sendPasswordResetEmail() {
    var email = document.getElementById("email").value;
    
    // Lógica para enviar o e-mail de redefinição de senha
    // Aqui você pode implementar a lógica de envio de e-mail real
    
    alert("E-mail de redefinição de senha enviado para: " + email);
}
