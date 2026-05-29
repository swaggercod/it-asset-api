# IT Asset Management API

A modern, fast, and documented RESTful API built with Python and FastAPI for managing corporate IT inventory.

## Overview
This backend service provides an automated way to track and manage IT equipment (Laptops, Routers, Servers, etc.). It demonstrates core backend engineering principles, including routing, data modeling with Pydantic, and automatic OpenAPI (Swagger) documentation.

## Features
* **GET /assets:** Retrieve a list of all recorded IT assets.
* **GET /assets/{id}:** Fetch details of a specific asset by its ID.
* **POST /assets:** Register a new IT asset into the inventory system.

## Tech Stack
* **Framework:** FastAPI (Python)
* **Server:** Uvicorn
* **Data Validation:** Pydantic

## How to Run
1. Clone this repository.
2. Install dependencies:
   `pip install fastapi uvicorn`
3. Start the local server:
   `python -m uvicorn main:app --reload`
4. Visit `http://127.0.0.1:8000/docs` to interact with the API via Swagger UI.
