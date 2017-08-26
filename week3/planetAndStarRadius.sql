SELECT p.koi_name, p.radius, s.radius
FROM Star s
JOIN Planet p on s.kepler_id = p.kepler_id
WHERE s.radius > (
  SELECT radius
  FROM Star
  ORDER BY radius desc
  LIMIT 1 OFFSET 5
  );
  
