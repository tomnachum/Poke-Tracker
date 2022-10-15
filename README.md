# Pokemon Tracker

## Running instructions

### Initialize the DB

1. run

   ```
   createDB.sql
   ```

   which creates the poke_tracker DB.

2. run

   ```
   create_tables.sql
   ```

   which creates 2 tables inside poke_tracker DB:

   - pokemons
   - trainers

3. run

   ```
   create_linking_table.sql
   ```

   which creates the table "pokemons_trainers" inside poke_tracker DB.

4. run
   ```
   initialize_tables.py
   ```
   which inserts the data from "DB/utils/poke_data.json" to the tables.
