# Restaurant Reservation

This project was made for the python trainning made on Natixis.

## Features
### Login and Register
At the home menu, you will be able to login or register a user.  
A user can be registered as a **Staff** or a **Regular** user.


### User permission
* If you are a **Staff** member, you will be able to register/delete a new restaurant and also checkout a reservation. The checkout will be used when the people leave the restaurant, to notify that their table is free.
* If you are a **Regular** user, you will be able to reserve a restaurant. The restaurants that a regular user can reserve (previously added by a Staff member) will be shown on a list.
* If you aren't logged in, you will only be able to see the list of available restaurants.


### Reservation
The staff is able to see all the reservations registered. They can see the person's name, the amount of people and the restaurant where they reserved.  
An user can reserve any restaurant from the list, if the amount of people are less or equal than the capacity of the restaurant. Otherwise, he will receive an error message. The restaurant capacity will be updated after every reservation.

It is assumed that all the restaurants have tables of 4. This means that if a person reserves a table for only 2 people, 4 places will be removed from the restaurants capacity.

An user can also cancel a reservation. If they cancel it, the restaurant capacity will be updated accordingly.
