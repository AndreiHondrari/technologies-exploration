DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
	a DEFAULT 123,
	b DEFAULT "gandalf",
	c
);

INSERT INTO t1(c) VALUES (9000);

SELECT * FROM t1;

DROP TABLE IF EXISTS t1;
