sqlite3 favourites.db            -- Create db file
.mode csv
.import favourites.csv favorites -- Import favourites.csv data into favourites table
.quit                            -- Exit sqlite3 CLI program

-- Show code ran to create table
.schema

-- Prints in table format
SELECT * FROM favourites;
SELECT language FROM favourites;
SELECT COUNT(DISTINCT language) FROM favourites;

-- 2 conditions
SELECT COUNT(*) FROM favourites WHERE language = 'C' AND problem = 'Hello, World';

-- If got quote in str, use 2 single quote
SELECT COUNT(*) FROM favourites WHERE problem = 'Hello, It''s Me';

-- Starts with 'Hello, '
SELECT COUNT(*) FROM favourites WHERE problem LIKE 'Hello, %';

-- Shows summary of each language with its count
SELECT language, COUNT(*) FROM favourites
    GROUP BY language
    ORDER BY COUNT(*) DESC;

-- Shows THE least popular language and its count
SELECT language, COUNT (*) AS n FROM favourites
    GROUP BY language
    ORDER BY n DESC
    LIMIT 1;

-- Insert, Delete, Update
INSERT INTO favourites (language, problem) VALUES ('SQL', 'Fiftyville');
DELETE FROM favourites WHERE Timestamp IS NULL;
UPDATE favourites SET language = 'SQL', problem = 'Fiftyville';

-- PK, FK
SELECT title FROM shows
    WHERE id IN (
        SELECT show_id FROM ratings
            WHERE rating >= 6.0
    )
    LIMIT 10;

-- Join 2 tables
SELECT * FROM shows
    JOIN ratings ON shows.id = ratings.show_id
    WHERE rating >= 6.0 LIMIT 10;

-- Method 1 (Select all shows title that Steve is in)
SELECT title FROM shows
    JOIN stars ON shows.id = stars.show_id
    JOIN people ON people.id = stars.person_id
    WHERE name = 'Steve';

-- Method 2 (Select all shows title that Steve is in)
SELECT title FROM shows, stars, people
    WHERE shows_id = stars.show_id
    AND people.id = stars.person_id
    AND name = 'Steve';

-- Print time taken for each command
.timer ON
SELECT * FROM shows;

-- Creates a B-tree. Makes searching faster
CREATE INDEX title_index ON shows (title);

-- Improve long queries with index
SELECT title FROM shows
    WHERE id IN (
        SELECT show_id FROM stars
        WHERE person_id = (
            SELECT id FROM people
            WHERE name = 'Steve'
        )
    );

CREATE INDEX name_index ON people (name);
CREATE INDEX person_index ON stars (person_id);