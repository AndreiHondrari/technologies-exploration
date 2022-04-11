
DROP TABLE IF EXISTS t1_abscess;
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    pk INT NOT NULL,
    level int,

    PRIMARY KEY (pk)
);

CREATE TABLE IF NOT EXISTS t1_abscess (
    pk_ref INT NOT NULL,
    abscess_level int,

    FOREIGN KEY (pk_ref) REFERENCES t1(pk)
);

/*
 * create conditional trigger
 */
DROP TRIGGER IF EXISTS t1_abscess_trigger;

CREATE TRIGGER IF NOT EXISTS t1_abscess_trigger
AFTER INSERT ON t1
WHEN NEW.level > 100 -- NOTICE the condition
BEGIN
    INSERT INTO t1_abscess(pk_ref, abscess_level)
    VALUES (NEW.pk, NEW.level);
END;

INSERT INTO t1 VALUES
    (1, 0), 
    (2, 1), 
    (3, 12), 
    (4, 127), 
    (5, 100),
    (6, 90),
    (7, 245),
    (8, 42)
;

SELECT * FROM t1;
SELECT rowid, * FROM t1_abscess;

DROP TRIGGER IF EXISTS t1_abscess_trigger;

DROP TABLE IF EXISTS t1_abscess;
DROP TABLE IF EXISTS t1;
