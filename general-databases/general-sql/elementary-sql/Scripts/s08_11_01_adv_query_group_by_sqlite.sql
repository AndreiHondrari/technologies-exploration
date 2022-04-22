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
    (578, 577, 'GANDHI'),
    (444, 10, 'tree'),
    (333, 20, 'forcefield'),
    (111, 20, 'apples'),
    (333, 10, 'sword'),
    (333, 50, 'magical'),
    (222, 640, 'startdust'),
    (111, 30, 'quadrant'),
    (255, 255, 'freaky'),
    (444, 1234, 'equation'),
    (9999, 2, 'equation'),
    (111, 101, 'quasimodo'),
    (10567, 2, 'perfect'),
    (20876, 123, 'broken'),
    (30567, 256, 'magnificent'),
    (123777, 2567, 'insane'),
    (257987, 3765, 'juggernaut'),
    (NULL, 5678, 'fantasy'),
    (5678, NULL, 'sorcerer'),
    (455, 455, 'ak47'),
    (566, 566, 'akko'),
    (577, 577, 'akama');

-- main start

-- title: first match
SELECT * FROM t1 WHERE x < 500 GROUP BY x;  -- will always pick the first match for a given grouping

-- title: count for group
SELECT x, COUNT(*) FROM t1 WHERE x < 500 GROUP BY x;

-- title: avg for group
SELECT x, ROUND(AVG(y), 2) FROM t1 WHERE x < 500 GROUP BY x;

-- title: group by multiple
SELECT * FROM t1 WHERE x < 500 GROUP BY x, y;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
