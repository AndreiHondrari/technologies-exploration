/*
 * We want to place on a single column the value with the highest priority
 * from a set of columns serving the same data
 */

-- setup
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
	a1 integer,
	a2 integer,
	a3 integer
);

INSERT INTO t1 VALUES
	(11, NULL, NULL),
	(22, NULL, NULL),
	(33, 333, NULL),
	(44, 444, 4444),
	(55, NULL, 5555),
	(NULL, 666, NULL),
	(NULL, NULL, 7777);

	
-- main start

-- title: multiplex column
/*
 * Notice how the order matters for priority.
 * First case match, first served.
 */
SELECT
	CASE
		WHEN a3 NOTNULL THEN a3
		WHEN a2 NOTNULL THEN a2
		WHEN a1 NOTNULL THEN a1
	END a
FROM t1;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
