CREATE DATABASE lbs_data WITH OWNER = {db_owner};

-- CREATE ADMIN
CREATE TABLE IF NOT EXISTS admin (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    password VARCHAR(128) NOT NULL
);

-- CREATE dEVICE
CREATE TABLE IF NOT EXISTS device (
    serial_number VARCHAR(50) PRIMARY KEY,
    device_model VARCHAR(128)
);

-- CREATE LOCATION
CREATE TABLE IF NOT EXISTS location (
    id SERIAL PRIMARY KEY,
    latitude NUMERIC(10,7),
    longitude NUMERIC(10,7),
    location_precision INT,
    location_type VARCHAR(10),
    created_on TIMESTAMP,
    updated_on TIMESTAMP
);
-- CREATE GSM_CELLS
CREATE TABLE IF NOT EXISTS gsm_cell (
    id SERIAL PRIMARY KEY,
    country_code INT,
    operator_id INT,
    cell_id INT,
    lac INT,
    signal_strength INT,
    age INT,
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES location (id) ON DELETE CASCADE
);
-- CREATE WIFI_NETWORKS
CREATE TABLE IF NOT EXISTS wifi_network (
    id SERIAL PRIMARY KEY,
    mac VARCHAR(128),
    signal_strength INT,
    age INT,
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES location (id) ON DELETE CASCADE
);
-- CREATE IP
CREATE TABLE IF NOT EXISTS ip (
    id SERIAL PRIMARY KEY,
    ip_address VARCHAR(50),
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES location (id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS gsm_cell_location
ON gsm_cell(location_id);

CREATE INDEX IF NOT EXISTS wifi_network_location
ON wifi_network(location_id);


CREATE INDEX IF NOT EXISTS ip_location
ON ip(location_id);

-------- LOGGING DB --------
CREATE DATABASE lbs_logs WITH OWNER = {db_owner};

CREATE TABLE IF NOT EXISTS log
(id SERIAL PRIMARY KEY,
module VARCHAR(128),
log_type VARCHAR (10),
endpoint VARCHAR (128),
methods VARCHAR (128),
message VARCHAR,
device_id VARCHAR,
time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS position
(
    id SERIAL PRIMARY KEY,
    latitude NUMERIC(10,7),
    longitude NUMERIC(10,7),
    location_precision INT,
    position_time TIMESTAMP,
    log_id INT,
    FOREIGN KEY (log_id) REFERENCES log(id) ON DELETE CASCADE
);
