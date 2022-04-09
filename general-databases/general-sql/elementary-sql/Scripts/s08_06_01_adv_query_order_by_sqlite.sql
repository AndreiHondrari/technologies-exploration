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
    (111, 10, "gandalf"),
    (444, 10, "tree"),
    (333, 20, "forcefield"),
    (111, 20, "apples"),
    (333, 10, "sword"),
    (333, 50, "magical"),
    (222, 640, "startdust"),
    (111, 30, "quadrant"),
    (444, 1234, "equation"),
    (9999, 2, "equation"),
    (111, 101, "quasimodo"),
    (10567, 2, "perfect"),
    (20876, 123, "broken"),
    (30567, 256, "magnificent"),
    (123777, 2567, "insane"),
    (257987, 3765, "juggernaut"),
    (NULL, 5678, "fantasy"),
    (5678, NULL, "sorcerer");

-- main start

-- title: order by default (x)
SELECT * FROM t1 ORDER BY x;

-- title: order by default (y)
SELECT * FROM t1 ORDER BY y;

-- title: order by desc (x)
SELECT * FROM t1 ORDER BY x DESC;

-- title: order by multiple
SELECT * FROM t1 ORDER BY x DESC, y ASC;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;