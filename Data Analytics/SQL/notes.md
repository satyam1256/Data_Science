# SQL Introduction

SQL (Structured Query Language) is a programming language used for storing, manipulating, and retrieving data in a relational database.

SQL is the standard language for Relational Database Management Systems (RDBMS). Popular RDBMSs such as MySQL, MS Access, Oracle, Sybase, Informix, Postgres, and SQL Server use SQL as their standard database language.

## SQL Process

When a SQL command is executed in any RDBMS, the system determines the best way to carry out the command. The SQL engine figures out how to interpret the task.

Components involved in this process include:

- Query Dispatcher
- Optimization Engines
- Classic Query Engine
- SQL Query Engine

**Note:** A classic query engine handles all non-SQL queries, but a SQL query engine won't handle logical files.

### DBMS Process Flow

## SQL Commands

The standard SQL commands to interact with relational databases are `CREATE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `DROP`. These commands can be classified into the following groups based on their nature:

### DDL - Data Definition Language

DDL deals with database schemas and descriptions of how data should reside in the database.

- **CREATE**: Creates a new table, view, or other objects in the database.
- **ALTER**: Modifies an existing database object, such as a table.
- **DROP**: Deletes an entire table, a view, or other objects in the database.
- **TRUNCATE**: Removes all records from a table, including all spaces allocated for the records.
- **COMMENT**: Adds comments to the data dictionary.
- **RENAME**: Renames an object.

### DML - Data Manipulation Language

DML deals with data manipulation and includes the most common SQL statements such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc. It is used to store, modify, retrieve, delete, and update data in a database.

- **SELECT**: Retrieves records from one or more tables.
- **INSERT**: Creates a record.
- **UPDATE**: Modifies records.
- **DELETE**: Deletes records.
- **MERGE**: Performs an UPSERT operation (insert or update).
- **CALL**: Calls a PL/SQL or Java subprogram.
- **EXPLAIN PLAN**: Provides an interpretation of the data access path.
- **LOCK TABLE**: Controls concurrency.

### DCL - Data Control Language

DCL includes commands such as `GRANT` and is mostly concerned with rights, permissions, and other controls of the database system.

- **GRANT**: Grants privileges to a user.
- **REVOKE**: Removes granted privileges from a user.

### TCL - Transaction Control Language

TCL deals with transactions within a database.

- **COMMIT**: Commits a transaction.
- **ROLLBACK**: Rolls back a transaction in case of an error.
- **SAVEPOINT**: Creates points within groups to roll back transactions.
- **SET TRANSACTION**: Specifies the characteristics of a transaction.

## SQL Command Help

### ALTER TABLE

`ALTER TABLE` lets you add columns to a table in a database.

```sql
ALTER TABLE table_name ADD column_name datatype;
```

### AS

`AS` is a keyword that allows you to rename a column or table using an alias.

```sql
SELECT column_name AS 'Alias' FROM table_name;
```

### AVG()

`AVG()` is an aggregate function that returns the average value for a numeric column

```sql
SELECT AVG(column_name) FROM table_name;

```

### BETWEEN

The `BETWEEN` operator is used to filter the result set within a certain range. The values can be numbers, text, or dates.

```sql
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value_1 AND value_2;

```

### CASE

`CASE` statements are used to create different outputs, usually in the `SELECT` statement. It is SQL's way of handling if-then logic.

```sql
SELECT column_name,
  CASE
    WHEN condition THEN 'Result_1'
    WHEN condition THEN 'Result_2'
    ELSE 'Result_3'
  END
FROM table_name;

```
