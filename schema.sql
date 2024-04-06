DROP DATABASE IF EXIST PartsComp;
CREATE DATABASE IF NOT EXIST PartsComp;

CREATE TABLE IF NOT EXIST users(
    user_id         SERIAL,
    user_name       VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_admin        BOOLEAN,
    PRIMARY KEY (user_id)
)

CREATE TABLE IF NOT EXIST cpu(
    cpu_id          SERIAL,
    cpu_name        VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    cpu_url         VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (part_id)
)

CREATE TABLE IF NOT EXIST graphics_card(
    graphics_id     SERIAL,
    graphics_name   VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    graphics_url    VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (part_id)
)

CREATE TABLE IF NOT EXIST storage(
    storage_id      SERIAL,
    storage_name    VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    storage_url     VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (part_id)
)

CREATE TABLE IF NOT EXIST power_supply(
    power_id        SERIAL,
    power_name      VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    power_url       VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (power_id)
)

CREATE TABLE IF NOT EXIST motherboard(
    board_id        SERIAL,
    board_name      VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    board_url       VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (board_id)
)

CREATE TABLE IF NOT EXIST cooling(
    board_id        SERIAL,
    board_name      VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    board_url       VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (board_id)
)

CREATE TABLE IF NOT EXIST memory(
    board_id        SERIAL,
    board_name      VARCHAR(255) NOT NULL,
    brand           VARCHAR(255) NOT NULL,
    price           DECIMAL(10,2),
    board_url       VARCHAR(255),
    has_conflict    BOOLEAN,
    PRIMARY KEY (board_id)
)

CREATE TABLE IF NOT EXIST build(
    build_id        SERIAL,
    cpu_id          ,
    power_id        ,
    graphics_id     ,
    cooling_id      ,
    memory_id       ,
    casing_id       ,
    storage         ,
    memory          ,
    user_id         ,
    referal_url     VARCHAR(255),
    total_price     INT,
    FOREIGN KEY (cpu_id)        REFERENCES cpu(cpu_id)
    FOREIGN KEY (power_id)      REFERENCES power_supply(power_id)
    FOREIGN KEY (graphics_id)   REFERENCES graphics_card(graphics_id)
    FOREIGN KEY (cooling_id)    REFERENCES cooling(cooling_id)
    FOREIGN KEY (memory_id)     REFERENCES memory(memory_id)
    FOREIGN KEY (casing_id)     REFERENCES casing(casing_id)
    FOREIGN KEY (storage)       REFERENCES storage(storage_id)
    FOREIGN KEY (memory)        REFERENCES memory(memory_id)
    FOREIGN KEY (user_id)       REFERENCES user(user_id)
    PRIMARY KEY (build_id)
)
