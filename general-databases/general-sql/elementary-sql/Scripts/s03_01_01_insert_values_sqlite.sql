/*
 * Insert values into a table
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
    x integer
);

-- main start

INSERT INTO t1 VALUES (11);
INSERT INTO t1 VALUES (22);
INSERT INTO t1 VALUES (33);

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;