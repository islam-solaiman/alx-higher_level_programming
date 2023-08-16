-- script that creates the database hbtn_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- CREAT user_0d_2 IF NOT EXISTS  password should be set to user_0d_2_pwd
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
GRANT ALL ON *.* TO user_0d_2@localhost;
