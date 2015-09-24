Set Up MySQL
============

To create a MySQL user:
-----------------------

- mysql -h localhost -u root -p

- CREATE USER 'myoflaskapp'@'localhost';

- GRANT ALL PRIVILEGES ON *.* TO 'myoflaskapp'@'localhost';

- ^C

- mysql -u myoflaskapp

To create a database:
---------------------
- CREATE DATABASE BucketList;

To show all databases:
----------------------
- SHOW DATABASES;

To switch a database:
---------------------
- USE BucketList;

To show all tables:
-------------------
- SHOW TABLES FROM BucketList;

To create a table:
------------------
CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));

To show structure of a table:
-----------------------------
DESCRIBE tbl_user;