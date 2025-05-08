-- Keep a log of any SQL queries you execute as you solve the mystery.

-- To get the report of the investigation and crime moment
SELECT id, description FROM crime_scene_reports WHERE
year = '2023' AND
month = '07' AND
day = '28' AND
street = 'Humphrey Street';
-- Takeaways : Venue - Humphrey Street bakery, Time: 10:15am, Interview of three people

-- To get the report from of the interview mentioned in the crime report
SELECT id, name, transcript
FROM interviews
WHERE year = '2023'
AND month = '07'
AND day = '28'
-- To get only the relevant data:
AND id BETWEEN 161 AND 163;
-- Takeaways: Thief drove away from the parking lot withing 10 minutes, parking logs might help
--          : Earlier in the morning, thief seen withdrawing money from atm at Leggett Street
--            beside Emma's Bakery
--          : After the theft, thief called someone for less than a minute to purchase the ticket of
--            the earliest flight out of Fiftyville, the next day


-- To check the bakery security camera mentioned by the first interviewee
SELECT license_plate
FROM bakery_security_logs
WHERE year = '2023'
AND month = '07'
AND day = '28'
AND hour = '10'
AND minute BETWEEN 15 AND 25;
-- Get a list of license plates, one of which is the thief's

-- Get the atm transactions at the time mentioned by second interviewee
SELECT account_number
FROM atm_transactions
WHERE year = 2023
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
-- Takeaway: List the account number of the people who withdrew money from the atm at that time

-- Get the person ids of the people associated with those account numbers
SELECT person_id
FROM bank_accounts
WHERE account_number IN
(SELECT account_number
FROM atm_transactions
WHERE year = 2023
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw');

-- Get details about people who used that atm to withdraw money that day and exited from the
-- bakery parking at almost same time as the thief
SELECT *
FROM people
WHERE id IN
    (SELECT person_id
    FROM bank_accounts
    WHERE account_number IN
        (SELECT account_number
        FROM atm_transactions
        WHERE year = 2023
            AND month = 7
            AND day = 28
            AND atm_location = 'Leggett Street'
            AND transaction_type = 'withdraw'))
AND license_plate IN
    (SELECT license_plate
      FROM bakery_security_logs
     WHERE year = '2023'
       AND month = '07'
       AND day = '28'
       AND hour = '10'
       AND minute BETWEEN 15 AND 25);
-- Takeaways: There are four people validating this condition. So Four suspects as of now
--          : We have their name, id, phone no, passport number

-- Accoording o the third interviewee, checking the phone calls made by the
-- four suspects in the mentioned time
SELECT *
  FROM phone_calls
 WHERE caller IN
    (SELECT phone_number
       FROM people
      WHERE id IN
        (SELECT person_id
           FROM bank_accounts
          WHERE account_number IN
            (SELECT account_number
               FROM atm_transactions
              WHERE year = 2023
                AND month = 7
                AND day = 28
                AND atm_location = 'Leggett Street'
                AND transaction_type = 'withdraw'))
      AND license_plate IN
          (SELECT license_plate
             FROM bakery_security_logs
            WHERE year = '2023'
              AND month = '07'
              AND day = '28'
              AND hour = '10'
              AND minute BETWEEN 15 AND 25))
AND year = 2023
AND month = 7
AND day = 28
AND duration < 60;
-- Takeaways: Phone number of 2 people suspected as the accomplice and theif suspect down to 2

-- Get the details of the 2 suspects
SELECT *
  FROM people
 WHERE phone_number IN
    (SELECT caller
       FROM phone_calls
      WHERE caller IN
        (SELECT phone_number
           FROM people
          WHERE id IN
            (SELECT person_id
               FROM bank_accounts
              WHERE account_number IN
                (SELECT account_number
                   FROM atm_transactions
                  WHERE year = 2023
                    AND month = 7
                    AND day = 28
                    AND atm_location = 'Leggett Street'
                    AND transaction_type = 'withdraw'))
                AND license_plate IN
            (SELECT license_plate
               FROM bakery_security_logs
              WHERE year = '2023'
                AND month = '07'
                AND day = '28'
                AND hour = '10'
                AND minute BETWEEN 15 AND 25))
         AND year = 2023
         AND month = 7
         AND day = 28
         AND duration < 60);
-- Takeaways : Details of the two suspetcs of the thieves

-- Identify the earliest flight from fiftyille the next day
SELECT *
  FROM flights
 WHERE origin_airport_id IN
    (SELECT id
       FROM airports
      WHERE city = 'Fiftyville')
   AND year = 2023
   AND month = 7
   AND day = 29
 ORDER BY hour, minute
 LIMIT 1;
-- TAkeaways: The flight which the thief escaped from

-- Passenger details of the person the two suspects were present in the flight
SELECT *
  FROM passengers
 WHERE flight_id IN
    (SELECT id
       FROM flights
      WHERE origin_airport_id IN
        (SELECT id
         FROM airports
        WHERE city = 'Fiftyville')
       AND year = 2023
       AND month = 7
       AND day = 29
     ORDER BY hour, minute
     LIMIT 1)
   AND passport_number IN
    (SELECT passport_number
       FROM people
      WHERE id IN
        (SELECT person_id
           FROM bank_accounts
          WHERE account_number IN
            (SELECT account_number
               FROM atm_transactions
              WHERE year = 2023
                AND month = 7
                AND day = 28
                AND atm_location = 'Leggett Street'
                AND transaction_type = 'withdraw'))
           AND license_plate IN
            (SELECT license_plate
             FROM bakery_security_logs
            WHERE year = '2023'
              AND month = '07'
              AND day = '28'
              AND hour = '10'
              AND minute BETWEEN 15 AND 25));

-- Which of the two suspects were present in the flight. i.e. the thief
SELECT *
  FROM people
 WHERE passport_number IN
    (SELECT passport_number
       FROM passengers
      WHERE flight_id IN
        (SELECT id
           FROM flights
          WHERE origin_airport_id IN
            (SELECT id
               FROM airports
              WHERE city = 'Fiftyville')
                AND year = 2023
                AND month = 7
                AND day = 29
          ORDER BY hour, minute
          LIMIT 1)
     AND passport_number IN
        (SELECT passport_number
           FROM people
          WHERE id IN
            (SELECT person_id
               FROM bank_accounts
              WHERE account_number IN
                (SELECT account_number
                   FROM atm_transactions
                  WHERE year = 2023
                    AND month = 7
                    AND day = 28
                    AND atm_location = 'Leggett Street'
                    AND transaction_type = 'withdraw'))
                    AND license_plate IN
                    (SELECT license_plate
                       FROM bakery_security_logs
                      WHERE year = '2023'
                        AND month = '07'
                        AND day = '28'
                        AND hour = '10'
                        AND minute BETWEEN 15 AND 25)))
 AND passport_number IN
 (SELECT passport_number
  FROM people
 WHERE phone_number IN
    (SELECT caller
       FROM phone_calls
      WHERE caller IN
        (SELECT phone_number
           FROM people
          WHERE id IN
            (SELECT person_id
               FROM bank_accounts
              WHERE account_number IN
                (SELECT account_number
                   FROM atm_transactions
                  WHERE year = 2023
                    AND month = 7
                    AND day = 28
                    AND atm_location = 'Leggett Street'
                    AND transaction_type = 'withdraw'))
                AND license_plate IN
            (SELECT license_plate
               FROM bakery_security_logs
              WHERE year = '2023'
                AND month = '07'
                AND day = '28'
                AND hour = '10'
                AND minute BETWEEN 15 AND 25))
         AND year = 2023
         AND month = 7
         AND day = 28
         AND duration < 60));

-- The person that the thief called at after the theft
SELECT *
  FROM people
 WHERE phone_number IN
 (SELECT receiver
    FROM phone_calls
    WHERE caller IN
 (SELECT phone_number
    FROM people
    WHERE passport_number IN
        (SELECT passport_number
        FROM passengers
        WHERE flight_id IN
            (SELECT id
            FROM flights
            WHERE origin_airport_id IN
                (SELECT id
                FROM airports
                WHERE city = 'Fiftyville')
                    AND year = 2023
                    AND month = 7
                    AND day = 29
            ORDER BY hour, minute
            LIMIT 1)
        AND passport_number IN
            (SELECT passport_number
            FROM people
            WHERE id IN
                (SELECT person_id
                FROM bank_accounts
                WHERE account_number IN
                    (SELECT account_number
                    FROM atm_transactions
                    WHERE year = 2023
                        AND month = 7
                        AND day = 28
                        AND atm_location = 'Leggett Street'
                        AND transaction_type = 'withdraw'))
                        AND license_plate IN
                        (SELECT license_plate
                        FROM bakery_security_logs
                        WHERE year = '2023'
                            AND month = '07'
                            AND day = '28'
                            AND hour = '10'
                            AND minute BETWEEN 15 AND 25)))
    AND passport_number IN
    (SELECT passport_number
    FROM people
    WHERE phone_number IN
        (SELECT caller
        FROM phone_calls
        WHERE caller IN
            (SELECT phone_number
            FROM people
            WHERE id IN
                (SELECT person_id
                FROM bank_accounts
                WHERE account_number IN
                    (SELECT account_number
                    FROM atm_transactions
                    WHERE year = 2023
                        AND month = 7
                        AND day = 28
                        AND atm_location = 'Leggett Street'
                        AND transaction_type = 'withdraw'))
                    AND license_plate IN
                (SELECT license_plate
                FROM bakery_security_logs
                WHERE year = '2023'
                    AND month = '07'
                    AND day = '28'
                    AND hour = '10'
                    AND minute BETWEEN 15 AND 25))
            AND year = 2023
            AND month = 7
            AND day = 28
            AND duration < 60)))
    AND year = 2023
    AND month = 7
    AND day = 28
    AND duration < 60);

-- The city that the thief escaped to:
SELECT *
FROM airports
WHERE id IN
(SELECT destination_airport_id
  FROM flights
 WHERE origin_airport_id IN
    (SELECT id
       FROM airports
      WHERE city = 'Fiftyville')
   AND year = 2023
   AND month = 7
   AND day = 29
 ORDER BY hour, minute
 LIMIT 1);
