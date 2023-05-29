
-- must be on for FK to work
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
    /*
     * must be unique otherwise
     * it can't be referenced as FK
     */
    a integer,
    b integer,
    msg varchar,
    
    constraint ab_uniq unique (a, b)
);

CREATE TABLE IF NOT EXISTS t2 (
    t1_a integer,
    t1_b integer,
    
    constraint t1_fks FOREIGN KEY (t1_a, t1_b) REFERENCES t1(a, b)
);

INSERT INTO t1 VALUES 
    (11, 1000, 'aaa'),
    (22, 1000, 'bbb'),
    (11, 2000, 'ccc'),
    (22, 2000, 'ddd'),
    (33, 3000, 'eee'),
    (44, 3000, 'fff');
    
select * from t1;

insert into t2 values
    (11, 1000),
    (33, 3000);

insert into t2 values (11, 3000);  -- will FAIL because FK is not satisfied

select * from t2;

DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t1;
