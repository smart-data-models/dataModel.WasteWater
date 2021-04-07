Entity: WasteWaterJunction  
==========================  
[Open License](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterJunction/LICENSE.md)  
Global description: **This entity contains an harmonised description of a generic Junction made for the Wastewater treatment domain. Junctions could be in place in certain sections of thetreatment plant. In wastewater treatment purposes, the junction is most useful if it is a locationof a sensor that measures a specific variable.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `bod`: Propety. Biological Oxygen Demand concentration measured in the influent or effluent.  - `cod`: Chemical Oxygen Deman concentration measured in the influent or effluent.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `do`: Dissolved Oxygen concentration measured in wastewater.  - `emissionFlow`: Gas emission flow volume measured at a junction prior to being emitted in an off-gas stack.  - `endsAt`: A relationship indicating the entity the junction is connected to in the downstream point  - `flowrate`: Flowrate of wastewater.  - `id`: Unique identifier of the entity  - `location`:   - `name`: The name of this item.  - `nh4`: Ammonia concentration measured in a tank.  - `no3`: Nitrate concentration measured in wastewater.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pH`: Water pH level measured.  - `po4`: Ortho-phosphate concentration measured in wastewater.  - `redox`: Redox level measured in wastewater.  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `startsAt`: A relationship indicating the entity the junction is connected to in the upstream point  - `temperature`: Wastewater temperature measured.  - `tic`: Total Inorganic Carbon concentration measured in the influent or effluent.  - `tn`: Total Nitrogen concentration measured in wastewater.  - `toc`: Total Organic Carbon concentration measured in the influent or effluent.  - `tss`: total suspended solids concentration measured in a tank.  - `type`: It has to be WasteWaterJunction. NGSI-LD Entity Type    
Required properties  
- `description`  - `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
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
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nh4:    
      description: 'Ammonia concentration measured in a tank.'    
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
            - format: uri    
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
## Example payloads    
#### WasteWaterJunction NGSI-v2 key-values Example    
Here is an example of a WasteWaterJunction in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### WasteWaterJunction NGSI-v2 normalized Example    
Here is an example of a WasteWaterJunction in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### WasteWaterJunction NGSI-LD key-values Example    
Here is an example of a WasteWaterJunction in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### WasteWaterJunction NGSI-LD normalized Example    
Here is an example of a WasteWaterJunction in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
