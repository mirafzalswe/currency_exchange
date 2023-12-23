#Currency Exchange
## Have a nice Reading


> This project is for currency exchange.

![image](https://github.com/mirafzal114/currency_exchange/assets/136591233/84ba68b4-5247-499e-9d58-9071b99b0c01)


![image](https://github.com/mirafzal114/currency_exchange/assets/136591233/7a96c062-2b4e-413a-bc7e-a424e6236cc1)

![image](https://github.com/mirafzal114/currency_exchange/assets/136591233/60c7e443-8a87-4f9f-b0e4-43b1017b6365)



**A sample program works like this.




## Installation and Usage

## Project using pipenv
### The first thing you need to do is to work with pipenv


This project uses the pipenv tool to manage dependencies and the Python virtual environment.


### Installing pipenv


1. Make sure Python is installed on your computer.
2. Install pipenv using the command:
    ```
    $ pip install pipenv
    ```
3. Install dependencies by running ``pip install -r requirements.txt``


### Cloning the project and installing dependencies


1. Clone the repository:
    ```
    $ git clone https://github.com/mirafzal114/currency_exchange.git
    ```
2. Access the repository:
    ```
    $ cd currency_exchange
    ```


3. Run the `pipenv install` command to create a virtual environment and install all dependencies from the `Pipfile.lock` file.


### Working with the project


- To activate the virtual environment, run:
    ```
    pipenv shell
    ```
- To install new dependencies run:
    ```
    pipenv install <package_name>
    ```
- To run scripts or an application from your project, use ``pipenv run``.




**When you are in the `(currency_exhange) currency_exchange` environment, you will have this view.


````bash
$ python manage.py makemigrations
````

**This will create all the migration (database migration) files needed to run this application.**


**To apply this migration, run the following command**
```bash
$ python manage.py migrate
```
**One final step, and then our application will be running. We need to create an admin user to run this application. Type the following command in the terminal and provide a username, password, and email address for the admin user.**
```bash
$ python manage.py createsuperuser
```
 **Start the program using the command:**
````bash
$ python manage.py runserver
````


4. Exit the environment:
    ````bash
    $ exit
    ````


## Project using Docker
### Now if you have Docker, see the project to use it with.


This project uses Docker to manage its environment. To run it locally, follow these steps:


### Steps to start the project


### Install Docker


1. Make sure you have Docker installed on your computer.
2. If Docker is not installed, you can download it [from here](https://docs.docker.com/get-docker/) and install it according to the instructions for your operating system.


### Start the project
### We have already entered the repositories with `pipenv` before, now we will continue with the next one, but you first enter your `Docker Desktop` application if you do not have `Linux` of course:
1. Create a Docker image by running the command: 
    ```
    $ docker build -t currency:1.0 .
    ```

2. Once the image has been successfully created, start the container: 
    ```
    $ docker run -p 1212:8000 currency:1.0
    ```
3. Check ``Dockerfile`` if you do not have an image download from ``Docker Hub``:
    ````bash
    $ docker pull python:3.11-alpine
    ````




Your project should now be available in your browser at `https://localhost:1212/`. 




5. Home Page:
    ```
    https://localhost:1212/
    ```
## Project home page. ##




## A project without Docker
### You can use it without Docker




1. Log in to the environment:
    ```bash
    $ pipenv shell
    ```
2. Enter the command:
    ````bash
    $ python manage.py runserver
    ````

    ## Contribution
**If you would like to contribute to the development of the application please follow these steps:**

1. Fork the repository on GitHub.
2. Clone the fork repository to your local machine.
3. Create a new branch for your feature or fix bugs.
4. Make changes and commits with descriptions of such messages.
5. Push changes to the fork repository.
6. Create a pull request (pull request) on the main repository.

   ## Contacts
**If you have questions or suggestions regarding the application, please contact us at mirafzaaal2609@gmail.com. We value your opinion!**

