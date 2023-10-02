/* (Beta) Export of data model Blower of the subject dataModel.WasteWater for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Blower_type AS ENUM ('Blower');
CREATE TABLE Blower (address JSON, airflow NUMERIC, airflowEstimation NUMERIC, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, endsAt TEXT, energy NUMERIC, name TEXT, owner JSON, pressure NUMERIC, source TEXT, startsAt TEXT, type Blower_type);