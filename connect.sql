CREATE DATABASE ATM_booth;

USE ATM_booth;

-- Table for storing user accounts
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    pin VARCHAR(4) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00
);

-- Table for storing transactions
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    type VARCHAR(255) NOT NULL,  -- 'Deposit' or 'Withdrawal'
    amount DECIMAL(10, 2) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
