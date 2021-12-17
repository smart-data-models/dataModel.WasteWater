Entität: WasteWaterPlant  
========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterPlant/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Datenmodell für Kläranlage.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `bod`: Die in der Kläranlage gemessene Konzentration des biologischen Sauerstoffbedarfs entspricht dieser Beobachtung.  - `cod`: Die in der Kläranlage gemessene Konzentration des chemischen Sauerstoffbedarfs entspricht dieser Beobachtung.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `do`: Der in der Kläranlage gemessene gelöste Sauerstoff entspricht dieser Beobachtung.  - `id`: Eindeutiger Bezeichner der Entität  - `inFlow`: Zuflussmenge in die Kläranlage/das Reservoir entsprechend dieser Beobachtung.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `municipalityInfo`: Informationen der Gemeinde zu dieser Beobachtung.  - `name`: Der Name dieses Artikels.  - `nh4`: Die in der Kläranlage gemessene Ammoniumkonzentration entspricht dieser Beobachtung.  - `no3`: Die in der Kläranlage gemessene Nitratkonzentration entspricht dieser Beobachtung.  - `observationDateTime`: Letzter gemeldeter Zeitpunkt der Beobachtung.  - `outFlow`: Abflussmenge in die Kläranlage/das Reservoir entsprechend dieser Beobachtung.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pHTSA`: Im Wasser beobachteter Säuregrad oder Basizität. Objekt, das die zeitliche Verarbeitung der Größeneigenschaft während einer Periode definiert. Es liefert Maximum, Minimum, Momentanwert und Durchschnitt  - `po4`: Die in der Kläranlage gemessene Ortho-Phosphat-Konzentration entspricht dieser Beobachtung.  - `redox`: Das in der Kläranlage gemessene Reduktions- oder Oxidationspotenzial entspricht dieser Beobachtung.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `tic`: Die in der Kläranlage gemessene Gesamtkonzentration an anorganischem Kohlenstoff entspricht dieser Beobachtung.  - `tn`: Die in der Kläranlage gemessene Gesamtstickstoffkonzentration entspricht dieser Beobachtung.  - `toc`: Die in der Kläranlage gemessene Gesamtkonzentration an organischem Kohlenstoff entspricht dieser Beobachtung.  - `treatmentPlantCapacity`: Die Umschlagskapazität der Kläranlage entspricht dieser Beobachtung.  - `treatmentPlantCode`: Eindeutiger Code für die Kläranlage, die dieser Beobachtung entspricht.  - `treatmentPlantId`: Eindeutige Identifikationsnummer für die Kläranlage, die dieser Beobachtung entspricht.  - `treatmentPlantName`: Name der Kläranlage, die dieser Beobachtung entspricht.  - `tss`: Die in einer Kläranlage gemessene Gesamtkonzentration an suspendierten Feststoffen entspricht dieser Beobachtung.  - `type`: NGSI-Entitätstyp. Es muss WasteWaterPlant sein    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteWaterPlant:    
  description: 'Data model for waste water treatment plant.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bod:    
      description: 'Biological Oxygen Demand concentration measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cod:    
      description: 'Chemical Oxygen Demand concentration measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    do:    
      description: 'Dissolved oxygen measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &wastewaterplant_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    inFlow:    
      description: 'In-flow amount into the treatment plant/reservoir corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City Id corresponding to this observation.'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardId:    
          description: 'Property. Model:''https://schema.org/Text''. Ward Id corresponding to this observation.'    
          type: string    
        wardName:    
          description: 'Property. Model:''https://schema.org/Text''. Ward name corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone Id corresponding to this observation.'    
          type: string    
        zoneName:    
          description: 'Property. Model:''https://schema.org/Text''. Zone name corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nh4:    
      description: 'Ammonium concentration measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    no3:    
      description: 'Nitrate concentration measured in waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    outFlow:    
      description: 'Out-flow amount into the treatment plant/reservoir corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastewaterplant_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pHTSA:    
      description: 'Acidity level or basicity level observed in the water. Object defining the temporal processing of the magnitude property during a period. It provides maximum, minimum, instant value and average'    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Number''. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Number''. Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Number''. Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Number''. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    po4:    
      description: 'Ortho-phosphate concentration measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    redox:    
      description: 'Reduction potential or oxidation measured in waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    tic:    
      description: 'Total Inorganic Carbon concentration measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tn:    
      description: 'Total Nitrogen concentration measured in waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    toc:    
      description: 'Total Organic Carbon concentration measured in the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    treatmentPlantCapacity:    
      description: 'Handling capacity of the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    treatmentPlantCode:    
      description: 'Unique code for the waste-water treatment plant corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    treatmentPlantId:    
      description: 'Unique identification number for the waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    treatmentPlantName:    
      description: 'Name of the waste-water treatment plant corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    tss:    
      description: 'Total suspended solids concentration measured in a waste-water treatment plant corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be WasteWaterPlant'    
      enum:    
        - WasteWaterPlant    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteWater/blob/master/WasteWaterPlant/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteWater/WasteWaterPlant/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### WasteWaterPlant NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine WasteWaterPlant im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "uri:ngsi-ld:1234:A43R",  
  "type": "WasteWaterPlant",  
  "no3": 10,  
  "bod": 250,  
  "inFlow": 5,  
  "toc": 0.7,  
  "nh4": 50,  
  "redox": 25,  
  "do": 4,  
  "treatmentPlantId": 7,  
  "outFlow": 6.7,  
  "tss": 2,  
  "treatmentPlantCapacity": 10,  
  "tic": 2,  
  "tn": 9,  
  "po4": 6,  
  "cod": 25,  
  "treatmentPlantName": "A",  
  "treatmentPlantCode": "2",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "pHTSA": {  
    "avgOverTime": 8,  
    "maxOverTime": 10,  
    "instValue": 6,  
    "minOverTime": 6  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
#### WasteWaterPlant NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine WasteWaterPlant im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "uri:ngsi-ld:1234:A43R",  
  "type": "WasteWaterPlant",  
  "no3": {  
    "type": "Number",  
    "value": 10  
  },  
  "bod": {  
    "type": "Number",  
    "value": 250  
  },  
  "inFlow": {  
    "type": "Number",  
    "value": 5  
  },  
  "toc": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "nh4": {  
    "type": "Number",  
    "value": 50  
  },  
  "redox": {  
    "type": "Number",  
    "value": 25  
  },  
  "do": {  
    "type": "Number",  
    "value": 4  
  },  
  "treatmentPlantId": {  
    "type": "Number",  
    "value": 7  
  },  
  "outFlow": {  
    "type": "Number",  
    "value": 6.7  
  },  
  "tss": {  
    "type": "Number",  
    "value": 2  
  },  
  "treatmentPlantCapacity": {  
    "type": "Number",  
    "value": 10  
  },  
  "tic": {  
    "type": "Number",  
    "value": 2  
  },  
  "tn": {  
    "type": "Number",  
    "value": 9  
  },  
  "po4": {  
    "type": "Number",  
    "value": 6  
  },  
  "cod": {  
    "type": "Number",  
    "value": 25  
  },  
  "treatmentPlantName": {  
    "type": "Number",  
    "value": "A"  
  },  
  "treatmentPlantCode": {  
    "type": "Number",  
    "value": "2"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "pHTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 8,  
      "maxOverTime": 10,  
      "instValue": 6,  
      "minOverTime": 6  
    }  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
#### WasteWaterPlant NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine WasteWaterPlant im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "uri:ngsi-ld:1234:A43R",  
  "type": "WasteWaterPlant",  
  "no3": 10,  
  "bod": 250,  
  "inFlow": 5,  
  "toc": 0.7,  
  "nh4": 50,  
  "redox": 25,  
  "do": 4,  
  "treatmentPlantId": 7,  
  "outFlow": 6.7,  
  "tss": 2,  
  "treatmentPlantCapacity": 10,  
  "tic": 2,  
  "tn": 9,  
  "po4": 6,  
  "cod": 25,  
  "treatmentPlantName": "A",  
  "treatmentPlantCode": "2",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "pHTSA": {  
    "avgOverTime": 8,  
    "maxOverTime": 10,  
    "instValue": 6,  
    "minOverTime": 6  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  },  
    "@context": "iudx:WasteWaterMgmt"  
}  
```  
#### WasteWaterPlant NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine WasteWaterPlant im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "uri:ngsi-ld:1234:A43R",  
  "type": "WasteWaterPlant",  
  "no3": {  
    "type": "Property",  
    "value": 10  
  },  
  "bod": {  
    "type": "Property",  
    "value": 250  
  },  
  "inFlow": {  
    "type": "Property",  
    "value": 5  
  },  
  "toc": {  
    "type": "Property",  
    "value": 0.7  
  },  
  "nh4": {  
    "type": "Property",  
    "value": 50  
  },  
  "redox": {  
    "type": "Property",  
    "value": 25  
  },  
  "do": {  
    "type": "Property",  
    "value": 4  
  },  
  "treatmentPlantId": {  
    "type": "Property",  
    "value": 7  
  },  
  "outFlow": {  
    "type": "Property",  
    "value": 6.7  
  },  
  "tss": {  
    "type": "Property",  
    "value": 2  
  },  
  "treatmentPlantCapacity": {  
    "type": "Property",  
    "value": 10  
  },  
  "tic": {  
    "type": "Property",  
    "value": 2  
  },  
  "tn": {  
    "type": "Property",  
    "value": 9  
  },  
  "po4": {  
    "type": "Property",  
    "value": 6  
  },  
  "cod": {  
    "type": "Property",  
    "value": 25  
  },  
  "treatmentPlantName": {  
    "type": "Property",  
    "value": "A"  
  },  
  "treatmentPlantCode": {  
    "type": "Property",  
    "value": "2"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "pHTSA": {  
    "type": "Property",  
    "value": {  
      "avgOverTime": 8,  
      "maxOverTime": 10,  
      "instValue": 6,  
      "minOverTime": 6  
    }  
  },  
  "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  },  
  "@context": [  
    "iudx:WasteWaterMgmt",  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
