DROP DATABASE IF EXIST PartsComp;
CREATE DATABASE IF NOT EXIST PartsComp;

CREATE TABLE IF NOT EXIST users(
    user_id         SERIAL NOT NULL,
    user_name       VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_admin        BOOLEAN,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXIST part(
    part_id         SERIAL NOT NULL,
    brand           VARCHAR(255),
    price           DECIMAL(10,2),
    rating          INT,
    wat_req         INT NULL,
    amount          INT NULL,
    PRIMARY KEY (part_id)
);

CREATE TABLE IF NOT EXIST build(
    build_id        SERIAL NOT NULL,
    referal_url     VARCHAR(255),
    time_created    TIMESTAMP,
    is_private      BOOLEAN,
    total_price     INT,
    user_id         INT,
    PRIMARY KEY (build_id)
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE IF NOT EXIST components(
    part_id         INT,
    build_id        INT,
    FOREIGN KEY (build_id) REFERENCES build(build_id)
    FOREIGN KEY (part_id) REFERENCES part(part_id)
);


-- If we want to do comments/forums
CREATE TABLE IF NOT EXIST post(
    post_id         SERIAL,
    user_id         INT,
    build_id        INT NULL,
    body_text       TEXT,

    PRIMARY KEY (post_id)
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    FOREIGN KEY (build_id) REFERENCES build(user_id)
);

CREATE TABLE IF NOT EXIST comment(
    user_id         INT,
    post_id         INT, 

    FOREIGN KEY (user_id) REFERENCES users(user_id)
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);