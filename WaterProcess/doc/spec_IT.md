<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AcquaProcesso  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WaterProcess/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello di dati è destinato a fornire informazioni sul processo dell'acqua in un impianto di depurazione o di trattamento dell'acqua**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alkalinity[number]`: Il volume di aspirazione della stazione di pompaggio. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: La domanda biochimica di ossigeno (BOD) è la quantità di ossigeno disciolto (DO) necessaria (cioè richiesta) dagli organismi biologici aerobici per scomporre il materiale organico presente in un determinato campione d'acqua a una certa temperatura per un periodo di tempo specifico.  - `chromaticity[number]`: La cromaticità dell'acqua trattata. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `cod[number]`: La domanda chimica di ossigeno (COD) è una misura indicativa della quantità di ossigeno che può essere consumata dalle reazioni in una soluzione misurata.  - `contactPoint[object]`: I dettagli da contattare con l'articolo.  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `operationStatus[string]`:   . Model: [https://schema.org/Text.ss The operation status of the water proce.](https://schema.org/Text.ss The operation status of the water proce.)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pH[number]`: Acidità o basicità di una soluzione acquosa.  - `residualChlorine[number]`: Il volume di aspirazione della stazione di pompaggio. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `temperature[number]`: La temperatura dell'acqua trattata. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `tn[number]`: Azoto totale  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: Fosforo totale  . Model: [https://schema.org/Number](https://schema.org/Number)- `tss[number]`: Solidi sospesi totali  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidity[number]`: Quantità di luce diffusa dalle particelle nella colonna d'acqua. Unità:'NTU  - `type[string]`: Tipo di entità NGSI. Deve essere WaterProcess  - `waterProcessType[string]`: Il tipo di processo dell'acqua presso l'impianto di depurazione dell'acqua o l'impianto di trattamento dell'acqua (anche detto impianto di trattamento delle acque reflue).  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterProcess:    
  description: The data model is intended to provide information about water process at water purification plant or water treatment plant    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alkalinity:    
      description: 'The intake volume of the pump station. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: cubic metre per second    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bod:    
      description: Biochemical oxygen demand (BOD) is the amount of dissolved oxygen (DO) needed (i.e. demanded) by aerobic biological organisms to break down organic material present in a given water sample at certain temperature over a specific time period    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    chromaticity:    
      description: 'The chromaticity of the processed water. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: none    
    cod:    
      description: Chemical oxygen demand (COD) is an indicative measure of the amount of oxygen that can be consumed by reactions in a measured solution    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    contactPoint:    
      description: The details to contact with the item.    
      properties:    
        areaServed:    
          description: Property. The geographic area where a service or offered item is provided. Supersedes serviceArea.    
          type: string    
        availabilityRestriction:    
          anyOf:    
            - description: Property. Array of identifiers format of any NGSI entity.    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
            - description: Property. Array of identifiers format of any NGSI entity.    
              items:    
                format: uri    
                type: string    
              type: array    
          description: 'Relationship. Model:''http://schema.org/hoursAvailable''. This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class.'    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'Property. Model:''http://schema.org/availableLanguage''. A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: 'Property. Model:''http://schema.org/contactOption''. An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).'    
        contactType:    
          description: Property. Contact type of this item.    
          type: string    
        email:    
          description: Property. Email address of owner.    
          format: idn-email    
          type: string    
        faxNumber:    
          description: 'Property. Model:''http://schema.org/Text''. The fax number.'    
          type: string    
        name:    
          description: Property. The name of this item.    
          type: string    
        productSupported:    
          description: 'Property. Model:''http://schema.org/Text''. The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").'    
          type: string    
        telephone:    
          description: Property. Telephone of this contact.    
          type: string    
        url:    
          description: Property. URL which provides a description or further information about this item.    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &waterprocess_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    operationStatus:    
      description: ""    
      enum:    
        - normal    
        - watch    
        - warning    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text.ss The operation status of the water proce.'    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *waterprocess_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    pH:    
      description: Acidity or basicity of an aqueous solution.    
      maximum: 14    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    residualChlorine:    
      description: 'The intake volume of the pump station. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: cubic metre per second    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    temperature:    
      description: 'The temperature of the processed water. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: celsius    
    tn:    
      description: Total nitrogen    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: mg/l    
    tp:    
      description: Total phosphorus    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: mg/l    
    tss:    
      description: Total suspended solids    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: mg/l    
    turbidity:    
      description: 'Amount of light scattered by particles in the water column. Unit:''NTU'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be WaterProcess    
      enum:    
        - WaterProcess    
      type: string    
      x-ngsi:    
        type: Property    
    waterProcessType:    
      description: The type of water process at water purification plant or water treatment plant (aka. waste water treatment plant).    
      enum:    
        - inflow    
        - sedimentation    
        - filtration    
        - disinfection    
        - waterTreatment    
        - primarySedimentation    
        - bioreactor    
        - effluent    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteWater/blob/master/WaterProcess/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteWater/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### WaterProcess NGSI-v2 valori-chiave Esempio  
Ecco un esempio di WaterProcess in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:waterdna:haemil:WaterProcess_01",  
  "type": "WaterProcess",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      127.266663,  
      36.524677  
    ]  
  },  
  "name": "inflow process at water treatment plant 1",  
  "waterProcessType": "inflow",  
  "tn": 73.152,  
  "tp": 6.1,  
  "tss": 130.9  
}  
```  
</details>  
#### WaterProcess NGSI-v2 normalizzato Esempio  
Ecco un esempio di WaterProcess in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:waterdna:haemil:WaterProcess_01",  
  "type": "WaterProcess",  
  "location": {  
    "type": "geo:sjon",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        127.266663,  
        36.524677  
      ]  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "inflow process at water treatment plant 1"  
  },  
  "waterProcessType": {  
    "type": "Text",  
    "value": "inflow"  
  },  
  "tn": {  
    "type": "Number",  
    "value": 73.152  
  },  
  "tp": {  
    "type": "Number",  
    "value": 6.1  
  },  
  "tss": {  
    "type": "Number",  
    "value": 130.9  
  }  
}  
```  
</details>  
#### WaterProcess Valori-chiave NGSI-LD Esempio  
Ecco un esempio di WaterProcess in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:waterdna:haemil:WaterProcess_01",  
  "type": "WaterProcess",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      127.266663,  
      36.524677  
    ]  
  },  
  "name": "inflow process at water treatment plant 1",  
  "waterProcessType": "inflow",  
  "tn": 73.152,  
  "tp": 6.1,  
  "tss": 130.9,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "http://uri.citydatahub.kr/ngsi-ld/water.jsonld"  
  ]  
}  
```  
</details>  
#### WaterProcess NGSI-LD normalizzato Esempio  
Ecco un esempio di WaterProcess in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:waterdna:haemil:WaterProcess_01",  
  "type": "WaterProcess",  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        127.266663,  
        36.524677  
      ]  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "inflow process at water treatment plant 1"  
  },  
  "waterProcessType": {  
    "type": "Property",  
    "value": "inflow"  
  },  
  "tn": {  
    "type": "Property",  
    "value": 73.152  
  },  
  "tp": {  
    "type": "Property",  
    "value": 6.1  
  },  
  "tss": {  
    "type": "Property",  
    "value": 130.9  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "http://uri.citydatahub.kr/ngsi-ld/water.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
