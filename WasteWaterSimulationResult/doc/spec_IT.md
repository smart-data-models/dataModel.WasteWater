Entità: WasteWaterSimulationResult  
==================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterSimulationResult/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un WasteWaterSimulationResults fatta per il dominio del trattamento delle acque reflue. L'entità contiene proprietà che sono parametri che sono stati predetti o previsti da modelli attraverso una simulazione **.  
versione: 0.0.1  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `airflow`: Stima del flusso d'aria da una soffiante generata attraverso l'aerazione di una data entità di acque reflue, mediante un modello di simulazione/dati-driven.  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `nh4`: Stima della concentrazione di ammoniaca in una data entità di acque reflue, mediante un modello di simulazione/dati-driven.  - `no3`: Stima della concentrazione di nitrati in una data entità di acque reflue, mediante un modello di simulazione/dati-driven.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `power`: Stima della potenza consumata da una soffiante per il processo di aerazione ad una data entità di acque reflue, mediante un modello di simulazione/dati.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio pienamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo di entità NGSI-LD. Deve essere un WasteWaterSimulationResults.    
Proprietà richieste  
- `id`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteWaterSimulationResult:    
  description: 'This entity contains an harmonised description of a WasteWaterSimulationResults made for the Wastewater treatment domain. The entity contains properties that are parameters which have been predicted or forecasted by models through a simulation.'    
  modelTags: FIWARE4WATER    
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
    airflow:    
      description: 'Estimation of airflow from a blower generated through aeration of a given wastewater entity, by a simulation/data-driven model.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' m/s'    
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
    id:    
      anyOf: &wastewatersimulationresult_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nh4:    
      description: 'Estimation of ammonia concentration at a given wastewater entity, by a simulation/data-driven model.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    no3:    
      description: 'Estimation of nitrate concentration at a given wastewater entity, by a simulation/data-driven model.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastewatersimulationresult_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    power:    
      description: 'Estimation of power consumed by a blower for the aeration process to a given wastewater entity, by a simulation/data-driven model.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' kW'    
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
    type:    
      description: 'NGSI-LD Entity Type. It has to be a WasteWaterSimulationResults.'    
      enum:    
        - WasteWaterSimulationResult    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### WasteWaterSimulationResult NGSI-v2 valori chiave Esempio  
Ecco un esempio di un WasteWaterSimulationResult in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:WasteWaterSimulationResults:dataValidation",  
  "type": "WasteWaterSimulationResult",  
  "name": "Data Validation",  
  "description": "AI-based data validation application. Simulation of NH4 and NO3 parameters in aerobic tank of bioreactor using deep learning models.",  
  "nh4": 1.83,  
  "no3": 6.27  
}  
```  
#### WasteWaterSimulationResult NGSI-v2 normalizzato Esempio  
Ecco un esempio di un WasteWaterSimulationResult in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:WasteWaterSimulationResults:dataValidation",  
  "type": "WasteWaterSimulationResult",  
  "name": {  
    "type": "Text",  
    "value": "Data Validation"  
  },  
  "description": {  
    "type": "Text",  
    "value": "AI-based data validation application. Simulation of NH4 and NO3 parameters in aerobic tank of bioreactor using deep learning models."  
  },  
  "nh4": {  
    "type": "Number",  
    "value": 1.83  
  },  
  "no3": {  
    "type": "Number",  
    "value": 6.27  
  }  
}  
```  
#### WasteWaterSimulationResultato NGSI-LD valori chiave Esempio  
Ecco un esempio di un WasteWaterSimulationResult in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
  "id": "urn:ngsi-ld:WasteWaterSimulationResults:dataValidation",  
  "type": "WasteWaterSimulationResult",  
  "name": "Data Validation",  
  "description": "AI-based data validation application. Simulation of NH4 and NO3 parameters in aerobic tank of bioreactor using deep learning models.",  
  "nh4": 1.83,  
  "no3": 6.27  
}  
```  
#### WasteWaterSimulationResultato NGSI-LD normalizzato Esempio  
Ecco un esempio di un WasteWaterSimulationResult in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:WasteWaterSimulationResults:dataValidation",  
  "type": "WasteWaterSimulationResult",  
  "name": {  
    "type": "Property",  
    "value": "Data Validation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "AI-based data validation application. Simulation of NH4 and NO3 parameters in aerobic tank of bioreactor using deep learning models."  
  },  
  "nh4": {  
    "type": "Property",  
    "value": 1.83,  
    "providedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:WasteWaterTank:aerobicTank02"  
    }  
  },  
  "no3": {  
    "type": "Property",  
    "value": 6.27,  
    "providedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:WasteWaterTank:aerobicTank02"  
    }  
  },  
  "@context": "https://smartdatamodels.org/context.jsonld"  
}  
```  
