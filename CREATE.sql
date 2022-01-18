CREATE TABLE contacts (
       id INTEGER PRIMARY KEY,
       firstname VARCHAR,
       last_modified TIMESTAMP,
       created TIMESTAMP,
       lastname VARCHAR,
       middleName VARCHAR,
       suffix VARCHAR,
       nickname VARCHAR,
       birthday TIMESTAMP,
       gender VARCHAR,
       address_1 VARCHAR,
       address_2 VARCHAR,
       city VARCHAR,
       secondary INTEGER,
       zip VARCHAR,
       title VARCHAR,
       email VARCHAR,
       phone VARCHAR,
       notes VARCHAR);


CREATE TABLE relationship (
       id INTEGER PRIMARY KEY,
       first_id INTEGER,
       last_modified TIMESTAMP,
       created TIMESTAMP,       second_id INTEGER,
       first_relationship_type VARCHAR,
       second_relationship_type VARCHAR);


CREATE TABLE tags (
       id INTEGER PRIMARY KEY,
       last_modified TIMESTAMP,
       created TIMESTAMP,
       contact_id INTEGER,
       tag VARCHAR,
       notes VARCHAR);


CREATE TABLE interactions (
       id INTEGER PRIMARY KEY,
       datetime_interaction TIMESTAMP,
       occured INTEGER,
       suggested_interaction INTEGER,
       mode_interaction VARCHAR,
       link VARCHAR,
       text_interaction VARCHAR,
       notes_prior VARCHAR,
       notes VARCHAR,       
       last_modified TIMESTAMP,
       created TIMESTAMP);
