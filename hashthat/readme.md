# Django Hasher
Hashthat is a simple website built with Django that takes user input and generates a SHA256 hash. This project follows the Test-Driven Development (TDD) approach to ensure code quality and reliability.

## Features
- User-friendly interface to input text for hashing.
- Generates a SHA256 hash for the provided text.
- Displays the generated hash to the user.
- Test suite to validate the functionality of the website.

## Installation
Clone the repository:

```bash
git clone <repository-url>
```

#### Change to the project directory:

```bash
cd django-hasher
```

#### Create and activate a virtual environment:

```bash
Copy code
python3 -m venv venv
source venv/bin/activate
```

#### Install the required dependencies:


```bash
pip install -r requirements.txt
```

#### Run the migrations:

````bash
python manage.py migrate
````

#### Start the development server:

```bash
python manage.py runserver
```

Access the website in your browser at http://localhost:8000.

#### Usage
Open the website in your browser.
Enter the text you want to hash in the provided input field.
Click the "Hash" button.
The generated SHA256 hash will be displayed on the page.
Test-Driven Development (TDD)
This project has been developed using the Test-Driven Development (TDD) approach, which involves writing tests before writing the actual code. The tests ensure the functionality of the website and help catch any potential issues or bugs.

To run the test suite, execute the following command:


```bash
python manage.py test
```
The test suite will run and provide a detailed report on the success of the tests. Any failures or errors will be displayed, indicating areas that require attention.

The TDD approach ensures that the code is thoroughly tested and increases confidence in its correctness. By writing tests first, we have a clear understanding of the expected behavior, which leads to better code quality and more reliable software.

### Contributing
Contributions to Hashthat are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the repository. Feel free to submit pull requests with bug fixes, new features, or enhancements.

License
This project is licensed under the MIT License.

Feel free to customize the content as needed for your project. Make sure to replace <repository-url> with the actual URL of your repository.