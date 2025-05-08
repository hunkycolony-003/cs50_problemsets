SELECT p.name,
       GROUP_CONCAT(m.title, char(10)) AS movie_titles,
       COUNT(p.name) AS name_count
FROM stars s
JOIN movies m ON s.movie_id = m.id
JOIN people p ON s.person_id = p.id
WHERE p.id IN
  (SELECT person_id
   FROM directors d
   WHERE d.movie_id IN
     (SELECT movie_id
      FROM ratings r
      WHERE r.rating >= 9.0))
GROUP BY p.name
ORDER BY p.name ASC;
