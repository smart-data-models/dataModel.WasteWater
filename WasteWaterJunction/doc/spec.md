<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: WasteWaterJunction  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterJunction/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains an harmonised description of a generic Junction made for the Wastewater treatment domain. Junctions could be in place in certain sections of thetreatment plant. In wastewater treatment purposes, the junction is most useful if it is a locationof a sensor that measures a specific variable.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: Biological Oxygen Demand concentration measured in the influent or effluent  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `cod[number]`: Chemical Oxygen Demand concentration measured in the influent or effluent  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `do[number]`: Dissolved Oxygen concentration measured in wastewater  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `emissionFlow[number]`: Gas emission flow volume measured at a junction prior to being emitted in an off-gas stack  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `endsAt[uri]`: A relationship indicating the entity the junction is connected to in the downstream point  - `flowrate[number]`: Flowrate of wastewater  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `nh4[number]`: Ammonium concentration measured in a tank  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `no3[number]`: Nitrate concentration measured in wastewater  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pH[number]`: Water pH level measured  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `po4[number]`: Ortho-phosphate concentration measured in wastewater  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `pressure[number]`: Pressure measured at given location. Most relevant for airflow as provided by blowers to wastewater tanks  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `redox[number]`: Redox level measured in wastewater  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `startsAt[uri]`: A relationship indicating the entity the junction is connected to in the upstream point  - `temperature[number]`: Wastewater temperature measured  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tic[number]`: Total Inorganic Carbon concentration measured in the influent or effluent  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tn[number]`: Total Nitrogen concentration measured in wastewater  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `toc[number]`: Total Organic Carbon concentration measured in the influent or effluent  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tss[number]`: total suspended solids concentration measured in a tank  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `type[string]`: It has to be WasteWaterJunction. NGSI-LD Entity Type  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `description`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteWaterJunction:    
  description: 'This entity contains an harmonised description of a generic Junction made for the Wastewater treatment domain. Junctions could be in place in certain sections of thetreatment plant. In wastewater treatment purposes, the junction is most useful if it is a locationof a sensor that measures a specific variable.'    
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
      description: Biological Oxygen Demand concentration measured in the influent or effluent    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    cod:    
      description: Chemical Oxygen Demand concentration measured in the influent or effluent    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
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
      description: Dissolved Oxygen concentration measured in wastewater    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    emissionFlow:    
      description: Gas emission flow volume measured at a junction prior to being emitted in an off-gas stack    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' m3'    
    endsAt:    
      description: A relationship indicating the entity the junction is connected to in the downstream point    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    flowrate:    
      description: Flowrate of wastewater    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' m3/h'    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nh4:    
      description: Ammonium concentration measured in a tank    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    no3:    
      description: Nitrate concentration measured in wastewater    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
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
    pH:    
      description: Water pH level measured    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    po4:    
      description: Ortho-phosphate concentration measured in wastewater    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    pressure:    
      description: Pressure measured at given location. Most relevant for airflow as provided by blowers to wastewater tanks    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' kPa'    
    redox:    
      description: Redox level measured in wastewater    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mV'    
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
    startsAt:    
      description: A relationship indicating the entity the junction is connected to in the upstream point    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    temperature:    
      description: Wastewater temperature measured    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' Celsius'    
    tic:    
      description: Total Inorganic Carbon concentration measured in the influent or effluent    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    tn:    
      description: Total Nitrogen concentration measured in wastewater    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    toc:    
      description: Total Organic Carbon concentration measured in the influent or effluent    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    tss:    
      description: total suspended solids concentration measured in a tank    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' mg/L'    
    type:    
      description: It has to be WasteWaterJunction. NGSI-LD Entity Type    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## Example payloads    
#### WasteWaterJunction NGSI-v2 key-values Example    
Here is an example of a WasteWaterJunction in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### WasteWaterJunction NGSI-v2 normalized Example    
Here is an example of a WasteWaterJunction in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### WasteWaterJunction NGSI-LD key-values Example    
Here is an example of a WasteWaterJunction in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### WasteWaterJunction NGSI-LD normalized Example    
Here is an example of a WasteWaterJunction in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
