-- upgrade --
CREATE TABLE IF NOT EXISTS "movie" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "adult" BOOL NOT NULL,
    "movie_id" INT NOT NULL,
    "original_title" TEXT NOT NULL,
    "popularity" DOUBLE PRECISION NOT NULL,
    "video" BOOL NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
