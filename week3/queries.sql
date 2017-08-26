SELECT radius, t_eff FROM star where radius > 1;
select kepler_id, t_eff from Star WHERE t_eff >= 5000 and t_eff <= 6000 ;
select kepler_name, radius from Planet where kepler_name is not NULL and radius >= 1 and radius <= 3;
select MIN(radius) , MAX(radius), AVG(radius), STDDEV(radius) from Planet WHERE kepler_name IS  NULL;
select kepler_id, COUNT(koi_name) FROM Planet GROUP BY kepler_id HAVING COUNT(koi_name) > 1 ORDER BY COUNT(koi_name) desc;
