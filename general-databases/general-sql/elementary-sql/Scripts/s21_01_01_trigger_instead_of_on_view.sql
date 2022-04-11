
DROP TABLE IF EXISTS t1_inserts;
DROP TABLE IF EXISTS t1_updates;
DROP TABLE IF EXISTS t1_deletes;
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    pk INT NOT NULL,
    descr text,
    
    PRIMARY KEY (pk)
);

CREATE TABLE IF NOT EXISTS t1_inserts (
    pk_ref INT NOT NULL,
    descr text,
    
    FOREIGN KEY (pk_ref) REFERENCES t1(pk)
);

CREATE TABLE IF NOT EXISTS t1_updates (
    pk_ref INT NOT NULL,
    old_descr text,
    new_descr text,
    
    FOREIGN KEY (pk_ref) REFERENCES t1(pk)
);

CREATE TABLE IF NOT EXISTS t1_deletes (
    pk_ref INT NOT NULL,
    FOREIGN KEY (pk_ref) REFERENCES t1(pk)
);

DROP VIEW IF EXISTS t1view;
CREATE TEMP VIEW IF NOT EXISTS t1view
AS
    SELECT * FROM t1
;

/*
 * create insert trigger for view
 */
DROP TRIGGER IF EXISTS t1view_insert_trigger;

CREATE TRIGGER IF NOT EXISTS t1view_insert_trigger
INSTEAD OF INSERT ON t1view
BEGIN
    INSERT INTO t1_inserts VALUES (NEW.pk, NEW.descr);
END;

/*
 * create update trigger for view
 */
DROP TRIGGER IF EXISTS t1view_update_trigger;

CREATE TRIGGER IF NOT EXISTS t1view_update_trigger
INSTEAD OF UPDATE ON t1view
BEGIN
    INSERT INTO t1_updates VALUES (OLD.pk, OLD.descr, NEW.descr);
END;

/*
 * create delete trigger for view
 */
DROP TRIGGER IF EXISTS t1view_delete_trigger;

CREATE TRIGGER IF NOT EXISTS t1view_delete_trigger
INSTEAD OF DELETE ON t1view
BEGIN
    INSERT INTO t1_deletes VALUES (OLD.pk);
END;

/*
 * initial values
 */
INSERT INTO t1 VALUES (1, 'gandalf'), (2, 'dolores ipsum');

-- insert on view
INSERT INTO t1view VALUES (3, 'frieza');

-- update on view
UPDATE t1view SET descr = 'jeff' WHERE pk = 1;

-- delete from view
DELETE FROM t1view WHERE pk = 2;

SELECT * FROM t1;
SELECT rowid, * FROM t1_inserts;
SELECT rowid, * FROM t1_updates;
SELECT rowid, * FROM t1_deletes;


-- cleanup

DROP TRIGGER IF EXISTS t1view_insert_trigger;
DROP VIEW IF EXISTS t1view;

DROP TABLE IF EXISTS t1_inserts;
DROP TABLE IF EXISTS t1_updates;
DROP TABLE IF EXISTS t1_deletes;
DROP TABLE IF EXISTS t1;
