/*
 * dbeaver is stupid ... it can't process transactions properly
 */
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
  a integer
);

-- insert some initial values
INSERT INTO t1 VALUES (11), (22);

-- title: before
SELECT * FROM t1;

-- insert with transaction

END TRANSACTION; -- for some reason this is needed???
BEGIN TRANSACTION;
  INSERT INTO t1 VALUES (33);
  INSERT INTO t1 VALUES (44);
  INSERT INTO t1 VALUES (55);
COMMIT;

--END TRANSACTION; -- for some reason this is needed???

-- title: after
SELECT * FROM t1;

DROP TABLE IF EXISTS t1;
