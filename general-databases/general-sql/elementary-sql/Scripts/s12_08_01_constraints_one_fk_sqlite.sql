
-- must be on for FK to work
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    /*
     * must be unique otherwise
     * it can't be referenced as FK
     */
    a integer unique,
    b varchar
);

CREATE TABLE IF NOT EXISTS t2 (
    t1a integer,

    FOREIGN KEY (t1a) REFERENCES t1(a)
);

INSERT INTO t1 VALUES
    (11, 'gandalf'),
    (22, 'maxime'),
    (33, 'cassidi'),
    (44, 'jeff');

INSERT INTO t2 VALUES
    (11), (11), (11), (44);

/*
 * silently 'fail' the insertion if
 * the foreign key does not reference
 * something actually existing
 */
INSERT INTO t2
SELECT 77
WHERE EXISTS (SELECT * FROM t1 WHERE a = 77); -- should fail

SELECT * FROM t1;
SELECT * FROM t2;

DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t1;
