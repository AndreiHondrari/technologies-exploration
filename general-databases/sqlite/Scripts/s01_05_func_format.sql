DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
	a, b, c
);

INSERT INTO t1 VALUES
	(111, 10, "gandalf"),
	(444, 10, "tree"),
	(333, 20, "forcefield"),
	(111, 20, "apples"),
	(333, 10, "sword"),
	(333, 50, "magical"),
	(222, 640, "startdust"),
	(111, 30, "quadrant"),
	(255, 255, "freaky")
;

SELECT printf("%d KEK %.2f LOL %s", a, b, c) FROM t1;


DROP TABLE IF EXISTS t1;