CREATE TABLE IF NOT EXISTS app_user (
    user_id SERIAL,
    username VARCHAR(255) UNIQUE NOT NULL ,
    password VARCHAR(255) NOT NULL ,
    PRIMARY KEY (user_id)
);

