### R1 - Identification of the problem you are trying to solve by building this particular app

Basically this app will try to solve a dog owner's issue of finding the right trainer with the righ skillset. 

### R2 - Why is it a problem that needs solving?

Well honestly there are a lot of Trainers out there that don't have the required skills. So this coul save up everyones time by laying it out there. People could just reference to this and go "oh, i dont need to check multiple sources of a trainers skills because I could look for it here from one source"

### R3 - Why have you chosen this database system. What are the drawbacks compared to others?

 I honestly have chosen this because this is the only one I know. From research and experience, one of the drawbacks that could be found are it's lack of JSON support. This system will have to rely on Marshmallow in order to be effectively used through flask. 

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



 ### R6 - ERD of the app

 ERD can be found here: https://drive.google.com/file/d/14HUveSCMzwMyGAWfcm-jqzDxo1j9Zj6A/view?usp=sharing