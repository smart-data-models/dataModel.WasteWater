Entidad: WasteWaterTank  
=======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterTank/LICENSE.md)  

## Lista de propiedades  

Propiedades requeridas  
- No hay propiedades requeridas  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
    endsAt:    
      description: 'A relationship indicating the entity the tank is connected to in the downstream point'    
      format: uri    
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
        anyOf: *wastewatertank_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pH:    
      description: 'Water pH level measured.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
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
    sludgeLevel:    
      description: 'Sludge Level measured in a secondary settler tank'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' metre'    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    startsAt:    
      description: 'A relationship indicating the entity the tank is connected to in the upstream point'    
      format: uri    
      type: Relationship    
    temperature:    
      description: 'Wastewater temperature measured.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: ' Celsius'    
    tn:    
      description: 'Total Nitrogen concentration measured in wastewater.'    
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
      description: 'NGSI-LD Entity Type. It has to be WasteWaterTank'    
      enum:    
        - WasteWaterTank    
      type: Property    
  required:    
    - id    
    - type    
    - name    
    - description    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### WasteWaterTank NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un WasteWaterTank en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### WasteWaterTank NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un WasteWaterTank en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
#### WasteWaterTank NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un WasteWaterTank en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### WasteWaterTank NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un WasteWaterTank en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
