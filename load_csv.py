from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Decimal, Text, Boolean


# db_url = 'postgresql://username:password@localhost:5432/your_database_name'
db_url = 'postgresql://postgres:3901@localhost:5432/bank_marketing'
csv_file_path = 'C:/Users/Ticy/Documents/GitHub Project/Designing_Bank_Marketing_Database/client.csv'
# metadata = MetaData()

with open(csv_file_path, 'r') as f:    
    conn = create_engine(db_url).raw_connection()
    cursor = conn.cursor()
    cmd = 'COPY client(id, age, job, marital, education, credit_default, housing, loan) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
    cursor.copy_expert(cmd, f)
    conn.commit()

client = Table('client', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('age', Integer()),
                  Column('job', Text()),
                  Column('marital', Text()), 
                  Column('education', Text()), 
                  Column('credit_default', Boolean()), 
                  Column('housing', Boolean()), 
                  Column('loan', Boolean()))

client = Table('campaign', metadata,
                  Column('campaign_id', Integer(), primary_key=True),
                  Column('age', Integer()),
                  Column('job', Text()),
                  Column('marital', Text()), 
                  Column('education', Text()), 
                  Column('credit_default', Boolean()), 
                  Column('housing', Boolean()), 
                  Column('loan', Boolean()))
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


client = Table('client', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('age', Integer()),
                  Column('job', Text()),
                  Column('marital', Text()), 
                  Column('education', Text()), 
                  Column('credit_default', Boolean()), 
                  Column('housing', Boolean()), 
                  Column('loan', Boolean()))

metadata.create_all(engine)

