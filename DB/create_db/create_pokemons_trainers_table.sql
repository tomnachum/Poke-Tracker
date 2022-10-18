USE poke_tracker;
CREATE TABLE pokemons_trainers(
    p_id INT,
    t_id INT,
    PRIMARY KEY (p_id, t_id),
    FOREIGN KEY(p_id) REFERENCES pokemons(p_id),
    FOREIGN KEY(t_id) REFERENCES trainers(t_id)
);