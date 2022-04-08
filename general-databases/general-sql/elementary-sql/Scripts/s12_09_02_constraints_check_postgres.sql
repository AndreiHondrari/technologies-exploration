
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    a int CHECK (a < 100)
);

INSERT INTO t1 VALUES (11);
INSERT INTO t1 VALUES (22);
INSERT INTO t1 VALUES (99);
INSERT INTO t1 VALUES (100);  -- does not make it

SELECT * FROM t1;

DROP TABLE IF EXISTS t1;
