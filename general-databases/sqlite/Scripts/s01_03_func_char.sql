DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    c1, c2, c3, c4
);

INSERT INTO t1 VALUES
    (97, 98, 99, 100)
;

SELECT *, char(c1, c2, c3, c4) FROM t1;


DROP TABLE IF EXISTS t1;