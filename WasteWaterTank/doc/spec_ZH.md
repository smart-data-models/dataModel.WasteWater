<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

======
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)
<!-- 35-RequiredProperties -->

- `description`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

WasteWaterTank:    
  description: 'This entity contains an harmonised description of a generic Tank made for the Wastewater treatment domain. For a given type of tank, all possible variables that can be measures are listed as properties. In the description property, the type of tank (anaerobic, pre-dinitrification, nitrification etc.)can be defined.'    
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
      description: 'Object defining the actual and estimated airflow'    
      properties:    
        estimated:    
          description: 'Property. Model: https://schema.org/Number. Units: ''m/s''. Airflow estimated by a model.'    
          type: number    
        measured:    
          description: 'Property. Model: https://schema.org/Number. Units: ''m/s''. Airflow measured by a device.'    
          type: number    
      type: object    
      x-ngsi:    
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
    endsAt:    
      description: 'A relationship indicating the entity the tank is connected to in the downstream point'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &wastewatertank_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *wastewatertank_-_properties_-_owner_-_items_-_anyof    
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
    power:    
      description: 'Object defining the actual and estimated power consumption'    
      properties:    
        estimated:    
          description: 'Property. Model: https://schema.org/Number. Units: ''kW''. Power estimated by a model.'    
          type: number    
        measured:    
          description: 'Property. Model: https://schema.org/Number. Units: ''kW''. Power measured by a device.'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
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
    sludgeLevel:    
      description: 'Sludge Level measured in a secondary settler tank'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' metre'    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startsAt:    
      description: 'A relationship indicating the entity the tank is connected to in the upstream point'    
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
    tn:    
      description: 'Total Nitrogen concentration measured in wastewater.'    
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
      description: 'NGSI-LD Entity Type. It has to be WasteWaterTank'    
      enum:    
        - WasteWaterTank    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - description    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteWater/blob/master/WasteWaterTank/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/specs/WasteWaterTreatment/WasteWaterTank/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:WasteWaterTank:aerobicTank2",  
  "type": "WasteWaterTank",  
  "name": "Aerobic Tank 2",  
  "description": "Aerobic tank in treatment lane 2.",  
  "tss": 3500,  
  "nh4": 1.3,  
  "no3": 5.2,  
  "do": 1.2,  
  "redox": 250,  
  "sludgeLevel": 0.8,  
  "temperature": 16,  
  "pH": 7.8,  
  "startsAt": "urn:ngsi-ld:WasteWaterTank:facultativeTank2",  
  "endsAt": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:WasteWaterTank:aerobicTank2",  
  "type": "WasteWaterTank",  
  "name": {  
    "type": "Text",  
    "value": "Aerobic Tank 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Aerobic tank in treatment lane 2."  
  },  
  "tss": {  
    "type": "Number",  
    "value": 3500  
  },  
  "nh4": {  
    "type": "Number",  
    "value": 1.3  
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
  "sludgeLevel": {  
    "type": "Number",  
    "value": 0.8  
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
    "value": "urn:ngsi-ld:WasteWaterTank:facultativeTank2"  
  },  
  "endsAt": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:WasteWaterTank:aerobicTank2",  
    "type": "WasteWaterTank",  
    "description": "Aerobic tank in treatment lane 2.",  
    "do": 1.2,  
    "endsAt": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a",  
    "name": "Aerobic Tank 2",  
    "nh4": 1.3,  
    "no3": 5.2,  
    "pH": 7.8,  
    "redox": 250,  
    "sludgeLevel": 0.8,  
    "startsAt": "urn:ngsi-ld:WasteWaterTank:facultativeTank2",  
    "temperature": 16,  
    "tss": 3500,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteWater/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:WasteWaterTank:aerobicTank2",  
    "type": "WasteWaterTank",  
    "description": {  
        "type": "Property",  
        "value": "Aerobic tank in treatment lane 2."  
    },  
    "do": {  
        "type": "Property",  
        "value": 1.2  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WasteWaterTank:secondarySettler2a"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Aerobic Tank 2"  
    },  
    "nh4": {  
        "type": "Property",  
        "value": 1.3  
    },  
    "no3": {  
        "type": "Property",  
        "value": 5.2  
    },  
    "pH": {  
        "type": "Property",  
        "value": 7.8  
    },  
    "redox": {  
        "type": "Property",  
        "value": 250  
    },  
    "sludgeLevel": {  
        "type": "Property",  
        "value": 0.8  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WasteWaterTank:facultativeTank2"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 16  
    },  
    "tss": {  
        "type": "Property",  
        "value": 3500  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
