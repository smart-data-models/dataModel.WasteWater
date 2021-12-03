Entity: OffGasStack  
===================  
[Open License](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/OffGasStack/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of a generic Off-gas Stack made for the Wastewater treatment domain. This entity represents stacks that are present in some wastewater treatment plants where the emissions, greenhouse gases included, are emitted.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `ch4`: CH4 gas emissions from an off-gas stack entity.  - `co2`: CO2 gas emissions from an off-gas stack entity.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `endsAt`: A relationship indicating the entity the Off Gas Stack is connected to in the downstream point.  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `n2o`: N2O gas emissions from an off-gas stack entity.  - `name`: The name of this item.  - `o2`: O2 gas emissions from an off-gas stack entity.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `startsAt`: A relationship indicating the entity the Off Gas Stack is connected to in the upstream point.  - `type`: NGSI-LD Entity Type. it has to be OffGasStack    
Required properties  
- `description`  - `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OffGasStack:    
  description: 'This entity contains a harmonised description of a generic Off-gas Stack made for the Wastewater treatment domain. This entity represents stacks that are present in some wastewater treatment plants where the emissions, greenhouse gases included, are emitted.'    
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
    ch4:    
      description: 'CH4 gas emissions from an off-gas stack entity.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' ppm'    
    co2:    
      description: 'CO2 gas emissions from an off-gas stack entity.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' ppm'    
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
    endsAt:    
      description: 'A relationship indicating the entity the Off Gas Stack is connected to in the downstream point.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &offgasstack_-_properties_-_owner_-_items_-_anyof    
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
    n2o:    
      description: 'N2O gas emissions from an off-gas stack entity.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' ppm'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    o2:    
      description: 'O2 gas emissions from an off-gas stack entity.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: ' ppm'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *offgasstack_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
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
      description: 'A relationship indicating the entity the Off Gas Stack is connected to in the upstream point.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: 'NGSI-LD Entity Type. it has to be OffGasStack'    
      enum:    
        - OffGasStack    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - description    
  type: object    
```  
</details>    
## Example payloads    
#### OffGasStack NGSI-v2 key-values Example    
Here is an example of a OffGasStack in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:OffGasStack:OffGasStack2",  
  "type": "OffGasStack",  
  "name": "Off Gas Stack 2",  
  "description": "Off gas stack from treatment lane 2.",  
  "n2o": 380,  
  "co2": 1.8,  
  "ch4": 35,  
  "o2": 18.6,  
  "startsAt": "urn:ngsi-ld:WasteWaterJunction:junction3",  
  "endsAt": "urn:ngsi-ld:WasteWaterJunction:junction4"  
}  
```  
#### OffGasStack NGSI-v2 normalized Example    
Here is an example of a OffGasStack in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:OffGasStack:OffGasStack2",  
  "type": "OffGasStack",  
  "name": {  
    "type": "Text",  
    "value": "Off Gas Stack 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Off gas stack from treatment lane 2."  
  },  
  "n2o": {  
    "type": "Number",  
    "value": 380  
  },  
  "co2": {  
    "type": "Number",  
    "value": 1.8  
  },  
  "ch4": {  
    "type": "Number",  
    "value": 35  
  },  
  "o2": {  
    "type": "Number",  
    "value": 18.6  
  },  
  "startsAt": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WasteWaterJunction:junction3"  
  },  
  "endsAt": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WasteWaterJunction:junction4"  
  }  
}  
```  
#### OffGasStack NGSI-LD key-values Example    
Here is an example of a OffGasStack in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": "https://smartdatamodels.org/context.jsonld",  
  "id": "urn:ngsi-ld:OffGasStack:OffGasStack2",  
  "type": "OffGasStack",  
  "name": "Off Gas Stack 2",  
  "description": "Off gas stack from treatment lane 2.",  
  "n2o": 380,  
  "co2": 1.8,  
  "ch4": 35,  
  "o2": 18.6,  
  "startsAt": "urn:ngsi-ld:WasteWaterJunction:junction3",  
  "endsAt": "urn:ngsi-ld:WasteWaterJunction:junction4"  
}  
```  
#### OffGasStack NGSI-LD normalized Example    
Here is an example of a OffGasStack in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
  "id": "urn:ngsi-ld:OffGasStack:OffGasStack2",  
  "type": "OffGasStack",  
  "name": {  
    "type": "Property",  
    "value": "Off Gas Stack 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Off gas stack from treatment lane 2."  
  },  
  "n2o": {  
    "type": "Property",  
    "value": 380  
  },  
  "co2": {  
    "type": "Property",  
    "value": 1.8  
  },  
  "ch4": {  
    "type": "Property",  
    "value": 35  
  },  
  "o2": {  
    "type": "Property",  
    "value": 18.6  
  },  
  "startsAt": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:WasteWaterJunction:junction3"  
  },  
  "endsAt": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:WasteWaterJunction:junction4"  
  }  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units