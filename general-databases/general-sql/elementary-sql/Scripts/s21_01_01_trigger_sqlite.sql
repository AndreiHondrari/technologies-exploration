
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    descr text
);

CREATE TABLE IF NOT EXISTS t2 (
    descr_copy text
);

/*
 * create a trigger
 */
DROP TRIGGER IF EXISTS mytrigger;

CREATE TRIGGER IF NOT EXISTS mytrigger
INSERT ON t1
BEGIN
    INSERT INTO t2 VALUES (NEW.descr);
END;

/*
 * do some inserts
 */
INSERT INTO t1 VALUES ("gandalf"), ("maxime");

SELECT * FROM t1;
SELECT * FROM t2;

DROP TRIGGER IF EXISTS mytrigger;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
