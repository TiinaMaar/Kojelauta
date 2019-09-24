--
-- Company :      Amiedu
-- Project :      DATA MODEL
-- Author :       DK
--
-- Date Created : Tuesday, September 20, 2019 14:52:48
-- Target DBMS : MariaDB
--

-- 
-- TABLE: O_ryhma 
--
use tballs;

CREATE TABLE O_ryhma(
    o_ryhmaID        INT    NOT NULL,
    nimi             VARCHAR(50),
    vetaja_email     VARCHAR(50),             
    lukujarjestys    VARCHAR(50),
    CONSTRAINT PK1 PRIMARY KEY (o_ryhmaID)
)
;



-- 
-- TABLE: Oppilaat 
--

CREATE TABLE Oppilaat(
    oppilasID    INT    NOT NULL,
    etunimi      VARCHAR(50),
    sukunimi     VARCHAR(50),
    o_ryhmaID    INT,
    CONSTRAINT PK4 PRIMARY KEY (oppilasID)
)
;



-- 
-- TABLE: Osallistuminen 
--

CREATE TABLE Osallistuminen(
    oppilasID    INT NOT NULL,
    VerkkoID     INT NOT NULL,
    CONSTRAINT PK5 PRIMARY KEY (oppilasID, VerkkoID)
)
;



-- 
-- TABLE: Poissaolo 
--

CREATE TABLE Poissaolo(
    pvm          DATE             NOT NULL,
    oppilasID    INT NOT NULL,
    lisatieto    VARCHAR(100),
    CONSTRAINT PK2 PRIMARY KEY (pvm, oppilasID)
)
;



-- 
-- TABLE: Verkkokurssit 
--

CREATE TABLE Verkkokurssit(
    VerkkoID             INT NOT NULL,
    verkkokurssinnimi    VARCHAR(50),
    status               INT,
    CONSTRAINT PK3 PRIMARY KEY (VerkkoID)
)
;



-- 
-- TABLE: Oppilaat 
--

ALTER TABLE Oppilaat ADD CONSTRAINT RefO_ryhma12 
    FOREIGN KEY (o_ryhmaID)
    REFERENCES O_ryhma(o_ryhmaID)
;


-- 
-- TABLE: Osallistuminen 
--

ALTER TABLE Osallistuminen ADD CONSTRAINT RefOppilaat4 
    FOREIGN KEY (oppilasID)
    REFERENCES Oppilaat(oppilasID)
;

ALTER TABLE Osallistuminen ADD CONSTRAINT RefVerkkokurssit5 
    FOREIGN KEY (VerkkoID)
    REFERENCES Verkkokurssit(VerkkoID)
;


-- 
-- TABLE: Poissaolo 
--

ALTER TABLE Poissaolo ADD CONSTRAINT RefOppilaat10 
    FOREIGN KEY (oppilasID)
    REFERENCES Oppilaat(oppilasID)
;


insert into O_ryhma values (1, 'eliitti', 'no@example.com', NULL);
insert into O_ryhma values (2, 'pohjasakka', no@example.com', NULL);
insert into O_ryhma values (3, 'te-keskuksen ryhma', no@example.com', NULL);
insert into Oppilaat values (1, 'Tiina', 'M', 1);
insert into Oppilaat values (2, 'Gleb', 'T', 1);
insert into Oppilaat values (3, 'Ville', 'A', 2);
insert into Oppilaat values (4, 'Vilja', 'Hanninen', 2);
commit;

