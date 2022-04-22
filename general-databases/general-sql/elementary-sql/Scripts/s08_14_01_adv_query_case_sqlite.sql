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

-- title: case in select
SELECT 
    DISTINCT(x),
    CASE
        WHEN x < 500 THEN 'kek'
        WHEN x >= 500 THEN 'lol'
    END woot
FROM t1
WHERE x NOTNULL AND x BETWEEN 300 AND 10000
ORDER BY x;

-- title: case in where
SELECT * FROM t1
WHERE
    x <= 500 AND
    CASE 
        WHEN x < 300 THEN y <= 50
        WHEN x >= 300 THEN y > 50
    END
ORDER BY x, y;

-- title: case in group by
/*
 * Doing it with subquery because 
 */
SELECT 
    -- show only x if x < 500
    CASE 
        WHEN x_original < 500 THEN x_original
        WHEN x_original >= 500 THEN NULL
    END x,
    
    -- show only y if x is >= 500
    CASE 
        WHEN x_original < 500 THEN NULL
        WHEN x_original >= 500 THEN y_original
    END y
FROM (
    -- query for relevant x and y, and ordered
    SELECT 
        x AS x_original,
        y AS y_original
    FROM t1
    WHERE x NOTNULL and y NOTNULL
    ORDER BY x, y
)
GROUP BY
    -- make sure to group only by non null values
    CASE
        WHEN x_original NOTNULL THEN x_original
        WHEN y_original NOTNULL THEN y_original 
    END
;

-- main end

-- cleanup
DROP TABLE IF EXISTS t1;
