/*
 * 
 */

-- setup
DROP TABLE IF EXISTS t1;
CREATE TABLE IF NOT EXISTS t1 (
    x integer,
    y integer,
    descr varchar(30)
);

INSERT INTO t1 VALUES 
    (111, 10, 'gandalf'),
    (444, 10, 'tree'),
    (333, 20, 'forcefield'),
    (111, 20, 'apples'),
    (333, 10, 'sword'),
    (333, 50, 'magical'),
    (222, 640, 'startdust'),
    (111, 30, 'quadrant'),
    (444, 1234, 'equation'),
    (9999, 2, 'equation'),
    (111, 101, 'quasimodo'),
    (10567, 2, 'perfect'),
    (20876, 123, 'broken'),
    (30567, 256, 'magnificent'),
    (123777, 2567, 'insane'),
    (257987, 3765, 'juggernaut');

-- main start

-- title: and
SELECT * FROM t1 WHERE x = 111 AND y > 100;

-- title: or
SELECT * FROM t1 WHERE x > 1000 OR y > 100;

-- title: or + and
SELECT * FROM t1 WHERE x < 1000 AND y = 50 OR x > 1000 AND y <= 10;

-- title: associative or + and
SELECT * FROM t1 WHERE x > 1000 AND (y < 100 OR y > 1000);

-- title: not
SELECT * FROM t1 WHERE NOT x = 111 AND NOT x = 333 AND x < 1000;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;