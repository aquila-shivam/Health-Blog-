# Health Blog Platform

This is a Django-based web application for a health blog platform.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aquila-shivam/Health-Blog-Platform.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Health-Blog-Platform
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000/` to view the health blog.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/new-feature`)
6. Create a new Pull Request
