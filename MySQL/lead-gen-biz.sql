-- 1. What query would you run to get the total revenue for March of 2012?

SELECT SUM(amount) FROM billing WHERE charged_datetime LIKE '2012-03-%';


-- 2. What query would you run to get total revenue collected from the client with an id of 2?

SELECT client_id, SUM(amount) FROM billing  WHERE client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?

SELECT * FROM sites WHERE client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?

SELECT client_id, COUNT(domain_name) as number_of_websites, month(sites.created_datetime), year(sites.created_datetime)
FROM sites 
WHERE client_id = 1
GROUP BY domain_name, month(sites.created_datetime), year(sites.created_datetime);

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?

SELECT COUNT(leads.registered_datetime) as number_of_leads, leads.site_id, sites.domain_name, date_format(leads.registered_datetime, '%M') as the_month FROM leads
JOIN sites ON sites.site_id = leads.site_id 
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:00' AND '2011-02-15 23:59:00' 
GROUP BY leads.site_id, the_month; 


-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?

SELECT CONCAT(clients.first_name,' ',clients.last_name) AS full_name, COUNT(leads.site_id) FROM leads
JOIN sites ON leads.site_id= sites.site_id
JOIN clients ON sites.client_id = clients.client_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id;


-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?

SELECT Concat(clients.first_name,' ', clients.last_name) as full_name, COUNT(leads.leads_id) as number_of_leads, date_format(leads.registered_datetime, '%M') as the_month FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE month(leads.registered_datetime) < 7 AND year(leads.registered_datetime) = 2011
GROUP BY sites.site_id, the_month;



-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

SELECT CONCAT(clients.first_name,' ',clients.last_name) as full_name, sites.domain_name as websites, COUNT(leads.registered_datetime), sites.created_datetime
FROM clients JOIN sites ON sites.client_id = clients.client_id 
JOIN leads ON leads.site_id = sites.site_id
WHERE year(leads.registered_datetime) = 2011
GROUP BY leads.site_id;

SELECT clients.client_id, CONCAT(clients.first_name,' ',clients.last_name) as full_name, sites.domain_name, COUNT(leads.leads_id), sites.created_datetime
FROM clients JOIN sites ON sites.client_id = clients.client_id 
JOIN leads ON leads.site_id = sites.site_id
GROUP BY leads.site_id
ORDER BY clients.client_id ASC;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client client id

SELECT CONCAT(clients.first_name,' ',clients.last_name) as full_name, SUM(billing.amount) as total_revenue, date_format(charged_datetime, '%M') as the_month, date_format(charged_datetime, '%Y') as the_year
FROM billing JOIN clients ON clients.client_id = billing.client_id
GROUP BY clients.client_id, the_year , the_month;
-- 

10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)billing

SELECT CONCAT(clients.first_name,' ', clients.last_name) as full_name, GROUP_CONCAT(sites.domain_name, ' ')
FROM clients
JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id; 



