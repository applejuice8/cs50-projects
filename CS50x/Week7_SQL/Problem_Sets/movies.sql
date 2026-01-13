-- 1.sql
SELECT title FROM movies
    WHERE year = '2008';

-- 2.sql
SELECT birth FROM people
    WHERE name = 'Emma Stone';

-- 3.sql
SELECT title FROM movies
    WHERE year >= '2018'
    ORDER BY title ASC;

-- 4.sql
SELECT COUNT(*) FROM ratings
    WHERE rating = '10.0';

-- 5.sql
SELECT title, year FROM movies
    WHERE title LIKE 'Harry Potter%'
    ORDER BY year;

-- 6.sql
SELECT AVG(rating) FROM movies
    JOIN ratings ON movies.id = ratings.movie_id
    WHERE year = '2012';

-- 7.sql
SELECT title, rating FROM movies
    JOIN ratings ON movies.id = ratings.movie_id
    WHERE year = '2010'
    ORDER BY rating DESC, title ASC;

-- 8.sql
SELECT people.name FROM people
    JOIN stars ON stars.person_id = people.id
    JOIN movies ON stars.movie_id = movies.id
    WHERE movies.title = 'Toy Story';

-- 9.sql
SELECT DISTINCT people.name FROM people
    JOIN stars ON stars.person_id = people.id
    JOIN movies ON stars.movie_id = movies.id
    WHERE movies.year = '2004'
    ORDER BY people.birth;

-- 10.sql
SELECT DISTINCT people.name FROM people
    JOIN directors ON directors.person_id = people.id
    JOIN ratings ON directors.movie_id = ratings.movie_id
    WHERE rating >= '9.0';

-- 11.sql
SELECT DISTINCT movies.title FROM movies
    JOIN stars ON stars.movie_id = movies.id
    JOIN people ON people.id = stars.person_id
    JOIN ratings ON ratings.movie_id = stars.movie_id
    WHERE people.name = 'Chadwick Boseman'
    ORDER BY ratings.rating DESC
    LIMIT 5;

-- 12.sql
SELECT title FROM movies
    JOIN stars ON stars.movie_id = movies.id
    JOIN people ON people.id = stars.person_id
    WHERE people.name = 'Bradley Cooper'
    AND title IN (
        SELECT title FROM movies
        JOIN stars ON stars.movie_id = movies.id
        JOIN people ON people.id = stars.person_id
        WHERE people.name = 'Jennifer Lawrence'
    );

-- 13.sql
SELECT DISTINCT people.name FROM people
    JOIN stars ON stars.person_id = people.id
    WHERE stars.movie_id IN (
        SELECT movies.id FROM movies
        JOIN stars ON stars.movie_id = movies.id
        JOIN people ON stars.person_id = people.id
        WHERE people.name = 'Kevin Bacon'
    )
    AND people.name != 'Kevin Bacon';