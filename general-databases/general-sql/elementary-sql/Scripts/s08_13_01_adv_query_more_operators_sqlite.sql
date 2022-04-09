/*
 *
 */

-- setup
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x integer,
    y integer,
    descr varchar(30)
);

CREATE TABLE IF NOT EXISTS t2 (
    a integer,
    b integer
);

INSERT INTO t1 VALUES
    (111, 10, "gandalf"),
    (578, 577, "GANDHI"),
    (444, 10, "tree"),
    (333, 20, "forcefield"),
    (111, 20, "apples"),
    (333, 10, "sword"),
    (333, 50, "magical"),
    (222, 640, "startdust"),
    (111, 30, "quadrant"),
    (255, 255, "freaky"),
    (444, 1234, "equation"),
    (9999, 2, "equation"),
    (111, 101, "quasimodo"),
    (10567, 2, "perfect"),
    (20876, 123, "broken"),
    (30567, 256, "magnificent"),
    (123777, 2567, "insane"),
    (257987, 3765, "juggernaut"),
    (NULL, 5678, "fantasy"),
    (5678, NULL, "sorcerer"),
    (455, 455, "ak47"),
    (566, 566, "akko"),
    (577, 577, "akama");

INSERT INTO t2 VALUES
    (NULL, 11),
    (NULL, 123),
    (777, 22),
    (999, 234);
    
-- main start

-- title: (t2) null query
SELECT * FROM t2 WHERE a ISNULL;

-- title: (t2) non-null query
SELECT * FROM t2 WHERE a NOTNULL;

-- title: (t1) in list
SELECT * FROM t1 WHERE x IN (111, 222, 333);

-- title: (t1) not in list
SELECT * FROM t1 WHERE x NOT IN (111, 222, 333) AND x < 1000;

-- title: (t1) between
SELECT * FROM t1 WHERE x BETWEEN 450 and 1000;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
