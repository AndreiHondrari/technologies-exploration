/*
 * Delete rows from a table, matching specific criteria
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
	x integer
);


-- main start

INSERT INTO t1 VALUES (11), (22), (33), (44), (55), (66), (77), (88), (99);

-- title: before delete
SELECT * FROM t1;

DELETE FROM t1 WHERE x >= 55;


-- title: after delete
SELECT * FROM t1;


-- main end

-- cleanup
DROP TABLE IF EXISTS t1;