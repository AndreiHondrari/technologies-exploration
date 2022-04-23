DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    a NOT NULL, 
    b NOT NULL,
    k,
    
    PRIMARY KEY (a, b)
);

INSERT INTO t1 VALUES
    (1, 11, 'blabla'),
    (2, 22, 'gandalf');

INSERT INTO t1 VALUES (1, 33, 'maxime');
INSERT OR IGNORE INTO t1 VALUES (2, 22, 'cassidi'); -- will fail

SELECT * FROM t1;


DROP TABLE IF EXISTS t1;
