/* (Beta) Export of data model Blower of the subject dataModel.WasteWater for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Blower_type AS ENUM ('Blower');
CREATE TABLE Blower (address json, airflow text, airflowEstimation text, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, endsAt text, energy text, id text, location json, name text, owner json, pressure text, seeAlso json, source text, startsAt text, type Blower_type);