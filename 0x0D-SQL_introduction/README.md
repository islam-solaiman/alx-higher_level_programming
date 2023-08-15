# 0x0D. SQL - Introduction

# Resources

### Read or watch:

[What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)<br>
[A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)<br>
[Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)<br>
[Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)<br>
[SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)<br>
[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)<br>
[What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)<br>
[MySQL Cheat Sheet](https://intranet.alxswe.com/projects/272#quiz-completed)<br>
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)<br>
[installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)<br>

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

	- What’s a database
	- What’s a relational database
	- What does SQL stand for
	- What’s MySQL
	- How to create a database in MySQL
	- What does DDL and DML stand for
	- How to CREATE or ALTER a table
	- How to SELECT data from a table
	- How to INSERT, UPDATE or DELETE data
	- What are subqueries
	- How to use MySQL functions

# Requirements

## General

	- Allowed editors: vi, vim, emacs
	- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
	- All your files should end with a new line
	- All your SQL queries should have a comment just before (i.e. syntax above)
	- All your files should start by a comment describing the task
	- All SQL keywords should be in uppercase (SELECT, WHERE…)
	- A README.md file, at the root of the folder of the project, is mandatory
	- The length of your files will be tested using wc

# More Info

## Comments for your SQL file:

$ cat my\_script.sql<br>
-- 3 first students in the Batch ID=3<br>
-- because Batch 3 is the best!<br>
SELECT id, name FROM students WHERE batch\_id = 3 ORDER BY created\_at DESC LIMIT 3;<br>
$

# Install MySQL 8.0 on Ubuntu 20.04 LTS

$ sudo apt update<br>
$ sudo apt install mysql-server<br>
...<br>
$ mysql --version<br>
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86\_64 ((Ubuntu))<br>
$

## Connect to your MySQL server:

$ sudo mysql<br>
Welcome to the MySQL monitor.  Commands end with ; or \g.<br>
Your MySQL connection id is 11<br>
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)<br>

Copyright (c) 2000, 2021, Oracle and/or its affiliates.<br>

Oracle is a registered trademark of Oracle Corporation and/or its<br>
affiliates. Other names may be trademarks of their respective
owners.<br>

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.<br>

mysql><br>
mysql> quit<br>
Bye<br>
$

# Use “container-on-demand” to run MySQL

### In the container, credentials are root/root

	- Ask for container Ubuntu 20.04
	- Connect via SSH
	- OR connect via the Web terminal
	- In the container, you should start MySQL before playing with it:


$ service mysql start<br>                                                   
 * Starting MySQL database server mysqld <br>
$<br>
$ cat 0-list\_databases.sql | mysql -uroot -p<br>                               
Database<br>                                                                                   
information\_schema<br>                                                                         
mysql<br>                                                                                      
performance\_schema<br>                                                                         
sys<br>                      
$
