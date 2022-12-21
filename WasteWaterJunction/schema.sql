/* (Beta) Export of data model WasteWaterJunction of the subject dataModel.WasteWater for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WasteWaterJunction_type AS ENUM ('WasteWaterJunction');
CREATE TABLE WasteWaterJunction (address json, alternateName text, areaServed text, bod text, cod text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, do text, emissionFlow text, endsAt text, flowrate text, id text, location json, name text, nh4 text, no3 text, owner json, pH text, po4 text, pressure text, redox text, seeAlso json, source text, startsAt text, temperature text, tic text, tn text, toc text, tss text, type WasteWaterJunction_type);