/*
 * In SQLITE by default all fields are nullable, including primary keys
 */
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    pk PRIMARY KEY,
    x UNIQUE
);

INSERT INTO t1(x) VALUES (11), (22), (33);

SELECT * FROM t1;

DROP TABLE IF EXISTS t1;


/*
 * We must specifically enforce not-null constraint on
 * a primary key if we really want that behaviour 
 */
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t2 (
    pk INT PRIMARY KEY NOT NULL,
    x UNIQUE
);

INSERT INTO t2 VALUES (1, 11), (2, 22), (3, 33);
INSERT OR IGNORE INTO t2 VALUES (2, 44);  -- will fail

SELECT * FROM t2;

DROP TABLE IF EXISTS t2;
