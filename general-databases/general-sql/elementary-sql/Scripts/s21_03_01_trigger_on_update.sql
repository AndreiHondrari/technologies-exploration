
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t1_history;

CREATE TABLE IF NOT EXISTS t1 (
    pk INT NOT NULL,
    descr text,
    
    PRIMARY KEY (pk)
);

CREATE TABLE IF NOT EXISTS t1_history (
    pk_ref INT NOT NULL,
    old_descr text,
    new_descr text,
    
    FOREIGN KEY (pk_ref) REFERENCES t1(pk)
);

/*
 * create history recorder trigger
 */
DROP TRIGGER IF EXISTS t1_remember_change_trigger;

CREATE TRIGGER IF NOT EXISTS t1_remember_change_trigger
AFTER UPDATE ON t1
BEGIN

    INSERT INTO t1_history (pk_ref, old_descr, new_descr)
    VALUES (OLD.pk, OLD.descr, NEW.descr);
END;

/*
 * initial values
 */
INSERT INTO t1 VALUES (1, 'gandalf'), (2, 'dolores ipsum');

UPDATE t1 SET descr = 'maxime' WHERE pk = 1;
UPDATE t1 SET descr = 'consectur est' WHERE pk = 2;
UPDATE t1 SET descr = 'jeff' WHERE pk = 1;

SELECT * FROM t1;
SELECT rowid, * FROM t1_history;

DROP TRIGGER IF EXISTS t1_remember_change_trigger;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t1_history;
