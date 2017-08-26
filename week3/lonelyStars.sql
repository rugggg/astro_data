SELECT s.kepler_id, s.t_eff, s.radius
FROM Star AS s
LEFT OUTER JOIN Planet AS p ON s.kepler_id = p.kepler_id
WHERE p.koi_name IS NULL
ORDER BY t_eff desc;
