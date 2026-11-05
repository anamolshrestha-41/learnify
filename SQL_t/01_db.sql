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

-- Find players older than the avg age
SELECT player_name, age FROM players
WHERE age > (SELECT AVG(age) FROM players );

-- Find players belonginig to Barca or Real Madrid  using IN
SELECT player_name FROM players
WHERE team_id IN(
    SELECT team_id FROM teams
    WHERE team_name IN ('BARCA', 'REAL MADRID')
);

--Find teams that have at least one player using EXISTS
SELECT team_name FROM teams t WHERE EXISTS(
    SELECT 1 FROM players p
    WHERE p.team_id=t.team_id
);

-- Find players older than the avg age of their position
SELECT player_name, age, position 
FROM players p
    WHERE age>(
        SELECT AVG(age) FROM players
        WHERE position=p.position
    );

-- Use a CTE to calculate avg player age.
WITH avg_age AS(
    SELECT AVG(age) AS average_age
    FROM players
)
SELECT player_name, age FROM players
WHERE age > (SELECT average_age FROM avg_age);

-- USE two CTEs to find players who scored more than 10 goals
WITH player_goals AS (
    SELECT player_id, SUM(goals) AS total_goals
    FROM player_matches
    GROUP BY player_id
),
high_score AS(
    SELECT * FROM player_goals
    WHERE total_goals>10
)
SELECT p.player_name, hg.total_goals
FROM high_score hg
JOIN players p
ON hg.player_id=p.player_id;

-- Combine player and team names using UNION
SELECT player_name AS name FROM players
UNION
SELECT team_name AS name FROM teams;

-- REPEAT USING UNION ALL
SELECT player_name as name FROM players
UNION ALL
SELECT team_name AS name FROM teams;

-- Find common name using intersect
SELECT player_name AS name FROM players
INTERSECT
SELECT team_name AS name FROM teams;

-- Find player names that do not appear in the team names using EXCEPT
SELECT player_name AS name FROM players
EXCEPT
SELECT team_name AS name FROM teams;

-- display every player with overall avg goals
SELECT player_name, goals, AVG(goals) OVER() AS overall_avg_goals FROM players;

-- calculate avg goals by position using partition by
SELECT player_name, position, goals, AVG(goals) OVER(PARTITION by position) AS p_avg FROM players;

-- rank players by goal using row number()
SELECT player_name, goals, ROW_NUMBER() OVER(ORDER BY goals DESC) AS r_goals FROM players;

--Rank Players using RANK
SELECT player_name, goals RANK() OVER(ORDER BY goals DESC) AS rank_goals FROM players;

-- RANK players using DENSE RANK()
SELECT player_name, goals, DENSE_RANK() OVER (ORDER BY goals DESC) AS d_rank_goals FROM players;

-- Find the Top Three players in each position.
WITH player_ranking AS(
    select player_name, position, goals, RANK() OVER(PARTITON BY position ORDER BY goals DESC) AS goal_rank FROM players
)
SELECT * FROM player_ranking
WHERE goal_rank<=3;

--Compare each player's goals with their previous match using LAG()
SELECT player_id, match_id, goals, LAG(goals) OVER (PARTITION BY player_id ORDER BY match_id) AS prev_goals FROM players;

-- Display the next match's goal using LEAD()
SELECT player_id, match_id, goals, LEAD(goals) OVER(PARTITION BY player_id ORDER BY match_id) AS next_goals FROM players;

-- Caclculate running goals for every player.
SELECT player_id, match_id, goals, SUM(goals) OVER(PARTITION BY player_id
ORDER BY match_id
ROW BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS  running_goals
FROM players;

-- Calculate a three_match moving average
SELECT player_id, match_id, goals, AVG(goals) OVER(PARTITION BY player_id ORDER BY match_id
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_average FROM player_matches;

-- Fnd eachh position's highest and lowest goal count
SELECT position, MAX(goals) AS highest_goals, MIN(goals) AS lowest_goals
FROM players
GROUP BY position;

-- Create a player_profile table with one:one relationship
CREATE TABLE player_profile(
    profile_id INTEGER PRIMARY KEY,
    player_id INTEGER UNIQUE REFERENCES players(player_id)
);

-- Create a player_matches table with a composite primary key
CREATE TABLE player_matches(
    player_id INTEGER,
    match_id INTEGER,
    goals INTEGER DEFAULT 0,
    assists INTEGER DEFAULT 0,
    PRIMARY KEY(player_id, match_id)
);

-- ADD a check constrain to prevent negative goals
ALTER TABLE players
ADD CONSTRAINT positive_goals
CHECK (goals>=0);

--Add a NOT NULL constraint to player names.
ALTER TABLE players
ADD CONSTRAINT not_null_player_names
NOT NULL player_names;

-- Create an index on player_name
CREATE INDEX player_index ON players(player_name);

-- EXPLAIN ANALYZE RUN ON PLAYER SEARCH
EXPLAIN ANALYZE
SELECT * FROM PLAYERS
WHERE player_name="Messi";

-- Create a transaction that updates a player's statistics
BEGIN;
UPDATE players
SET goal=goal+1
WHERE player_id=101;
COMMIT;

--FIND THE TOP 10 GOAL SCORERS
SELECT player_id, SUM(goals) as total_goals
FROM players
GROUP BY player_id
ORDER BY total_goals DESC
LIMIT 10;

--Calculate avg goals per player
SELECT player_id, COUNT(*) AS matches_played, SUM(goals) AS total_goals, AVG(age) AS avg_age
FROM player_matches
GROUP BY player_id;

-- FInd the total goal scored each months
SELECT DATE_TRUNC('month', month_date) AS month, COUNT(*) AS total_matches FROM matches
GROUP BY DATE_TRUNC('month', month_date)
ORDER BY month;

-- Compare monthly goals using LAG().
SELECT DATE_TRUNC('month', month_date) AS month,
LAG(COUNT(*)) OVER(ORDER BY DATE_TRUNC('month', month_date)) AS prev_month_goals,
COUNT(*) AS current_month_goals
FROM matches
GROUP BY month
ORDER BY month;

-- Calculate each team's win percentage
SELECT t.team_name, COUNT(*) AS total_matches,
SUM(ROUND(100.0* CASE
WHEN m.home_team_id=t.team_id AND m.home_team_score>m.away_team_score THEN 1
WHEN m.away_team_id=t.team_id AND m.away_team_score>m.home_team_score THEN 1
ELSE 0
END)) AS wins
FROM teams t
JOIN matches m
ON t.team_id IN (m.home_team_id, m.away_team_id)
GROUP BY t.team_name
ORDER BY wins DESC;

-- Group players by jjoining year.
SELECT EXTRACT (YEAR FROM join_date) AS joining_year, COUNT(*) AS total_players, AVG(age) AS avg_age
FROM players
GROUP BY EXTRACT(YEAR FROM join_date)
ORDER BY joining_year;

-- Find players with missing ages
SELECT * FROM players
WHERE age IS NULL;

-- Find duplicate player names.
SELECT player_name, COUNT(*) AS name_count
FROM players
GROUP BY player_name
HAVING COUNT(*)>1;

-- Create high, medium, and low scorer categories
SELECT player_id, SUM(goals) AS total_goals,
CASE WHEN SUM(goals)>20 THEN 'HIGH SCORER'
WHEN SUM(goals) BETWEEN 10 AND 20 THEN 'MEDIUM SCORER'
ELSE 'LOW SCORER'
END AS scorer_category
FROM player_matches
GROUP BY player_id;

-- Prepare a player performance dataset for ML
SELECT p.player_id, p.player_name, p.player_position,
COUNT(pm.match_id) AS matches_played,
COALESCE(SUM(pm.goals), 0) AS total_goals,
COALESCE (SUM(pm.assists), 0) AS total_assists,
COALESCE (AVG(pm.minutes_played), 0) AS total_minutes_played,
CASE WHEN total_goals>=20 THEN 'HIGH'
WHEN total_goals BETWEEN 10 and 20 THEN 'MEDIUM'
ELSE 'LOW'
END AS performance_category
FROM players p
LEFT JOIN player_matches pm
ON p.player_id=pm.player_id
GROUP BY p.player_id, p.player_name, p.player_position
ORDER BY total_goals DESC;