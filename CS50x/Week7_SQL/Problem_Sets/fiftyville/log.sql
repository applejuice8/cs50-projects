-- Keep a log of any SQL queries you execute as you solve the mystery.
-- July 28, 2024 on Humphrey Street

-- Read crime scene report on the crime
SELECT * FROM crime_scene_reports
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND street = 'Humphrey Street';

-- Information learned
-- Theft took place at 10:15am at the Humphrey Street bakery
-- 3 witnesses present at the time, all mentioned the bakery

-- Check interviews regarding the crime
SELECT * FROM interviews
    WHERE day = '28' AND month = '7' AND year = '2024';

-- Information learned from the 3 interviews
-- Sometime within ten minutes of the theft, thief get into a car in the bakery parking lot and drive away
-- Earlier this morning, the thief withdrawing some money on Leggett Street
-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute
-- thief plans to take the earliest flight out of Fiftyville tomorrow
-- The thief asked the accompolice to purchase the flight ticket

-- Car Suspects
SELECT people.name AS car_suspects FROM people
    JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND hour = '10' AND minute <= '25'
    AND activity = 'exit';

-- Withdrawal Suspects
SELECT people.name AS withdrawal_suspects FROM people
    JOIN bank_accounts ON bank_accounts.person_id = people.id
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- Call Suspects
SELECT people.name AS call_suspects FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND duration < '60';

-- The escape flight ID
SELECT flights.id FROM flights
    JOIN airports ON airports.id = flights.origin_airport_id
    WHERE day = '29' AND month = '7' AND year = '2024'
    AND airports.city = 'Fiftyville'
    ORDER BY hour ASC, minute ASC
    LIMIT 1;

-- Find escape destination (New York City)
SELECT airports.city FROM airports
    JOIN flights ON flights.destination_airport_id = airports.id
    WHERE flights.id = (
        SELECT flights.id FROM flights
            JOIN airports ON airports.id = flights.origin_airport_id
            WHERE day = '29' AND month = '7' AND year = '2024'
            AND airports.city = 'Fiftyville'
            ORDER BY hour ASC, minute ASC
            LIMIT 1
    );

-- All passengers on the escape flight
SELECT people.name AS flight_suspects FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    WHERE passengers.flight_id = (
        SELECT flights.id FROM flights
            JOIN airports ON airports.id = flights.origin_airport_id
            WHERE day = '29' AND month = '7' AND year = '2024'
            AND airports.city = 'Fiftyville'
            ORDER BY day ASC, hour ASC, minute ASC
            LIMIT 1
    );

-- Common suspects (Found out it's Bruce)
SELECT people.name AS car_suspects FROM people
    JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND hour = '10' AND minute <= '25'
    AND activity = 'exit'
INTERSECT
SELECT people.name AS withdrawal_suspects FROM people
    JOIN bank_accounts ON bank_accounts.person_id = people.id
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
INTERSECT
SELECT people.name AS call_suspects FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND duration < '60'
INTERSECT
SELECT people.name AS flight_suspects FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    WHERE passengers.flight_id = (
        SELECT flights.id FROM flights
            JOIN airports ON airports.id = flights.origin_airport_id
            WHERE day = '29' AND month = '7' AND year = '2024'
            AND airports.city = 'Fiftyville'
            ORDER BY day ASC, hour ASC, minute ASC
            LIMIT 1
    );

-- Find out who Bruce called (Found out it's Robin)
SELECT people.name AS accompolice_suspect FROM people
    JOIN phone_calls ON phone_calls.receiver = people.phone_number
    WHERE day = '28' AND month = '7' AND year = '2024'
    AND phone_calls.caller = (
        SELECT phone_number FROM people
            WHERE name = 'Bruce'
    )
    AND duration < '60';
