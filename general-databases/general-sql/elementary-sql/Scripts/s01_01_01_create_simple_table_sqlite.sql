/*
 * Create a simple table
 * 
 * Observations:
 * - the second create will yield an error because the table was created in the first instruction
 */

CREATE TABLE some_table (
  k integer,
  d varchar(30)
);

CREATE TABLE some_table (  -- this will fail
  k integer,
  d varchar(30)
);
