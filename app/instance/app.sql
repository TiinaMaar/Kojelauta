--
-- Company :      Amiedu
-- Project :      DATA MODEL
-- Author :       DK
--
-- Date Created : Tuesday, September 20, 2019 14:52:48
-- Target DBMS : MariaDB
--

use tballs;

CREATE TABLE O_ryhma(
    o_ryhmaID        INT    NOT NULL,
    nimi             VARCHAR(50),
    kurssivastaava_email     VARCHAR(50),             
    lukujarjestys    VARCHAR(50),
    CONSTRAINT PK1 PRIMARY KEY (o_ryhmaID)
)
;

CREATE TABLE Oppilaat(
    oppilasID    INT    NOT NULL,
    etunimi      VARCHAR(50),
    sukunimi     VARCHAR(50),
    o_ryhmaID    INT,
    CONSTRAINT PK4 PRIMARY KEY (oppilasID)
)
;

CREATE TABLE Osallistuminen(
    oppilasID    INT NOT NULL,
    VerkkoID     INT NOT NULL,
    CONSTRAINT PK5 PRIMARY KEY (oppilasID, VerkkoID)
)
;

CREATE TABLE Poissaolo(
    pvm          DATE             NOT NULL,
    oppilasID    INT NOT NULL,
    lisatieto    VARCHAR(100),
    CONSTRAINT PK2 PRIMARY KEY (pvm, oppilasID)
)
;

CREATE TABLE Verkkokurssit(
    VerkkoID             INT NOT NULL,
    verkkokurssinnimi    VARCHAR(50),
    status               INT,
    CONSTRAINT PK3 PRIMARY KEY (VerkkoID)
)
;

ALTER TABLE Oppilaat ADD CONSTRAINT RefO_ryhma12 
    FOREIGN KEY (o_ryhmaID)
    REFERENCES O_ryhma(o_ryhmaID)
;

ALTER TABLE Osallistuminen ADD CONSTRAINT RefOppilaat4 
    FOREIGN KEY (oppilasID)
    REFERENCES Oppilaat(oppilasID)
;

ALTER TABLE Osallistuminen ADD CONSTRAINT RefVerkkokurssit5 
    FOREIGN KEY (VerkkoID)
    REFERENCES Verkkokurssit(VerkkoID)
;

ALTER TABLE Poissaolo ADD CONSTRAINT RefOppilaat10 
    FOREIGN KEY (oppilasID)
    REFERENCES Oppilaat(oppilasID)
;


insert into O_ryhma values (1, 'TVTeat Ketterä DevOps TYPO4', 'annika@amiedu.fi', '../../static/media/Lukujärjestys TvteatTYPO4.pdf');
insert into O_ryhma values (2, 'TVTeat Ketterä DevOps TYPO5', 'no@amiedu.fi', NULL);
insert into O_ryhma values (3, 'TVTeat Ketterä DevOps TYPO6', 'no1@amiedu.fi', NULL);
insert into Oppilaat values (1, 'Tiina', 'Maaranen', 1);
insert into Oppilaat values (2, 'Gleb', 'Tishchenko', 1);
insert into Verkkokurssit values ('Git');
insert into Verkkokurssit values ('Linux');
insert into Verkkokurssit values ('Python');

commit;