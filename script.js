// script.js

let users = [];
let currentUser = null;

document.getElementById("login-form").addEventListener("submit", login);
document.getElementById("create-account-form").addEventListener("submit", createAccount);
document.getElementById("create-account-btn").addEventListener("click", showCreateAccountScreen);

function showCreateAccountScreen() {
    document.getElementById("login-screen").style.display = "none";
    document.getElementById("create-account-screen").style.display = "block";
}

function login(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const pin = document.getElementById("pin").value;

    const user = users.find(user => user.name === username && user.pin === pin);

    if (user) {
        currentUser = user;
        document.getElementById("user-name").textContent = username;
        showAccountScreen();
    } else {
        alert("Invalid username or PIN");
    }
}

function createAccount(event) {
    event.preventDefault();
    const username = document.getElementById("new-username").value;
    const pin = document.getElementById("new-pin").value;

    if (pin.length !== 4 || isNaN(pin)) {
        alert("PIN must be 4 digits");
        return;
    }

    const user = {
        name: username,
        pin: pin,
        balance: 0,
        transactions: []
    };

    users.push(user);
    alert("Account created successfully!");
    showLoginScreen();
}

function showLoginScreen() {
    document.getElementById("create-account-screen").style.display = "none";
    document.getElementById("login-screen").style.display = "block";
}

function showAccountScreen() {
    document.getElementById("login-screen").style.display = "none";
    document.getElementById("create-account-screen").style.display = "none";
    document.getElementById("account-screen").style.display = "block";
}

function checkBalance() {
    alert(`Your balance is: $${currentUser.balance}`);
}

function depositMoney() {
    const amount = parseFloat(prompt("Enter amount to deposit:"));
    if (amount > 0) {
        currentUser.balance += amount;
        currentUser.transactions.push(`Deposited: $${amount}`);
        alert(`Deposited $${amount}. New balance: $${currentUser.balance}`);
    } else {
        alert("Invalid amount");
    }
}

function withdrawMoney() {
    const amount = parseFloat(prompt("Enter amount to withdraw:"));
    if (amount > 0 && amount <= currentUser.balance) {
        currentUser.balance -= amount;
        currentUser.transactions.push(`Withdrew: $${amount}`);
        alert(`Withdrew $${amount}. New balance: $${currentUser.balance}`);
    } else {
        alert("Invalid amount or insufficient funds");
    }
}

function transactionHistory() {
    const historyList = document.getElementById("history-list");
    historyList.innerHTML = "";
    currentUser.transactions.forEach(transaction => {
        const li = document.createElement("li");
        li.textContent = transaction;
        historyList.appendChild(li);
    });
    document.getElementById("transaction-history").style.display = "block";
}

function logout() {
    currentUser = null;
    document.getElementById("account-screen").style.display = "none";
    showLoginScreen();
}
// Toggle the visibility of the PIN
document.getElementById('toggle-password').addEventListener('click', function() {
    var pinInput = document.getElementById('pin');
    var icon = document.getElementById('toggle-password');

    if (pinInput.type === 'password') {
        pinInput.type = 'text';
        icon.innerHTML = '&#128064;'; // Eye open icon
    } else {
        pinInput.type = 'password';
        icon.innerHTML = '&#128065;'; // Eye closed icon
    }
});
