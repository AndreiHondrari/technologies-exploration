DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    val INT
);

INSERT INTO t1 VALUES
    (11), (22), (33), (44), (55);


WITH kek AS (
    SELECT 
        t1.val * 2 AS a, 
        (t1.val + 10) * 3 AS b,
        t1.val * 10 + t1.val * 100 + t1.val * 1000 AS c
    FROM t1
)
SELECT a, c FROM kek;


DROP TABLE IF EXISTS t1;