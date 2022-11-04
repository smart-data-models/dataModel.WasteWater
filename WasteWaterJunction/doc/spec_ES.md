<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: WasteWaterJunction  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterJunction/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esta entidad contiene una descripción armonizada de un empalme genérico realizado para el ámbito del tratamiento de aguas residuales. Los empalmes pueden estar situados en determinadas secciones de la planta de tratamiento. En el ámbito del tratamiento de aguas residuales, el empalme es más útil si se trata de la ubicación de un sensor que mide una variable específica.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: Concentración de demanda biológica de oxígeno medida en el afluente o el efluente.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `cod[number]`: Concentración de demanda química de oxígeno medida en el afluente o el efluente.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `do[number]`: Concentración de oxígeno disuelto medida en las aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `emissionFlow[number]`: Volumen de flujo de emisión de gas medido en un cruce antes de ser emitido en una chimenea de gases.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `endsAt[string]`: Una relación que indica la entidad a la que está conectada la unión en el punto posterior  - `flowrate[number]`: Caudal de aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `nh4[number]`: Concentración de amonio medida en un tanque.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `no3[number]`: Concentración de nitratos medida en las aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pH[number]`: Medición del nivel de pH del agua.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `po4[number]`: Concentración de ortofosfato medida en las aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `pressure[number]`: Presión medida en un lugar determinado. Más relevante para el flujo de aire proporcionado por los sopladores a los depósitos de aguas residuales  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `redox[number]`: Nivel de redox medido en las aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startsAt[string]`: Una relación que indica la entidad a la que está conectada la unión en el punto anterior  - `temperature[number]`: Medición de la temperatura de las aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tic[number]`: Concentración de carbono inorgánico total medida en el afluente o el efluente.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tn[number]`: Concentración de nitrógeno total medida en las aguas residuales.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `toc[number]`: Concentración de carbono orgánico total medida en el afluente o el efluente.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tss[number]`: concentración total de sólidos en suspensión medida en un tanque.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `type[string]`: Tiene que ser WasteWaterJunction. Tipo de entidad NGSI-LD  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `description`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
      description: 'Biological Oxygen Demand concentration measured in the influent or effluent.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    cod:    
      description: 'Chemical Oxygen Demand concentration measured in the influent or effluent.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
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
      description: 'Dissolved Oxygen concentration measured in wastewater.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    emissionFlow:    
      description: 'Gas emission flow volume measured at a junction prior to being emitted in an off-gas stack.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' m3'    
    endsAt:    
      description: 'A relationship indicating the entity the junction is connected to in the downstream point'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    flowrate:    
      description: 'Flowrate of wastewater.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
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
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nh4:    
      description: 'Ammonium concentration measured in a tank.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    no3:    
      description: 'Nitrate concentration measured in wastewater.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastewaterjunction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pH:    
      description: 'Water pH level measured.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    po4:    
      description: 'Ortho-phosphate concentration measured in wastewater.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    pressure:    
      description: 'Pressure measured at given location. Most relevant for airflow as provided by blowers to wastewater tanks'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' kPa'    
    redox:    
      description: 'Redox level measured in wastewater.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startsAt:    
      description: 'A relationship indicating the entity the junction is connected to in the upstream point'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    temperature:    
      description: 'Wastewater temperature measured.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' Celsius'    
    tic:    
      description: 'Total Inorganic Carbon concentration measured in the influent or effluent.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    tn:    
      description: 'Total Nitrogen concentration measured in wastewater.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    toc:    
      description: 'Total Organic Carbon concentration measured in the influent or effluent.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    tss:    
      description: 'total suspended solids concentration measured in a tank.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    type:    
      description: 'It has to be WasteWaterJunction. NGSI-LD Entity Type'    
      enum:    
        - WasteWaterJunction    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - description    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteWater/blob/master/WasteWaterJunction/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/specs/WasteWaterTreatment/WasteWaterJunction/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### WasteWaterJunction NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una WasteWaterJunction en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### WasteWaterJunction NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una WasteWaterJunction en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### WasteWaterJunction NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una WasteWaterJunction en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WasteWaterJunction:junction2",  
    "type": "WasteWaterJunction",  
    "bod": 2.44,  
    "cod": 36.6,  
    "description": "A junction in the treatment lane representing a sampling location for the effluent wastewater.",  
    "do": 1.2,  
    "flowrate": 27650,  
    "name": "Junction 2",  
    "nh4": 0.5,  
    "no3": 5.2,  
    "pH": 7.8,  
    "po4": 0.29,  
    "redox": 250,  
    "startsAt": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a",  
    "temperature": 16,  
    "tn": 7.18,  
    "toc": 16.28,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteWater/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### WasteWaterJunction NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una WasteWaterJunction en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WasteWaterJunction:junction2",  
    "type": "WasteWaterJunction",  
    "bod": {  
        "type": "Property",  
        "value": 2.44  
    },  
    "cod": {  
        "type": "Property",  
        "value": 36.6  
    },  
    "description": {  
        "type": "Property",  
        "value": "A junction in the treatment lane representing a sampling location for the effluent wastewater."  
    },  
    "do": {  
        "type": "Property",  
        "value": 1.2  
    },  
    "flowrate": {  
        "type": "Property",  
        "value": 27650  
    },  
    "name": {  
        "type": "Property",  
        "value": "Junction 2"  
    },  
    "nh4": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "no3": {  
        "type": "Property",  
        "value": 5.2  
    },  
    "pH": {  
        "type": "Property",  
        "value": 7.8  
    },  
    "po4": {  
        "type": "Property",  
        "value": 0.29  
    },  
    "redox": {  
        "type": "Property",  
        "value": 250  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 16  
    },  
    "tn": {  
        "type": "Property",  
        "value": 7.18  
    },  
    "toc": {  
        "type": "Property",  
        "value": 16.28  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteWater/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
