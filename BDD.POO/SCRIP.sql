CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
);
INSERT INTO estudiantes(nombre, edad)
VALUES
('Juan', 20),
('María', 22),
('Pedro', 19);