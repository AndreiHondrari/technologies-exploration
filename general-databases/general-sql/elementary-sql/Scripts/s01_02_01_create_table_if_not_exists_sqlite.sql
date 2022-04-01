/*
 * Create table only if it exists
 * 
 * Observations:
 * - will run without problems because of the IF NOT EXISTS clause
 */

CREATE TABLE IF NOT EXISTS some_table (
  k integer,
  d varchar(30)
);

CREATE TABLE IF NOT EXISTS some_table (
  k integer,
  d varchar(30)
);