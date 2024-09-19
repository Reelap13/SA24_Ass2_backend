# AnyChat

## Project Description:

This project is a server for an anonymous chat, built using FastAPI with Python. The server supports three main types of requests:

1. Retrieve the number of messages.
2. Retrieve all messages.
3. Send messages.

## Project Structure:

- api: Contains routers that organize and handle requests, splitting them into different files and categories for better management.

- schemas: This folder holds object schemas, such as schemas for message sending requests and schemas for client request responses. This helps with data validation and structuring.

- services: Implements the core functionality for handling requests. These modules manage the application's logic and data interactions.

- systems: Contains larger systems and components of the project responsible for the execution logic of various parts. This may include chat state management functions or other significant architectural elements.
