
create_country_dim = """
CREATE TABLE IF NOT EXISTS country_dim (
    country_id              INTEGER PRIMARY KEY ,
    country_name            VARCHAR,
    country_avg_tmp         FLOAT

);
"""

insert_country_dim  = ("""
INSERT INTO country_dim (country_id, country_name, country_avg_tmp)
    VALUES (%s, %s, %s)

""")

drop_country_dim = "DROP TABLE IF EXISTS country_dim;"

create_state_dim = """
CREATE TABLE IF NOT EXISTS state_dim (
    code_state              VARCHAR PRIMARY KEY ,
    state_name              VARCHAR,
    state_avg_tmp           FLOAT,
    male_population         BIGINT,
    female_population       BIGINT,
    totalPopulatio          BIGINT

);
"""

insert_state_dim  = ("""
INSERT INTO state_dim (code_state, state_name, state_avg_tmp, male_population, female_population, totalPopulatio)
    VALUES (%s, %s, %s, %s, %s, %s)

""")

drop_state_dim = "DROP TABLE IF EXISTS state_dim;"


create_visa_dim = """
CREATE TABLE IF NOT EXISTS visa_dim (
    visa_id             INTEGER PRIMARY KEY ,
    visa_type_issued    VARCHAR,
    visa_end_date       DATE
);
"""

insert_visa_dim  = ("""
INSERT INTO visa_dim (visa_id, visa_type_issued, visa_end_date)
    VALUES (%s,%s, %s)

""")

drop_visa_dim = "DROP TABLE IF EXISTS visa_dim;"

create_imigration_fact = """
CREATE TABLE IF NOT EXISTS imigration_fact (
    cicid INTEGER PRIMARY KEY,
    gender CHAR,
    age INTEGER,
    arrival_date DATE,
    code_state  VARCHAR REFERENCES state_dim (code_state) ,
    visa_id INTEGER REFERENCES visa_dim (visa_id),
    country_citiz_id INTEGER REFERENCES country_dim (country_id),
    country_res_id INTEGER REFERENCES country_dim (country_id)
);
"""
insert_imigration_fact  = ("""
INSERT INTO imigration_fact (cicid, gender, age, arrival_date, code_state, visa_id, country_citiz_id, country_res_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

drop_imigration_fact = "DROP TABLE IF EXISTS imigration_fact;"



create_table_queries = [create_country_dim, create_state_dim, create_visa_dim, create_imigration_fact]
drop_table_queries = [drop_imigration_fact,drop_country_dim,drop_state_dim,drop_visa_dim]
