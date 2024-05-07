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
    location_precision NUMERIC,
    location_type VARCHAR(10),
    created_on TIMESTAMP,
    updated_on TIMESTAMP
);
-- CREATE GSM_CELLS
CREATE TABLE IF NOT EXISTS gsm_cell (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(50),
    operator_id VARCHAR(50),
    cell_id VARCHAR(50),
    lac VARCHAR(50),
    signal_strength VARCHAR(50),
    age VARCHAR(50),
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES location (id) ON DELETE CASCADE
);
-- CREATE WIFI_NETWORKS
CREATE TABLE IF NOT EXISTS wifi_network (
    id SERIAL PRIMARY KEY,
    mac VARCHAR(128),
    signal_strength VARCHAR(50),
    age VARCHAR(50),
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
