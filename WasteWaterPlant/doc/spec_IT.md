<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Impianto acque reflue    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterPlant/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Modello di dati per impianto di trattamento delle acque reflue.**    
versione: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: Concentrazione di Domanda Biologica di Ossigeno misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `cod[number]`: Concentrazione della domanda chimica di ossigeno misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `do[number]`: Ossigeno disciolto misurato nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `inFlow[number]`: Quantità di flusso in entrata nell'impianto di trattamento/serbatoio corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `municipalityInfo[object]`: Informazioni sul comune corrispondenti a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: Id della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: Nome della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: Nome del distretto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: Nome dello stato corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: Nome dell'Ente Locale Urbano corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: Ward Id corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: Nome del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: Numero del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: Id della zona corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: Il nome di questo elemento  - `nh4[number]`: Concentrazione di ammonio misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `no3[number]`: Concentrazione di nitrati misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `observationDateTime[date-time]`: Ultima ora di osservazione segnalata  . Model: [https://schema.org/Text](https://schema.org/Text)- `outFlow[number]`: Quantità di flusso in uscita nell'impianto di trattamento/serbatoio corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pHTSA[object]`: Livello di acidità o basicità osservato nell'acqua. Oggetto che definisce l'elaborazione temporale della proprietà magnitudo durante un periodo. Fornisce il valore massimo, minimo, istantaneo e medio.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `avgOverTime[number]`: Descrive il valore medio di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: Descrive il valore istantaneo (associato al timestamp corrente) di una quantità variabile nel tempo.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: Descrive il valore massimo di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `po4[number]`: Concentrazione di ortofosfato misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `redox[number]`: Potenziale di riduzione o di ossidazione misurato nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `tic[number]`: Concentrazione di carbonio inorganico totale misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `tn[number]`: Concentrazione di azoto totale misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `toc[number]`: Concentrazione di carbonio organico totale misurata nell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `treatmentPlantCapacity[number]`: Capacità di gestione dell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `treatmentPlantCode[string]`: Codice univoco dell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `treatmentPlantId[number]`: Numero di identificazione univoco dell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `treatmentPlantName[string]`: Nome dell'impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `tss[number]`: Concentrazione totale di solidi sospesi misurata in un impianto di trattamento delle acque reflue corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo di entità NGSI. Deve essere WasteWaterPlant  <!-- /30-PropertiesList -->    
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
WasteWaterPlant:      
  description: Data model for waste water treatment plant.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
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
      description: Biological Oxygen Demand concentration measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    cod:      
      description: Chemical Oxygen Demand concentration measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    do:      
      description: Dissolved oxygen measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    inFlow:      
      description: In-flow amount into the treatment plant/reservoir corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
      x-ngsi:      
        type: GeoProperty      
    municipalityInfo:      
      description: Municipality information corresponding to this observation      
      properties:      
        cityId:      
          description: City Id corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        cityName:      
          description: City name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        district:      
          description: District name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        stateName:      
          description: Name of the state corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        ulbName:      
          description: Name of the Urban Local Body corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardId:      
          description: Ward Id corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardName:      
          description: Ward name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardNum:      
          description: Ward number corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        zoneId:      
          description: Zone Id corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        zoneName:      
          description: Zone name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nh4:      
      description: Ammonium concentration measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    no3:      
      description: Nitrate concentration measured in waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    outFlow:      
      description: Out-flow amount into the treatment plant/reservoir corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    pHTSA:      
      description: 'Acidity level or basicity level observed in the water. Object defining the temporal processing of the magnitude property during a period. It provides maximum, minimum, instant value and average'      
      properties:      
        avgOverTime:      
          description: Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        instValue:      
          description: Describes the instantaneous value (associated with the current timestamp) of a time varying quantity      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        maxOverTime:      
          description: Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        minOverTime:      
          description: Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    po4:      
      description: Ortho-phosphate concentration measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    redox:      
      description: Reduction potential or oxidation measured in waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    tic:      
      description: Total Inorganic Carbon concentration measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tn:      
      description: Total Nitrogen concentration measured in waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    toc:      
      description: Total Organic Carbon concentration measured in the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    treatmentPlantCapacity:      
      description: Handling capacity of the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    treatmentPlantCode:      
      description: Unique code for the waste-water treatment plant corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    treatmentPlantId:      
      description: Unique identification number for the waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    treatmentPlantName:      
      description: Name of the waste-water treatment plant corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    tss:      
      description: Total suspended solids concentration measured in a waste-water treatment plant corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: NGSI entity type. It has to be WasteWaterPlant      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WasteWater/blob/master/WasteWaterPlant/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteWater/WasteWaterPlant/schema.json      
  x-model-tags: IUDX      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### WasteWaterPlant Valori-chiave NGSI-v2 Esempio    
Ecco un esempio di WasteWaterPlant in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### WasteWaterPlant NGSI-v2 normalizzato Esempio    
Ecco un esempio di WasteWaterPlant in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
    "type": "Text",  
    "value": "A"  
  },  
  "treatmentPlantCode": {  
    "type": "Text",  
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
</details>    
#### WasteWaterPlant Valori chiave NGSI-LD Esempio    
Ecco un esempio di WasteWaterPlant in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi-ld:1234:A43R",  
  "type": "WasteWaterPlant",  
  "bod": 250,  
  "cod": 25,  
  "do": 4,  
  "inFlow": 5,  
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
  "nh4": 50,  
  "no3": 10,  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "outFlow": 6.7,  
  "pHTSA": {  
    "avgOverTime": 8,  
    "maxOverTime": 10,  
    "instValue": 6,  
    "minOverTime": 6  
  },  
  "po4": 6,  
  "redox": 25,  
  "tic": 2,  
  "tn": 9,  
  "toc": 0.7,  
  "treatmentPlantCapacity": 10,  
  "treatmentPlantCode": "2",  
  "treatmentPlantId": 7,  
  "treatmentPlantName": "A",  
  "tss": 2,  
  "@context": [  
    "iudx:WasteWaterMgmt",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteWater/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WasteWaterPlant NGSI-LD normalizzato Esempio    
Ecco un esempio di WasteWaterPlant in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "uri:ngsi-ld:1234:A43R",  
    "type": "WasteWaterPlant",  
    "bod": {  
        "type": "Property",  
        "value": 250  
    },  
    "cod": {  
        "type": "Property",  
        "value": 25  
    },  
    "do": {  
        "type": "Property",  
        "value": 4  
    },  
    "inFlow": {  
        "type": "Property",  
        "value": 5  
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
    "nh4": {  
        "type": "Property",  
        "value": 50  
    },  
    "no3": {  
        "type": "Property",  
        "value": 10  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "outFlow": {  
        "type": "Property",  
        "value": 6.7  
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
    "po4": {  
        "type": "Property",  
        "value": 6  
    },  
    "redox": {  
        "type": "Property",  
        "value": 25  
    },  
    "tic": {  
        "type": "Property",  
        "value": 2  
    },  
    "tn": {  
        "type": "Property",  
        "value": 9  
    },  
    "toc": {  
        "type": "Property",  
        "value": 0.7  
    },  
    "treatmentPlantCapacity": {  
        "type": "Property",  
        "value": 10  
    },  
    "treatmentPlantCode": {  
        "type": "Property",  
        "value": "2"  
    },  
    "treatmentPlantId": {  
        "type": "Property",  
        "value": 7  
    },  
    "treatmentPlantName": {  
        "type": "Property",  
        "value": "A"  
    },  
    "tss": {  
        "type": "Property",  
        "value": 2  
    },  
    "@context": [  
        "iudx:WasteWaterMgmt",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteWater/master/context.jsonld"  
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
