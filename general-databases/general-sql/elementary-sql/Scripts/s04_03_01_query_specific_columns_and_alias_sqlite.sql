/*
 * Query - filtered
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
    x integer,
    y integer
);

INSERT INTO t1 VALUES (11, 233);
INSERT INTO t1 VALUES (22, 244);
INSERT INTO t1 VALUES (33, 344);
INSERT INTO t1 VALUES (44, 355);
INSERT INTO t1 VALUES (55, 466);
INSERT INTO t1 VALUES (66, 477);
INSERT INTO t1 VALUES (77, 588);
INSERT INTO t1 VALUES (88, 599);
INSERT INTO t1 VALUES (99, 600);

-- main start

-- title: select only x
SELECT x FROM t1;

-- title: alias columns
SELECT
    x AS this,
    y AS that
FROM t1;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;