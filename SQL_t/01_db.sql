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
SELECT * FROM teams;-- tables creation

SELECT * FROM players
WHERE age BETWEEN 25 AND 35;

SELECT * FROM players
WHERE position IN ('Forward', 'Midfilders');

SELECT * FROM players
WHERE NOT team_id=1;

SELECT * FROM players
WHERE team_id IN(1, 2, 3);

SELECT * FROM players
WHERE age BETWEEN 20 AND 30;

SELECT * FROM players
WHERE player_name LIKE 'M%';

SELECT * FROM players
WHERE player_name LIKE '%a%';

SELECT * FROM players
WHERE team_id IS NULL;

SELECT * FROM players
WHERE team_id IS NOT NULL;

SELECT player_name, age,
CASE
WHEN age < 25 THEN 'Young'
WHEN age BETWEEN 25 AND 32 THEN 'EXPERIENCED'
ELSE 'ETERAN'
END AS category
FROM players;

-- COUNT ALL PLAYERS
SELECT COUNT(*) AS total_players
FROM players;

-- Average age of players
SELECT AVG(age) AS average_age
FROM players;

-- OLDEST AND YOUNGEST PLAYER
SELECT MIN(age) AS youngest_player
FROM players;
SELECT MAX(age) AS oldest_player
FROM players;

-- total goal scored
SELECT SUM(goals) AS total_goals
FROM players;

--Players in each position
SELECT position, COUNT(*) AS total_players
FROM players
GROUP BY position;

-- avg age in each position
SELECT position, AVG(age) as average_age
FROM players
GROUP BY position;

--position containing more than 2 players
SELECT position, COUNT(*) AS total_players
FROM players
GROUP BY position
HAVING COUNT(*)>2;

-- total goals scored by players older than 25
SELECT age, SUM(goals) as total_goals
FROM players
GROUP BY age
HAVING age > 25;

-- positions by average age, highest first
SELECT position, AVG(age) as average_age
FROM players
GROUP BY position
ORDER BY average_age DESC;

-- INNER JOIN: RETURNS only records that have matching values in both tables
SELECT players.player_name, teams.team_name
FROM players
INNER JOIN teams
ON players.team_id= teams.team_id;

-- Display all players including those without a team, using LEFT JOIN
SELECT players.player_name, teams.team_name
FROM players
LEFT JOIN teams
ON players.team_id= teams.team_id;

-- Display all teams, including teams without players, using LEFT JOIN
SELECT players.player_name, teams.team_name
FROM teams
LEFT JOIN players
ON players.team_id=teams.team_id;

--Find players who belongs to the ame team using self join
SELECT p1.player_name AS player1, p2.player_name AS player2, t.team_name
FROM players p1
INNER JOIN players p2 
ON p1.team_id=p2.team_id 
WHERE p1.player_id<>p2.player_id;

--Display player names, team names, goals, and assists by joining three tables.
SELECT p.player_name, t.team_name, p.goals, p.assists
FROM players p
INNER JOIN teams t
ON p.team_id=t.team_id
JOIN player_matches pm
ON p.player_id=pm.player_id;

-- Calculate total goal scored by each team
SELECT t.team_name, SUM(p.goals) AS total_goals
FROM teams t
JOIN players p
ON t.team_id=p.team_id
JOIN player_matches pm
ON p.player_id=pm.player_id
GROUP BY t.team_name
ORDER BY total_goals DESC;

-- FInd the number of players in each team
SELECT t.team_name, COUNT(p.player_id) AS total_players
FROM teams t
JOIN players p
ON t.team_id=p.team_id
GROUP BY t.team_name;