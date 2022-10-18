USE poke_tracker;
CREATE TABLE pokemons(
    p_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    height INT,
    weight INT
);
CREATE TABLE trainers(
    t_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    town VARCHAR(255)
);
CREATE TABLE types(
    ty_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);