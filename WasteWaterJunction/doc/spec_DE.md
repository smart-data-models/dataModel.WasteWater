Entität: WasteWaterJunction  
===========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterJunction/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Dieses Element enthält eine harmonisierte Beschreibung einer generischen Abzweigung, die für den Bereich der Abwasserbehandlung erstellt wurde. Abzweigungen können in bestimmten Abschnitten der Aufbereitungsanlage vorhanden sein. In der Abwasseraufbereitung ist die Abzweigung am nützlichsten, wenn sie ein Standort eines Sensors ist, der eine bestimmte Variable misst.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `bod`: Propety. Konzentration des biologischen Sauerstoffbedarfs, gemessen im Zulauf oder Ablauf.  - `cod`: Chemische Sauerstoffbedarfskonzentration, gemessen im Zulauf oder Ablauf.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `do`: Konzentration des gelösten Sauerstoffs, gemessen im Abwasser.  - `emissionFlow`: Gasemissionsvolumenstrom, der an einer Verbindungsstelle gemessen wird, bevor er in einem Abgaskamin emittiert wird.  - `endsAt`: Eine Beziehung, die die Entität angibt, mit der der Knotenpunkt im nachgelagerten Punkt verbunden ist  - `flowrate`: Durchflussmenge des Abwassers.  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `nh4`: Ammoniumkonzentration, gemessen in einem Tank.  - `no3`: Nitratkonzentration im Abwasser gemessen.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pH`: Der pH-Wert des Wassers wird gemessen.  - `po4`: Ortho-Phosphat-Konzentration im Abwasser gemessen.  - `redox`: Redoxlevel im Abwasser gemessen.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `startsAt`: Eine Beziehung, die die Entität angibt, mit der der Knotenpunkt im vorgelagerten Punkt verbunden ist  - `temperature`: Temperatur des Abwassers gemessen.  - `tic`: Gesamte anorganische Kohlenstoffkonzentration, gemessen im Zulauf oder Ablauf.  - `tn`: Gesamt-Stickstoffkonzentration, gemessen im Abwasser.  - `toc`: Konzentration des gesamten organischen Kohlenstoffs, gemessen im Zulauf oder Ablauf.  - `tss`: Konzentration der gesamten suspendierten Feststoffe, die in einem Tank gemessen wird.  - `type`: Es muss WasteWaterJunction sein. NGSI-LD Entity Typ    
Erforderliche Eigenschaften  
- `description`  - `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteWaterJunction:    
  description: 'This entity contains an harmonised description of a generic Junction made for the Wastewater treatment domain. Junctions could be in place in certain sections of thetreatment plant. In wastewater treatment purposes, the junction is most useful if it is a locationof a sensor that measures a specific variable.'    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    bod:    
      description: 'Propety. Biological Oxygen Demand concentration measured in the influent or effluent.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    cod:    
      description: 'Chemical Oxygen Deman concentration measured in the influent or effluent.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
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
    do:    
      description: 'Dissolved Oxygen concentration measured in wastewater.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    emissionFlow:    
      description: 'Gas emission flow volume measured at a junction prior to being emitted in an off-gas stack.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' m3'    
    endsAt:    
      description: 'A relationship indicating the entity the junction is connected to in the downstream point'    
      format: uri    
      type: Relationship    
    flowrate:    
      description: 'Flowrate of wastewater.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' m3/h'    
    id:    
      anyOf: &wastewaterjunction_-_properties_-_owner_-_items_-_anyof    
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
    nh4:    
      description: 'Ammonium concentration measured in a tank.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    no3:    
      description: 'Nitrate concentration measured in wastewater.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastewaterjunction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pH:    
      description: 'Water pH level measured.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
    po4:    
      description: 'Ortho-phosphate concentration measured in wastewater.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    redox:    
      description: 'Redox level measured in wastewater.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mV'    
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
      description: 'A relationship indicating the entity the junction is connected to in the upstream point'    
      format: uri    
      type: Relationship    
    temperature:    
      description: 'Wastewater temperature measured.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' Celsius'    
    tic:    
      description: 'Total Inorganic Carbon concentration measured in the influent or effluent.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    tn:    
      description: 'Total Nitrogen concentration measured in wastewater.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    toc:    
      description: 'Total Organic Carbon concentration measured in the influent or effluent.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    tss:    
      description: 'total suspended solids concentration measured in a tank.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' mg/L'    
    type:    
      description: 'It has to be WasteWaterJunction. NGSI-LD Entity Type'    
      enum:    
        - WasteWaterJunction    
      type: Property    
  required:    
    - id    
    - type    
    - description    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### WasteWaterJunction NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine WasteWaterJunction im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:WasteWaterJunction:junction2",  
  "type": "WasteWaterJunction",  
  "name": "Junction 2",  
  "description": "A junction in the treatment lane representing a sampling location for the effluent wastewater.",  
  "nh4": 0.5,  
  "no3": 5.2,  
  "do": 1.2,  
  "redox": 250,  
  "tn": 7.18,  
  "toc": 16.28,  
  "po4": 0.29,  
  "bod": 2.44,  
  "cod": 36.6,  
  "flowrate": 27650,  
  "temperature": 16,  
  "pH": 7.8,  
  "startsAt": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
}  
```  
#### WasteWaterJunction NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine WasteWaterJunction im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:WasteWaterJunction:junction2",  
  "type": "WasteWaterJunction",  
  "name": {  
    "type": "Text",  
    "value": "Junction 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "A junction in the treatment lane representing a sampling location for the effluent wastewater."  
  },  
  "nh4": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "no3": {  
    "type": "Number",  
    "value": 5.2  
  },  
  "do": {  
    "type": "Number",  
    "value": 1.2  
  },  
  "redox": {  
    "type": "Number",  
    "value": 250  
  },  
  "tn": {  
    "type": "Number",  
    "value": 7.18  
  },  
  "toc": {  
    "type": "Number",  
    "value": 16.28  
  },  
  "po4": {  
    "type": "Number",  
    "value": 0.29  
  },  
  "bod": {  
    "type": "Number",  
    "value": 2.44  
  },  
  "cod": {  
    "type": "Number",  
    "value": 36.6  
  },  
  "flowrate": {  
    "type": "Number",  
    "value": 27650  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 16  
  },  
  "pH": {  
    "type": "Number",  
    "value": 7.8  
  },  
  "startsAt": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
  }  
}  
```  
#### WasteWaterJunction NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine WasteWaterJunction im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": "https://smartdatamodels.org/context.jsonld",  
  "id": "urn:ngsi-ld:WasteWaterJunction:junction2",  
  "type": "WasteWaterJunction",  
  "name": "Junction 2",  
  "description": "A junction in the treatment lane representing a sampling location for the effluent wastewater.",  
  "nh4": 0.5,  
  "no3": 5.2,  
  "do": 1.2,  
  "redox": 250,  
  "tn": 7.18,  
  "toc": 16.28,  
  "po4": 0.29,  
  "bod": 2.44,  
  "cod": 36.6,  
  "flowrate": 27650,  
  "temperature": 16,  
  "pH": 7.8,  
  "startsAt": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
}  
```  
#### WasteWaterJunction NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine WasteWaterJunction im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
[  
  {  
    "@context": "https://smartdatamodels.org/context.jsonld",  
    "id": "urn:ngsi-ld:WasteWaterJunction:junction2",  
    "type": "WasteWaterJunction",  
    "name": {  
      "type": "Property",  
      "value": "Junction 2"  
    },  
    "description": {  
      "type": "Property",  
      "value": "A junction in the treatment lane representing a sampling location for the effluent wastewater."  
    },  
    "nh4": {  
      "type": "Property",  
      "value": 0.5  
    },  
    "no3": {  
      "type": "Property",  
      "value": 5.2  
    },  
    "do": {  
      "type": "Property",  
      "value": 1.2  
    },  
    "redox": {  
      "type": "Property",  
      "value": 250  
    },  
    "tn": {  
      "type": "Property",  
      "value": 7.18  
    },  
    "toc": {  
      "type": "Property",  
      "value": 16.28  
    },  
    "po4": {  
      "type": "Property",  
      "value": 0.29  
    },  
    "bod": {  
      "type": "Property",  
      "value": 2.44  
    },  
    "cod": {  
      "type": "Property",  
      "value": 36.6  
    },  
    "flowrate": {  
      "type": "Property",  
      "value": 27650  
    },  
    "temperature": {  
      "type": "Property",  
      "value": 16  
    },  
    "pH": {  
      "type": "Property",  
      "value": 7.8  
    },  
    "startsAt": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
    }  
  }  
]  
```  
