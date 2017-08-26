SELECT ROUND(AVG(p.t_eq), 1), MIN(s.t_eff), MAX(s.t_eff)
FROM Star s
JOIN Planet p on p.kepler_id = s.kepler_id
WHERE s.t_eff > (
  SELECT AVG(t_eff) FROM Star  
);

