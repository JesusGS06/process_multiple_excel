
CREATE DATABASE hotel;

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    occupation VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    date_of_entry DATE NOT NULL
);