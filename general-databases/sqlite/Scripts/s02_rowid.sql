/*
 * all sqlite tables have a special rowid column by default 
 */
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    x
);

INSERT INTO t1 VALUES (11), (22), (33);

-- title: rowid_sample
SELECT rowid, * FROM t1;

DROP TABLE IF EXISTS t1;

/*
 * the rowid can be omitted but
 * mandatorily a primary key 
 * must be specified on the table
 */
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t2 (
    pk PRIMARY KEY,  -- must be here otherwise it won't work
    x
) WITHOUT ROWID; -- notice the notation

INSERT INTO t2 VALUES (1, 11), (2, 22), (3, 33);

DROP TABLE IF EXISTS t2;