DROP INDEX IF EXISTS idx_t1_some;

DROP TABLE IF EXISTS t1;

-- create table
CREATE TABLE IF NOT EXISTS t1 (
    pk int NOT NULL,
    something text NOT NULL,
    val int NOT NULL,
    
    PRIMARY KEY (pk)
);

-- put some values
INSERT INTO t1 VALUES
    (1, 'lorem ipsum', 111),
    (2, 'consectur sigitur', 111),
    (3, 'kaelus est', 222);

/*
 * index on single column
 */
CREATE INDEX idx_t1_some ON t1(something);

EXPLAIN QUERY PLAN
SELECT * FROM t1 WHERE something = 'kaelus est' AND val = 222;

/*
 * index on multiple columns
 */
CREATE INDEX idx_t1_kek ON t1(something, val);

EXPLAIN QUERY PLAN
SELECT * FROM t1 WHERE something = 'kaelus est' AND val = 222;

-- cleanup
DROP INDEX IF EXISTS idx_t1_some;
DROP INDEX IF EXISTS idx_t1_kek;
DROP TABLE IF EXISTS t1;
