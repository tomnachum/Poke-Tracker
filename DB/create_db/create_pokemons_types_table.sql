USE poke_tracker;
CREATE TABLE pokemons_types(
    p_id INT,
    ty_id INT,
    PRIMARY KEY (p_id, ty_id),
    FOREIGN KEY(p_id) REFERENCES pokemons(p_id),
    FOREIGN KEY(ty_id) REFERENCES types(ty_id)
);