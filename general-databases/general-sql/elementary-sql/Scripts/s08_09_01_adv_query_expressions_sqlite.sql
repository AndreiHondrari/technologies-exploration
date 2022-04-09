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

-- main start

-- title: sample 1
SELECT y, y * 2 as changed_y FROM t1;

-- title: sample 2
SELECT x, x % 1000 as changed_x FROM t1;


-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
