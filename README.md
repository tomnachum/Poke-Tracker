# Pokemon Tracker

## Running instructions

### Initialize the DB

1. run `createDB.sql`
   which creates the poke_tracker DB.

2. run `create_tables.sql`
   which creates 2 tables inside poke_tracker DB:

   - pokemons
   - trainers

3. run `create_pokemons_trainers_table.sql`
   which creates the table "pokemons_trainers" inside poke_tracker DB.

4. run `create_pokemons_types_table.sql`
   which creates the table "pokemons_trainers" inside poke_tracker DB.

5. run `initialize_tables.py`
   which inserts the data from "DB/utils/poke_data.json" to the tables.

### run the server

1. run `server.py`
   which run the server on port 8000

2. go to http://localhost:8000 and start using the pokemonAPI.
