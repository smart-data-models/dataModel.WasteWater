<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: WasteWaterPlant    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterPlant/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Modelo de datos para planta de tratamiento de aguas residuales.**    
versión: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: Concentración de demanda biológica de oxígeno medida en la estación depuradora de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `cod[number]`: Concentración de demanda química de oxígeno medida en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `do[number]`: Oxígeno disuelto medido en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `inFlow[number]`: Caudal de entrada en la depuradora/embalse correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `municipalityInfo[object]`: Información municipal correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: Id de ciudad correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: Nombre de la ciudad correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: Nombre del distrito correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: Nombre del estado correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: Nombre de la Entidad Local Urbana correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: Ward Id correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: Nombre del pabellón correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: Número de pabellón correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: Id de zona correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: El nombre de este artículo  - `nh4[number]`: Concentración de amonio medida en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `no3[number]`: Concentración de nitrato medida en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `observationDateTime[date-time]`: Última hora de observación comunicada  . Model: [https://schema.org/Text](https://schema.org/Text)- `outFlow[number]`: Caudal de salida en la depuradora/embalse correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `pHTSA[object]`: Nivel de acidez o basicidad observado en el agua. Objeto que define el tratamiento temporal de la propiedad magnitud durante un período. Proporciona el valor máximo, mínimo, instantáneo y medio.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `avgOverTime[number]`: Describe el valor medio de los datos de una serie temporal a lo largo de una duración especificada en el pasado. La duración se especifica utilizando otro parámetro en el objeto descriptor de valor relacionado con este valor  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: Describe el valor instantáneo (asociado a la marca de tiempo actual) de una cantidad variable en el tiempo  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: Describe el valor máximo de los datos de una serie temporal a lo largo de una duración especificada en el pasado. La duración se especifica utilizando otro parámetro en el objeto descriptor de valor relacionado con este valor  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `po4[number]`: Concentración de ortofosfato medida en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `redox[number]`: Potencial de reducción u oxidación medido en la planta de tratamiento de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tic[number]`: Concentración de carbono inorgánico total medida en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `tn[number]`: Concentración de nitrógeno total medida en la estación depuradora de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `toc[number]`: Concentración de carbono orgánico total medida en la depuradora correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `treatmentPlantCapacity[number]`: Capacidad de tratamiento de la estación depuradora de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `treatmentPlantCode[string]`: Código único de la estación depuradora de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `treatmentPlantId[number]`: Número único de identificación de la estación depuradora de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `treatmentPlantName[string]`: Nombre de la estación depuradora de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `tss[number]`: Concentración total de sólidos en suspensión medida en una planta de tratamiento de aguas residuales correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Tiene que ser WasteWaterPlant  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
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
## Ejemplo de carga útil    
#### WasteWaterPlant NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de una WasteWaterPlant en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### WasteWaterPlant NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de WasteWaterPlant en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
#### WasteWaterPlant NGSI-LD key-values Ejemplo    
He aquí un ejemplo de una WasteWaterPlant en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### WasteWaterPlant NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de WasteWaterPlant en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
