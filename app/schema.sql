DROP TABLE IF EXISTS oppilas;
DROP TABLE IF EXISTS ryhma;
DROP TABLE IF EXISTS osallistuminen;
DROP TABLE IF EXISTS poissaolo;
DROP TABLE IF EXISTS verkkokurssi;
DROP TABLE IF EXISTS kouluttaja;
DROP TABLE IF EXISTS lahipaiva;
DROP TABLE IF EXISTS aihe;

CREATE TABLE oppilas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ryhma_id INTEGER NOT NULL,
    etunimi TEXT NOT NULL,
    sukunimi TEXT NOT NULL,
    FOREIGN KEY (ryhma_id) REFERENCES ryhma (id)
);

CREATE TABLE ryhma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nimi TEXT NOT NULL,
    lahipaiva DATE,
    lukujarjestys TEXT
);

CREATE TABLE osallistuminen (
    oppilas_id INTEGER NOT NULL,
    verkko_id INTEGER NOT NULL,
    vaihe TEXT,
    FOREIGN KEY (oppilas_id) REFERENCES oppilas (id)
);

CREATE TABLE poissaolo (
    pvm DATE NOT NULL,
    oppilas_id INTEGER NOT NULL,
    lisatieto TEXT,
    FOREIGN KEY (oppilas_id) REFERENCES oppilas (id)
);

CREATE TABLE verkkokurssi (
    verkko_id INTEGER PRIMARY KEY AUTOINCREMENT,
    verkkokurssinnimi TEXT NOT NULL
);

CREATE TABLE kouluttaja (
    id INTEGER NOT NULL,
    nimi TEXT NOT NULL,
    sukunimi TEXT NOT NULL,
    aihe TEXT
);

CREATE TABLE lahipaiva (
    pvm TEXT,
    aihe TEXT,
    kouluttaja TEXT,
    luokka TEXT,
    ryhma_id INTEGER,
    FOREIGN KEY (pvm) REFERENCES aihe (pvm)
);