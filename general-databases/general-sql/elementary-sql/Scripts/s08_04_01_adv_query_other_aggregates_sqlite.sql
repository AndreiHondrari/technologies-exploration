/*
 * 
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
	x integer,
	descr varchar(30)
);

INSERT INTO t1 VALUES 
	(111, "gandalf"),
	(444, "tree"),
	(333, "forcefield"),
	(111, "apples"),
	(333, "sword"),
	(333, "magical"),
	(222, "startdust"),
	(111, "quadrant"),
	(444, "equation"),
	(9999, "equation");

-- main start

SELECT MIN(x), MAX(x), ROUND(AVG(x), 2), SUM(x) FROM t1;

-- title: when used with other columns
SELECT MIN(x), descr FROM t1;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;