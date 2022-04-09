/*
 * Insert multiple values with one instruction
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
    x integer
);


-- main start

INSERT INTO t1 VALUES (11), (22), (33), (44);  -- insertions happen in a single instruction
SELECT * FROM t1;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;