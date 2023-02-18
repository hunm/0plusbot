CREATE TABLE IF NOT EXISTS Users(
    user_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(32),
    is_wanna_porn BOOLEAN DEFAULT FALSE,
    is_wanna_categoried_porn BOOLEAN DEFAULT FALSE
);