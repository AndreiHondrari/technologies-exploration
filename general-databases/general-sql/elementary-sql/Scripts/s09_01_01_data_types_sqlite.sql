/*
 * 
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

CREATE TABLE IF NOT EXISTS t1 (
    a,
    b INTEGER,
    c REAL,
    d TEXT,
    e BLOB
);

INSERT INTO t1(a) VALUES (11), ('some'), (23.45), (x'ffaa00');

-- title: dynamic type
SELECT a, typeof(a), b, c, d, e FROM t1;


DELETE FROM t1;
INSERT INTO t1(b, c, d, e) VALUES 
    (123, 78.99, 'some text', x'fe7900ff'), 
    ('not int', 'not float', 9999, 'not blob');

-- title: type not enforced
SELECT * FROM t1;

DELETE FROM t1;
INSERT INTO t1(e) VALUES
    (x''),
    (x'0f'),
    (x'fe00'),
    (x'6677ff11');

-- title: blobs
SELECT e FROM t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
