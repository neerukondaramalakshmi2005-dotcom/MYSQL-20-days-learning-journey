Day-2
========
What is data, field, record, database?
--------------------------------------------
What is Data?
------------------
raw facts or figures without context.
example: 101,Ravi,50000,hyd

What is the field?
---------------
smallest unit of data in a database(column/attribute)
example: EmpName,EmpId,EmpSalary,EmpAddress

What is Record ?
--------------
collection of related fields(row/tuple)
example :(111,ravi,60000,vjy)

What is a database ?
-------------------
organized collection of related records stored together.
example : an employee database containing all employee records.


Client-server
------------------
client : the role of the client in client-server architecture is to send requests to the server. and to get a response from the server.

Server : - server is software the role of the server in client-server arch is to take requests from clients.
if the request is a valid request then it will generate some response we can handover that response to the client. If the client request is not a valid request then it will raise the errors.

protocol :- it has a set of rules and regulations. The role of the protocol in client-server arch is to send requests from client to server.

Data Models In DBMS
=========================
def : a Data Model defines how data is stored, organized, and manipulated in a database.

1. Physical Data Model
==========================
def: describes how data is physically stored in storage devices.

Audience :  Database administrators.

2. Logical Data Model
--------------------------
defines the structure of data (entities,attributes,relationships) independent of physical storage areas.

Audience : Developers and data architects.

3. Hierarchal Data Model :
--------------------------------
data is represented as tree Structure(parent child relationship)
example :- company-->departments-->employees

4. Network Data Model :
-----------------------
Data is represented as graph with records(nodes)and relationships(edges)

example : student enrolled in multiple courses, courses tough by multiple professors.

5. Relational Data Models(RDBMS)
--------------------------------------
data is stored in tables(relations)with rows(tuples)and columns(attributes)

example
----------
student(id,name,marks,age,dept_id)
department(dept_id,dept_name)

6. Entity Relationship(E-R Model)
-------------------------------------
a conceptual model that shows entities(things),attributes(properties)and relationships

MySQL Installation
---------------------------
https://dev.mysql.com/downloads/installer/

after installation go to location

just double click ---> choose the yes option.

4 option
server
client
full
custom ---> choose custom option--> choose next button

it will show available products
such as
MySQL server
application
documentation

go to my sql server

https://tinyurl.com/MySQL-Batch-03

SQL Identifiers
----------------

SQL identifiers are names used to identify database objects such as.
Database names, Table names, Column names, view names, index names, constraints, triggers, stored procedures.

While we are declaring an identifier we have to follow some rules and regulations.

1. the only allowed characters to declare identifiers a-z or A-Z or 0-9,_,$
2. must begin with a letter or underscore(_).
3. we can't declare identifiers with reserved keywords.
4. spaces are not considered to declare identifiers.
5. identifiers are case sensitive
6. max length to declare identifiers are 15 characters.


SQL (Structured Query Language) commands are broadly classified into five main categories based on their functionality: DDL, DML, DQL, DCL, and TCL. Each category and every command within it is explained below with its purpose and usage.
Command
Description / Definition
DDL
Data Definition Language - defines and modifies the structure of database objects (tables, schemas, indexes).
DML
Data Manipulation Language - manages data stored within database objects (insert, update, delete).
DQL
Data Query Language - used to fetch/retrieve data from the database.
DCL
Data Control Language - manages permissions and access control on database objects.
TCL
Transaction Control Language - manages transactions to maintain data integrity.


 
1. DDL - Data Definition Language
DDL commands are used to define, create, alter, and remove the structure of database objects such as tables, schemas, and indexes. Changes made by DDL commands are auto-committed and permanent.
Command
Description / Definition
CREATE
Creates a new database object such as a table, database, view, index, or schema. Example: CREATE TABLE Students (ID INT, Name VARCHAR(50));
ALTER
Modifies the structure of an existing database object, such as adding, deleting, or modifying columns in a table. Example: ALTER TABLE Students ADD Email VARCHAR(100);
DROP
Permanently deletes an existing database object (table, database, index, view) along with all its data and structure. This action cannot be rolled back in most databases.
TRUNCATE
Removes all rows/records from a table quickly while keeping the table structure intact for future use. Faster than DELETE as it does not log individual row deletions.
RENAME
Renames an existing database object, such as a table or column, to a new name without changing its structure or data.
COMMENT
Adds explanatory notes or comments to database objects (tables, columns) for documentation purposes; does not affect data or structure.

2. DML - Data Manipulation Language
DML commands are used to insert, update, delete, and manage data stored inside existing database tables. Unlike DDL, DML changes can typically be rolled back if not committed.
Command
Description / Definition
INSERT
Adds new rows/records of data into a table. Example: INSERT INTO Students (ID, Name) VALUES (1, 'Ravi');
UPDATE
Modifies existing records in a table by changing the values of one or more columns based on a specified condition. Example: UPDATE Students SET Name='Kumar' WHERE ID=1;
DELETE
Removes one or more existing rows from a table based on a specified condition, while keeping the table structure. Can be rolled back if used within a transaction.
MERGE
Combines INSERT, UPDATE, and DELETE operations into a single statement by comparing source and target tables (also called an 'upsert').
CALL
Invokes or executes a stored procedure to perform a set of predefined operations.
EXPLAIN PLAN
Describes the access path or execution plan that the database will use to run a given SQL statement, used mainly for performance tuning.
LOCK TABLE
Controls concurrency by locking a table to restrict access from other transactions while it is being modified.

3. DQL - Data Query Language
DQL consists of commands used purely to query and retrieve data from one or more tables without modifying it.
Command
Description / Definition
SELECT
Retrieves data from one or more tables or views based on specified columns and conditions. It is the most frequently used SQL command. Example: SELECT Name FROM Students WHERE ID=1;


 
4. DCL - Data Control Language
DCL commands deal with the rights, permissions, and other access controls of the database system, determining which users can access or manipulate data.
Command
Description / Definition
GRANT
Gives specific privileges or permissions (such as SELECT, INSERT, UPDATE, DELETE) to a database user or role. Example: GRANT SELECT ON Students TO User1;
REVOKE
Removes previously granted privileges or permissions from a database user or role, restricting their access to database objects.

5. TCL - Transaction Control Language
TCL commands manage transactions within a database to ensure data integrity, consistency, and to group DML statements into logical units of work.
Command
Description / Definition
COMMIT
Permanently saves all changes made during the current transaction to the database, making them visible to other users.
ROLLBACK
Undoes/reverts changes made during the current transaction back to the last committed state or a savepoint, in case of an error.
SAVEPOINT
Sets a temporary marker within a transaction to which you can later roll back, without undoing the entire transaction.
SET TRANSACTION
Defines properties for a transaction, such as its isolation level, to control how it interacts with other concurrent transactions.
RELEASE SAVEPOINT
Removes a previously created savepoint from the current transaction, freeing associated resources.

Note: Some references also group SELECT under DML instead of a separate DQL category, and command availability/syntax may vary slightly across database systems (MySQL, PostgreSQL, Oracle, SQL Server).




mysql> show databases;
+------------------------+
| Database               |
+------------------------+
| information_schema     |
| jeevan_raksha_pharmacy |
| mysql                  |
| performance_schema     |
| sys                    |
+------------------------+
5 rows in set (0.08 sec)

mysql> CREATE DATABASE PFS3;
Query OK, 1 row affected (0.06 sec)

mysql> SHOW DATABASES;
+------------------------+
| Database               |
+------------------------+
| information_schema     |
| jeevan_raksha_pharmacy |
| mysql                  |
| performance_schema     |
| pfs3                   |
| sys                    |
+------------------------+
6 rows in set (0.00 sec)

mysql> USE PFS3;
Database changed
mysql> CREATE TABLE EMPLOYEES(
    -> EMPID CHAR(5),
    -> FNAME VARCHAR(100),
    -> LNAME VARCHAR(30),
    -> AGE INT,
    -> DOJ DATE,
    -> ADDRESS TINYTEXT,
    -> DEPT VARCHAR(20)
    -> );
Query OK, 0 rows affected (0.27 sec)

mysql> ^C
mysql> -- TO SHOW THE TABLE DESCRIPTION
mysql> DESC EMPLOYEES;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| EMPID   | char(5)      | YES  |     | NULL    |       |
| FNAME   | varchar(100) | YES  |     | NULL    |       |
| LNAME   | varchar(30)  | YES  |     | NULL    |       |
| AGE     | int          | YES  |     | NULL    |       |
| DOJ     | date         | YES  |     | NULL    |       |
| ADDRESS | tinytext     | YES  |     | NULL    |       |
| DEPT    | varchar(20)  | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
7 rows in set (0.02 sec)

mysql> SHOW COLUMNS FROM EMPLOYEES;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| EMPID   | char(5)      | YES  |     | NULL    |       |
| FNAME   | varchar(100) | YES  |     | NULL    |       |
| LNAME   | varchar(30)  | YES  |     | NULL    |       |
| AGE     | int          | YES  |     | NULL    |       |
| DOJ     | date         | YES  |     | NULL    |       |
| ADDRESS | tinytext     | YES  |     | NULL    |       |
| DEPT    | varchar(20)  | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
7 rows in set (0.00 sec)







