SELECT s.radius, COUNT(p.koi_name)  
FROM Star as s 
JOIN Planet as p ON s.radius > 1 AND s.kepler_id = p.kepler_id 
GROUP BY s.kepler_id
HAVING COUNT(p.koi_name) > 1
ORDER  BY s.radius desc;
