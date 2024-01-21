Airbnb Clone Project
====================

This project is an Airbnb clone that aims to replicate some of the core functionalities of the Airbnb platform. It provides a command-line interface (CLI) that allows users to interact with the system, manage property listings, and perform various operations related to property rentals.

Project Overview
----------------

The Airbnb clone project consists of a modular architecture with a focus on the Model-View-Controller (MVC) design pattern. The data models, business logic, and user interface are structured to facilitate extensibility and maintainability.

Command Interpreter
-------------------

The heart of the Airbnb clone is its command interpreter. The command interpreter allows users to interact with the system through a text-based interface. It accepts various commands for managing users, properties, bookings, and more.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1.  Open a terminal window.
2.  Navigate to the project directory.
3.  Run the command: `./console.py`

The command interpreter will launch, indicating that it's ready to accept commands.

### How to Use the Command Interpreter

The command interpreter accepts a variety of commands, each corresponding to a specific action within the Airbnb clone. Here are some common commands:

*   `create`: Create a new instance of a specified model.
*   `show`: Display details of a specific instance.
*   `update`: Update attributes of a specific instance.
*   `destroy`: Delete a specific instance.
*   `all`: Display all instances or all instances of a specific model.

To execute a command, enter the command followed by relevant arguments. For example:

sqlCopy code

`create User email="user@example.com" password="password123" show User 1 update Place 5 name="Cozy Cabin" destroy Review 3 all City`

### Examples

1.  **Create a User:**
    
    sqlCopy code
    
    `create User email="john.doe@example.com" password="securepassword"`
    
2.  **Show Property Details:**
    
    sqlCopy code
    
    `show Place 1`
    
3.  **Update Property Information:**
    
    sqlCopy code
    
    `update Place 2 name="Luxury Apartment" price_per_night=200`
    
4.  **Delete a Booking:**
    
    undefinedCopy code
    
    `destroy Booking 4`
    
5.  **List all Cities:**
    
    cssCopy code
    
    `all City`
    

These are just a few examples, and the command interpreter supports a wide range of commands to manage different aspects of the Airbnb clone.

Feel free to explore and experiment with the available commands to create, view, update, and delete data within the system.