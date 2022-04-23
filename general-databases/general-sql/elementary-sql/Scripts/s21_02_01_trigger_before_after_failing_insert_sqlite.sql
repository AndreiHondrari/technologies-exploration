
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t1_attempts;
DROP TABLE IF EXISTS t1_successes;

CREATE TABLE IF NOT EXISTS t1 (
    x int CHECK(x > 0 AND x < 100)
);

CREATE TABLE IF NOT EXISTS t1_attempts (
    x_copy int
);

CREATE TABLE IF NOT EXISTS t1_successes (
    x_copy int
);

/*
 * create triggers
 */
DROP TRIGGER IF EXISTS t1_attempt_trigger;
DROP TRIGGER IF EXISTS t1_success_trigger;

-- attempt trigger
CREATE TRIGGER IF NOT EXISTS t1_attempt_trigger
BEFORE INSERT ON t1
BEGIN
    INSERT INTO t1_attempts VALUES (NEW.x);
END;

-- success trigger
CREATE TRIGGER IF NOT EXISTS t1_success_trigger
AFTER INSERT ON t1
BEGIN
    INSERT INTO t1_successes VALUES (NEW.x);
END;

/*
 * do some inserts
 */
INSERT OR IGNORE INTO t1 VALUES
    (-23),
    (0),
    (1),
    (50),
    (555),
    (90),
    (42),
    (9999);

SELECT * FROM t1;
SELECT * FROM t1_attempts;
SELECT * FROM t1_successes;

DROP TRIGGER IF EXISTS t1_attempt_trigger;
DROP TRIGGER IF EXISTS t1_success_trigger;

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t1_attempts;
DROP TABLE IF EXISTS t1_successes;
