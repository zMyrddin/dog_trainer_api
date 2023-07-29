### R1 - Identification of the problem you are trying to solve by building this particular app

Basically this app will try to solve a dog owner's issue of finding the right trainer with the righ skillset. 

### R2 - Why is it a problem that needs solving?

Well honestly there are a lot of Trainers out there that don't have the required skills. So this could save up everyone's time by laying it out there. People could just reference to this and go "oh, i dont need to check multiple sources of a trainers skills because I could look for it here from one source"

### R3 - Why have you chosen this database system. What are the drawbacks compared to others?

 Honestly, I have chosen this because this is the only one I know. It has strong ACID compliance and ensures data integrity. It has a lot of resource and information. However from research and experience, one of the drawbacks is it's high learning curve. Not that I could compare to a different one at the moment. The readability of data could also be one of it's drawbacks. PSQL is a bit hard to read. Postman could be a bit hard to for the untrained eye but as you go along and use it more you'd get used to it.

 ### R4 - Identify and discuss the key functionalities and benefits of an ORM

#### Key Functionalities and Benefits of an ORM

As a student exploring the world of databases and data management, understanding Object-Relational Mapping (ORM) is essential. ORM is a technique that bridges the gap between object-oriented programming languages and relational databases, making it easier for developers to work with databases using familiar programming paradigms. Here, we will discuss the key functionalities and benefits of using an ORM.

##### 1. Abstraction of Database Operations

ORM abstracts the underlying database operations, allowing developers to interact with the database using high-level programming constructs like classes and objects. Instead of writing raw SQL queries, developers can use ORM methods to create, read, update, and delete (CRUD) records in the database. This abstraction simplifies database interactions, making the code more readable and maintainable.

##### 2. Mapping of Objects to Tables

One of the primary functions of an ORM is to map object-oriented entities to database tables. The ORM defines how each attribute of a class corresponds to a specific column in the database. This mapping is crucial as it allows seamless conversion between objects in the application and rows in the database, enabling efficient data retrieval and manipulation.

##### 3. Query Generation and Optimization

ORMs offer query generation capabilities, automatically generating the necessary SQL queries based on the ORM methods used by developers. This saves developers from the tedious task of crafting SQL statements manually. Furthermore, advanced ORMs can optimize queries by using techniques like lazy loading and prefetching related data, improving database performance and reducing the number of queries executed.

##### 4. Data Validation and Type Conversion

ORMs often provide built-in data validation and type conversion mechanisms. Before data is saved to the database, the ORM validates it based on the defined constraints in the object's model. Additionally, the ORM handles data type conversions between the application's data types and the database's data types, ensuring data integrity and preventing type-related issues.

##### 5. Cross-Database Compatibility

ORMs are designed to work with various database management systems, such as PostgreSQL, MySQL, SQLite, and Oracle. This cross-database compatibility enables developers to switch between databases easily without changing the application's code significantly. It promotes database independence, making it convenient for applications to support multiple database backends.

##### 6. Object-Relational Integrity

Maintaining integrity between the object-oriented model and the relational database is crucial for consistent data management. ORM frameworks implement features like transactions and atomicity to ensure data integrity during complex operations involving multiple database entities. This protects the database from inconsistencies caused by partial updates or failures.

##### 7. Ease of Maintenance and Testing

By using ORM, developers can create more modular and maintainable code. The separation of database operations from the application logic simplifies testing, as developers can mock the ORM methods during unit testing without accessing the actual database. Additionally, ORM-driven applications tend to be more organized and easier to refactor, leading to better code quality.

##### 8. Security and Injection Protection

ORMs help protect applications against common security vulnerabilities like SQL injection. By utilizing parameterized queries and escaping user inputs, ORM frameworks shield the application from potential attacks that manipulate SQL statements. This reduces the risk of data breaches and enhances the security of the application.



 ### R5

#### Customer Endpoints

###### Get All Customers

URL: /customer/
Method: GET
Description: Retrieve a list of all customers in the system.
Authentication: Not required
Response:
Status Code: 200 OK
Body: JSON array containing customer information.

###### Get One Customer

URL: /customer/<int:id>
Method: GET
Description: Retrieve details of a specific customer by ID.
Authentication: Not required
Parameters:
id: Integer (Customer ID)
Response:
Status Code: 200 OK if the customer exists, 404 Not Found otherwise.
Body: JSON object containing customer information.

###### Update Customer

URL: /customer/update/<int:id>
Methods: PUT or PATCH
Description: Update details of a specific customer by ID.
Authentication: Admin access required
Parameters:
id: Integer (Customer ID)
Request Body: JSON object with the following fields (partial update allowed):
customer_name: String (optional)
email: String (optional)
password: String (optional)
Response:
Status Code: 200 OK if the update is successful, 404 Not Found if the customer does not exist, 500 Internal Server Error for other errors.
Body: JSON object containing updated customer information.

###### Delete Customer

URL: /customer/delete/<int:id>
Method: DELETE
Description: Delete a specific customer by ID.
Authentication: Admin access required
Parameters:
id: Integer (Customer ID)
Response:
Status Code: 200 OK if the deletion is successful, 404 Not Found if the customer does not exist, 500 Internal Server Error for other errors.
Body: JSON object with a message confirming the deletion.

#### Trainer Endpoints

##### Get All Trainers

URL: /trainer/
Method: GET
Description: Retrieve a list of all trainers in the system.
Authentication: Not required
Response:
Status Code: 200 OK
Body: JSON array containing trainer information.

##### Get One Trainer

URL: /trainer/<int:id>
Method: GET
Description: Retrieve details of a specific trainer by ID.
Authentication: Not required
Parameters:
id: Integer (Trainer ID)
Response:
Status Code: 200 OK if the trainer exists, 404 Not Found otherwise.
Body: JSON object containing trainer information.

##### Update Trainer

URL: /trainer/update/<int:id>
Methods: PUT or PATCH
Description: Update details of a specific trainer by ID.
Authentication: Admin access required
Parameters:
id: Integer (Trainer ID)
Request Body: JSON object with the following fields (partial update allowed):
trainer_name: String (optional)
email: String (optional)
password: String (optional)
skills: String (optional)
Response:
Status Code: 200 OK if the update is successful, 404 Not Found if the trainer does not exist, 500 Internal Server Error for other errors.
Body: JSON object containing updated trainer information.

##### Delete Trainer

URL: /trainer/delete/<int:id>
Method: DELETE
Description: Delete a specific trainer by ID.
Authentication: Admin access required
Parameters:
id: Integer (Trainer ID)
Response:
Status Code: 200 OK if the deletion is successful, 404 Not Found if the trainer does not exist, 500 Internal Server Error for other errors.
Body: JSON object with a message confirming the deletion.


#### Dog Endpoints

##### Get All Dogs

URL: /dog/
Method: GET
Description: Retrieve a list of all dogs in the system.
Authentication: Not required
Response:
Status Code: 200 OK
Body: JSON array containing dog information.

##### Get One Dog

URL: /dog/<int:id>
Method: GET
Description: Retrieve details of a specific dog by ID.
Authentication: Not required
Parameters:
id: Integer (Dog ID)
Response:
Status Code: 200 OK if the dog exists, 404 Not Found otherwise.
Body: JSON object containing dog information.

##### Add Dog

URL: /dog/new
Method: POST
Description: Add a new dog to the system.
Authentication: User access required
Request Body: JSON object with the following fields:
dog_name: String (required)
size: String (required)
breed: String (required)
Response:
Status Code: 201 Created if the dog is added successfully, 409 Conflict if there is an integrity violation or missing data.
Body: JSON object with a message confirming the addition.

##### Update Dog

URL: /dog/update/<int:id>
Methods: PUT or PATCH
Description: Update details of a specific dog by ID.
Authentication: Admin access required
Parameters:
id: Integer (Dog ID)
Request Body: JSON object with the following fields (partial update allowed):
dog_name: String (optional)
size: String (optional)
breed: String (optional)
Response:
Status Code: 200 OK if the update is successful, 404 Not Found if the dog does not exist, 500 Internal Server Error for other errors.
Body: JSON object containing updated dog information.

##### Delete Dog

URL: /dog/delete/<int:id>
Method: DELETE
Description: Delete a specific dog by ID.
Authentication: Admin access required
Parameters:
id: Integer (Dog ID)
Response:
Status Code: 200 OK if the deletion is successful, 404 Not Found if the dog does not exist, 500 Internal Server Error for other errors.
Body: JSON object with a message confirming the deletion.

#### Course Endpoints

##### Get All Courses

URL: /course/
Method: GET
Description: Retrieve a list of all courses in the system.
Authentication: Not required
Response:
Status Code: 200 OK
Body: JSON array containing course information.

##### Get One Course

URL: /course/<int:id>
Method: GET
Description: Retrieve details of a specific course by ID.
Authentication: Not required
Parameters:
id: Integer (Course ID)
Response:
Status Code: 200 OK if the course exists, 404 Not Found otherwise.
Body: JSON object containing course information.

##### Add Course

URL: /course/new
Method: POST
Description: Add a new course to the system.
Authentication: Admin access required
Request Body: JSON object with the following fields:
course_name: String (required)
description: String (required)
level: String (required)
duration: Integer (required)
cost: Float (required)
trainer_id: Integer (optional)
Response:
Status Code: 201 Created if the course is added successfully, 409 Conflict if there is an integrity violation or missing data.
Body: JSON object with a message confirming the addition.

##### Update Course

URL: /course/update/<int:id>
Methods: PUT or PATCH
Description: Update details of a specific course by ID.
Authentication: Admin access required
Parameters:
id: Integer (Course ID)
Request Body: JSON object with the following fields (partial update allowed):
course_name: String (optional)
description: String (optional)
level: String (optional)
duration: Integer (optional)
cost: Float (optional)
trainer_id: Integer (optional)
Response:
Status Code: 200 OK if the update is successful, 404 Not Found if the course does not exist, 500 Internal Server Error for other errors.
Body: JSON object containing updated course information.

##### Delete Course

URL: /course/delete/<int:id>
Method: DELETE
Description: Delete a specific course by ID.
Authentication: Admin access required
Parameters:
id: Integer (Course ID)
Response:
Status Code: 200 OK if the deletion is successful, 404 Not Found if the course does not exist, 500 Internal Server Error for other errors.
Body: JSON object with a message confirming the deletion.


 ### R6 - ERD of the app

 ERD can be found here: https://drive.google.com/file/d/14HUveSCMzwMyGAWfcm-jqzDxo1j9Zj6A/view?usp=sharing

### R7 Detail any third party services that your app will use

#### Flask:
    Flask is a popular Python web framework that our app relies on to handle HTTP requests and responses. It provides the foundation for building web applications and APIs. Flask is known for its simplicity and ease of use, making it an excellent choice for beginners like us. It allows us to define routes, handle user requests, and return appropriate responses.

#### SQLAlchemy:
    SQLAlchemy is a powerful and flexible Object-Relational Mapping (ORM) library for Python. It simplifies the interaction with databases and allows us to work with Python objects instead of raw SQL queries. This makes it easier for us to manage and manipulate database records. With SQLAlchemy, we can define our models as Python classes and interact with the database in an object-oriented manner.

#### Marshmallow:
    Marshmallow is a data serialization/deserialization library for Python, and it is used in our app for data validation and transformation. We use Marshmallow to define schemas for our models, which specify how data should be formatted when interacting with the API. Marshmallow helps us ensure that data coming from the client is in the expected format and can be easily converted into Python objects.

#### Flask-JWT-Extended:
    Flask-JWT-Extended is a Flask extension that adds support for JSON Web Tokens (JWT) to our app. JWT is a secure way of transmitting information between parties as JSON objects. With Flask-JWT-Extended, we can implement user authentication and manage user sessions using JWT tokens. This allows us to secure our API endpoints and restrict access to certain routes based on user authentication.

#### bcrypt:
    Bcrypt is a password-hashing library used in our app to securely store passwords in the database. It employs a one-way hashing algorithm that adds a layer of security to our user passwords. Bcrypt hashes passwords before storing them in the database, ensuring that even if the database is compromised, user passwords remain protected.

#### PostgreSQL:
    PostgreSQL is a powerful open-source relational database management system that our app uses to store and retrieve data. It provides a robust and scalable solution for managing large datasets. We chose PostgreSQL because it is known for its reliability and support for complex queries.


### R8 Describe your projects models in terms of the relationships they have with each other

#### Customer Model:
    The Customer model represents the customers of our system. Each customer can have multiple dogs. He/she can enroll their dogs one course at a time through the help of an admin. The Customer model has a zero-to-many relationship with the Dog model. This means that a customer can have multiple or Zerodogs.

#### Trainer Model:
    The Trainer model represents the dog trainers in our system. Each trainer can be associated with multiple courses that they will teach as long as they have the skills for it. The Trainer model has a one-to-many relationship with the Course model. This means that a trainer can be assigned to teach multiple courses.

#### Dog Model:
    The Dog model represents the dogs in our system. Each dog belongs to a single customer. The Dog model has a many-to-one relationship with the Customer model. This means that multiple dogs can be owned by the same customer. The dog has a one to one relationship as well with the Course Model. They can only be enrolled at one course at a time.

#### Course Model:
    The Course model represents the training courses offered in our system. Each course is associated with one trainer and one-to-many dogs. The Course model has a many-to-one relationship with the Trainer model and but a one-to-many on the Dog model. This means that a course is taught by one trainer and could training one or many dogs.

### R9 Discuss the database relations to be implemented in your application

#### Customer and Dog (One-to-Many)

    The `Customer` model represents the customers of the application, and the `Dog` model represents the dogs owned by the customers.

    This is a one-to-many relationship because one customer can have multiple dogs, but each dog belongs to only one customer.

    The relationship is established using the `customer_id` foreign key in the `Dog` model, which references the primary key `id` of the `Customer` model.

#### Trainer and Course (One-to-Many)

    The `Trainer` model represents the trainers in the application, and the `Course` model represents the courses conducted by the trainers.

    This is a one-to-many relationship because one trainer can conduct multiple courses (depending on their skillset), but each course is conducted by only one trainer.

    The relationship is established using the `trainer_id` foreign key in the `Course` model, which references the primary key `id` of the `Trainer` model.

#### Dog and Course (Many-to-One)

    The `Dog` model and the `Course` model have a many-to-one relationship, representing the enrollment of dogs in courses.
    
    This is a Many-to-One relationship because a dog could only be enrolled in one class at a time while a Class can accomodate many dogs at a time.

    The relationship is established using the `dog_id` foreign key in the `Course` model, which references the primary key `id` of the `Trainer` model.


### R10 Describe the way tasks are allocated and tracked in your project

    I have used Notion as my project management tool and to manage and track all the tasks. It is kind of like Trello but I already used Trello last time so I figured might as well try a new one. It is quite the same in terms of GUI where you could have cards on it and multiple layers per card.

    Honestly it could be a bit better as the interface isn't really great however it does do the job.

    How I tackled it is I tried to visualize how I would be doing the project and write down the major plot points.
    As I go along and think about it, I also indicate sub points along the way. This goes on and on until I thought it was fine.

    However, as the project goes along, you realize there are more to it than what you wrote so I go back to my management tool and add these new cards in to manage. 

    I have different columns for each step ( actually only 3. If there are some items that I need to go back and check, I move them from done to doing then back to done after i'm finished)

    Here's a screenshot of the platform. As you can see there are 19 cards at Done and it wouldnt really show all the way as it is too many. I feel like I have broken it down to quite a few manageable chunks.

    ![Notion](https://drive.google.com/file/d/14_JtiEzMctIe5IId0k7SoNmcITUKipEt/view?usp=sharing)

