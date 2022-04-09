DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    a, b, c
);

INSERT INTO t1 VALUES
    (NULL, NULL, NULL),
    (NULL, NULL, 11),
    (NULL, 22, NULL),
    (33, NULL, NULL),
    (NULL, 44, 55),
    (66, 77, NULL),
    (88, NULL, 99)
;

SELECT *, coalesce(a, b, c) FROM t1;


DROP TABLE IF EXISTS t1;