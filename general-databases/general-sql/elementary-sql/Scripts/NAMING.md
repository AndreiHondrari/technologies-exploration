# Naming convention for the SQL scripts

## Format

The names of the SQL scripts are formatted as such:
`s <concept_index> _ <subconcept_index> _ <database type index> _ <concept description> _ <database type> .sql`

Where the parts have the following meanings:

- **concept index** - a number denoting a belonging to a specific concept like:
  creating tables, dropping tables, query-ing, etc.

- **subconcept index** - a number denoting a sub-theme of the concept invovled.
  Examples: regular create, create if not exists, regular drop, drop if exists,
  etc.

- **database type index** - for now these are:
  - **1** - sqlite
  - **2** - postgres

- **concept description** - a simple and very short description explaining what
  the script does
- **database type** - _**'sqlite'**_, or _**'postgres'**_

## Simplified format

You could also have:

`s <concept_index> _ <subconcept_index> _ <optional: sqlite/postgres> _ <concept description>.sql`
