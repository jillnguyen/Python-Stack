
SELECT * FROM countries 
JOIN languages ON countries.id = languages.country_id WHERE languages.language = "Slovene" ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.name) FROM countries
JOIN cities ON cities.country_id = countries.id
GROUP BY countries.name ORDER BY COUNT(cities.name) DESC;

SELECT cities.name, cities.population 
FROM cities JOIN countries on countries.id = cities.country_id
WHERE countries.name ="Mexico" AND cities.population > 500000 ORDER BY cities.population DESC;
   
SELECT countries.name, languages.language, languages.percentage
FROM countries JOIN languages ON languages.country_id = countries.id WHERE languages.percentage > 89 ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area, countries.population 
FROM countries WHERE countries.surface_area < 501 AND countries.population > 100000;

SELECT * FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital >200 AND countries.life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population
FROM cities JOIN countries ON countries.id = cities.country_id 
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT countries.region, COUNT(countries.name) 
FROM countries GROUP BY countries.region ORDER BY COUNT(countries.name) DESC;

