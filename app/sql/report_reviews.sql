SELECT avaliation_type, COUNT(*) AS total
FROM reviews
WHERE avaliation_date BETWEEN :start_date AND :end_date
GROUP BY avaliation_type;