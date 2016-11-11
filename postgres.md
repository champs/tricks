#Postgres
##Function
```
	-- Function increments the input value by 1
   CREATE OR REPLACE FUNCTION increment(i INT) RETURNS INT AS $$
    BEGIN
      RETURN i + 1;
    END;
    $$ LANGUAGE plpgsql;
 
    -- An example how to use the function (Returns: 11)
    SELECT increment(10);
```
| Tables        | Stored Procedure	| Function  |
| ------------- |:-------------:		| -----:|
| expression    | False 		  		| True  |
| Return Value  | False      			| True|
| Return Value out  | True       		| False|
| Return Single result set  | True 	| True|
| Return Multiple result sets  | True      			| False|

####If/Case Statement
```
IF condition THEN
   statement;
END IF;

CASE
    WHEN boolean-expression-1 THEN
      statements
  [ WHEN boolean-expression-2 THEN
      statements
    ... ]
  [ ELSE
      statements ]
END CASE;

```


ps. you can overload the function name as long as parameters are different
##Stored Procedure

####Advantage
* Reduce Number of round trips between db and application.
* Increase application performance, user defined function is pre-compiled and stored in the DB
* Reuse in many applications.

####Disadvantage
* Slow in software dev.
* difficult to manage version/debug
* not portable to other db management system.

```
CREATE FUNCTION function_name(p1 type, p2 type)
 RETURNS type AS
BEGIN
 -- logic
END;
LANGUAGE language_name;
```

##Trigger
> Trigger is a function that is invoked automatically whenever an even (INSERT, UPDATE, DELETE, TRUNCATE) occurs.
