-- tables creation
CREATE TABLE teams(
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL,
    city VARCHAR(100)
);
CREATE TABLE players(
    player_id INTEGER PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    age INTEGER,
    position VARCHAR(50),
    team_id INTEGER,
    FOREIGN KEY(team_id)
    REFERENCES teams(team_id)
);

-- insert data
-- INSERT INTO teams(team_id, team_name, city) VALUES
INSERT INTO teams VALUES
(1, 'Barcelona', 'Barcelona'),
(2, 'Real Madrid', 'Madrid'),
(3, 'Manchester City', 'Manchester');

INSERT INTO players VALUES
(101, 'Messi', 39, 'Forward', 1),
(102, 'Pedri', 23, 'Midfielder', 1),
(103, 'Mbappe', 27, 'Forward', 2),
(104, 'Haaland', 26, 'Forward', 3),
(105, 'Bellingham', 22, 'Midfielder', 2);

-- retrieve data
SELECT * FROM teams;
SELECT * FROM players;

-- filter data
SELECT * FROM players WHERE age<30;
SELECT * FROM teams WHERE city='Madrid';

-- sort data
SELECT * 
FROM players
ORDER BY age ASC;

-- top three players by age
SELECT player_name, age
FROM players
ORDER BY age ASC
LIMIT 3;

-- unique positions
SELECT DISTINCT position FROM players;

-- update player's age
UPDATE players
SET age = 40
WHERE player_id= 101;

-- add a goal's column
ALTER TABLE players
ADD COLUMN goals INTEGER DEFAULT 0;

-- UPDATE GOALS
UPDATE players
SET goals= 25
WHERE player_id= 987;

-- delete from player
DELETE FROM players
WHERE player_id=105;

-- FINAL DATA
SELECT * FROM players;
SELECT * FROM teams;