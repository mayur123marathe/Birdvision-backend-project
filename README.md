# Flask E-Commerce API

A simple RESTful API built using Python Flask for managing products in an e-commerce application. The API handles products stored in an SQLite database and responds with JSON formatted data.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is designed as a basic backend API for managing products in an e-commerce setting. It provides CRUD (Create, Read, Update, Delete) operations for products stored in an SQLite database. All interactions with the API return JSON responses.

## Features

- Add new products to the database
- Retrieve details of all or specific products
- Update product details
- Delete products from the database
- Products stored in SQLite, with responses in JSON format

## Technologies Used

- **Flask**: Python microframework for web development
- **SQLite**: Lightweight relational database for local storage
- **SQLAlchemy**: ORM for SQLite integration
- **Python 3**: Programming language
- **JSON**: Data exchange format

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-ecommerce-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-ecommerce-api
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Initialize the SQLite database by running the following script:

    ```bash
    python init_db.py
    ```

    This will create an `ecommerce.db` file and set up the required tables.

2. The database schema can be found in the `init_db.py` file.

## Running the Application

1. Start the Flask server:

    ```bash
    flask run
    ```

2. By default, the server will run at `http://127.0.0.1:5000/`.

3. You can test the API using a tool like Postman or curl.

## API Endpoints

The following endpoints are available in the API:

### Get All Products

- **URL**: `/products`
- **Method**: `GET`
- **Description**: Retrieves a list of all products.
- **Response**: JSON array of products.

### Get a Single Product

- **URL**: `/products/<id>`
- **Method**: `GET`
- **Description**: Retrieves a product by its ID.
- **Response**: JSON object of the product.

### Add a New Product

- **URL**: `/products`
- **Method**: `POST`
- **Description**: Adds a new product to the database.
- **Request Body**: JSON with product details.

    ```json
    {
        "name": "Product Name",
        "description": "Product Description",
        "price": 19.99,
        "quantity": 10
    }
    ```

- **Response**: Confirmation message with the new product ID.

### Update a Product

- **URL**: `/products/<id>`
- **Method**: `PUT`
- **Description**: Updates an existing product.
- **Request Body**: JSON with updated product details.
- **Response**: Confirmation message.

### Delete a Product

- **URL**: `/products/<id>`
- **Method**: `DELETE`
- **Description**: Deletes a product by its ID.
- **Response**: Confirmation message.

## Testing

1. To run tests, first make sure the Flask application is not running.

2. Use the following command to run the test suite:

    ```bash
    pytest
    ```

3. Test cases are located in the `tests/` directory.

## Future Enhancements

- Implement user authentication and authorization
- Add pagination for large datasets
- Add more advanced filtering options for products
- Include more detailed validation on inputs
- Add a front-end interface for managing products

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch with your feature/bug fix.
3. Commit your changes.
4. Push to your branch and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
