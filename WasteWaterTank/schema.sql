/* (Beta) Export of data model WasteWaterTank of the subject dataModel.WasteWater for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WasteWaterTank_type AS ENUM ('WasteWaterTank');
CREATE TABLE WasteWaterTank (address JSON, airflow JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, do NUMERIC, endsAt TEXT, name TEXT, nh4 NUMERIC, no3 NUMERIC, owner JSON, pH NUMERIC, power JSON, redox NUMERIC, sludgeLevel NUMERIC, source TEXT, startsAt TEXT, temperature NUMERIC, tn NUMERIC, tss NUMERIC, type WasteWaterTank_type);