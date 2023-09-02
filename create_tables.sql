-- Create table client, campaign, economics
DROP TABLE IF EXISTS client;
CREATE TABLE client(
    id SERIAL PRIMARY KEY,
    age INTEGER,
    job TEXT,
    marital TEXT,
    education TEXT,
    credit_default BOOLEAN,
    housing BOOLEAN,
    loan BOOLEAN
);

DROP TABLE IF EXISTS campaign;
CREATE TABLE campaign(
    campaign_id SERIAL PRIMARY KEY,
    client_id INTEGER references client (id),
    number_contacts INTEGER,
    contact_duration INTEGER,
    pdays INTEGER,
    previous_campaign_contacts INTEGER,
    previous_outcome BOOLEAN,
    campaign_outcome BOOLEAN,
    last_contact_date DATE    
);

DROP TABLE IF EXISTS economics;
CREATE TABLE economics(
    client_id INTEGER references client (id),
    emp_var_rate FLOAT,
    cons_price_idx FLOAT,
    euribor_three_months FLOAT,
    number_employed FLOAT
);