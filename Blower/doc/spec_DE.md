Entität: Gebläse  
================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/Blower/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines Gebläses, das für die Domäne "Abwasserbehandlung" hergestellt wurde. Die Entität repräsentiert ein Gebläse, das für Belüftungszwecke im Abwasserbehandlungsprozess verwendet wird. Wichtige Parameter werden gemessen, um die Menge des Luftstroms zu regulieren und zu messen, der dem Belüftungsbecken im Bioreaktor zugeführt wird. Der Energieverbrauch eines Gebläses ist ebenfalls eine wichtige Information für die Echtzeitsteuerung und -optimierung der Kläranlage.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `airflow`: Luftstrom, der von einem Gebläse ausgeblasen wird.  - `airflowEstimation`: Luftstromabschätzung durch AI-Soft-Sensor-Simulation.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endsAt`: Eine Beziehung, die die Entität angibt, mit der das Gebläse im nachgeschalteten Punkt verbunden ist.  - `energy`: Energie, die von einem Gebläse verbraucht wird.  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pressure`: Druckmessung im Gebläse.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `startsAt`: Eine Beziehung, die die Entität angibt, mit der das Gebläse im vorgeschalteten Punkt verbunden ist.  - `type`: NGSI-LD Entity Type. Es muss Gebläse sein    
Erforderliche Eigenschaften  
- `description`  - `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Blower:    
  description: 'This entity contains an harmonised description of a Blower made for the Wastewater treatment domain. The entity represents a Blower that are used for aeration purposes in the wastewater treatment process. Important parameters are measured to regulate and measure the amount of airflow is being provided to the aeration tank in the bioreactor. Energy consumption of a blower is also important information for real-time control and optimisation of the wastewater treatment plant.'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    airflow:    
      description: 'Airflow blown by a blower.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' m/s'    
    airflowEstimation:    
      description: 'Airflow estimation by AI soft sensor simulation.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' m/s'    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    endsAt:    
      description: 'A relationship indicating the entity the blower is connected to in the downstream point.'    
      format: uri    
      type: Relationship    
    energy:    
      description: 'Energy consumed by a blower.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' kW'    
    id:    
      anyOf: &blower_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *blower_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pressure:    
      description: 'Pressure measurement in the blower.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' kPa'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    startsAt:    
      description: 'A relationship indicating the entity the blower is connected to in the upstream point.'    
      format: uri    
      type: Relationship    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Blower'    
      enum:    
        - Blower    
      type: Property    
  required:    
    - id    
    - type    
    - description    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Gebläse NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen Blower im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Blower:Blower2",  
  "type": "Blower",  
  "name": "Blower 2",  
  "description": "Blower 2 providing aeration for wastewater treatment process.",  
  "airflow": 368.75,  
  "energy": 229.89,  
  "pressure": 84.06  
}  
```  
#### Gebläse NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Blower im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Blower:Blower2",  
  "type": "Blower",  
  "name": {  
    "type": "Text",  
    "value": "Blower 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Blower 2 providing aeration for wastewater treatment process."  
  },  
  "airflow": {  
    "type": "Number",  
    "value": 368.75  
  },  
  "energy": {  
    "type": "Number",  
    "value": 229.89  
  },  
  "pressure": {  
    "type": "Number",  
    "value": 84.06  
  }  
}  
```  
#### Gebläse NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Blower im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": "https://smartdatamodels.org/context.jsonld",  
  "id": "urn:ngsi-ld:Blower:Blower2",  
  "type": "Blower",  
  "name": "Blower 2",  
  "description": "Blower 2 providing aeration for wastewater treatment process.",  
  "airflow": 368.75,  
  "energy": 229.89,  
  "pressure": 84.06  
}  
```  
#### Gebläse NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Blower im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": "https://smartdatamodels.org/context.jsonld",  
  "id": "urn:ngsi-ld:Blower:Blower2",  
  "type": "Blower",  
  "name": {  
    "type": "Property",  
    "value": "Blower 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Blower 2 providing aeration for wastewater treatment process."  
  },  
  "airflow": {  
    "type": "Property",  
    "value": 368.75  
  },  
  "energy": {  
    "type": "Property",  
    "value": 229.89  
  },  
  "pressure": {  
    "type": "Property",  
    "value": 84.06  
  }  
}  
```  
