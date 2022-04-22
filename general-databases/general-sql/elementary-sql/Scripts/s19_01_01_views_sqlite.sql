
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;

CREATE TABLE IF NOT EXISTS t1 (
    x int,
    descr text
);

CREATE TABLE IF NOT EXISTS t2 (
    a int
);

INSERT INTO t1 VALUES
    (11, 'gandalf'),
    (22, 'GANDHI'),
    (11, 'tree'),
    (11, 'forcefield'),
    (33, 'apples'),
    (66, 'sword'),
    (44, 'magical'),
    (88, 'startdust'),
    (22, 'quadrant'),
    (55, 'freaky'),
    (44, 'equation'),
    (99, 'equation'),
    (22, 'quasimodo'),
    (11, 'perfect'),
    (77, 'broken'),
    (77, 'magnificent'),
    (33, 'insane'),
    (55, 'juggernaut'),
    (55, 'fantasy'),
    (11, 'sorcerer'),
    (22, 'ak47'),
    (11, 'akko'),
    (33, 'akama')
;

INSERT INTO t2 VALUES (11), (33);

/*
 * create some views
 */
DROP VIEW IF EXISTS view1;
CREATE VIEW IF NOT EXISTS view1
AS
    SELECT * FROM t1 
    WHERE x = 11
;

DROP VIEW IF EXISTS view2;
CREATE VIEW IF NOT EXISTS view2
AS
    SELECT t1.*
    FROM t1 INNER JOIN t2
    ON t1.x = t2.a
;

/*
 * use views
 */

-- title: view1
SELECT * FROM view1;

-- title: view2
SELECT * FROM view2;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
