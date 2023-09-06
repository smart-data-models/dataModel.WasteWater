<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：废水交汇处  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WasteWaterJunction/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**该实体包含对废水处理领域通用连接点的统一描述。污水处理厂的某些部分可能会有连接点。在废水处理中，如果交界处是测量特定变量的传感器位置，则交界处最为有用**。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: 进水或出水中测得的生物需氧量浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `cod[number]`: 进水或出水中测得的化学需氧量浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `do[number]`: 测量废水中的溶解氧浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `emissionFlow[number]`: 在废气烟囱排放前在交界处测量的气体排放流量  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `endsAt[uri]`: 表示连接点与下游点中的实体相连的关系  - `flowrate[number]`: 废水流量  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `nh4[number]`: 在水槽中测量铵浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `no3[number]`: 测量废水中的硝酸盐浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pH[number]`: 测量水的 pH 值  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `po4[number]`: 废水中测得的正磷酸盐浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `pressure[number]`: 在指定位置测得的压力。与废水池鼓风机提供的气流最为相关  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `redox[number]`: 测量废水中的氧化还原水平  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `startsAt[uri]`: 表示连接点在上游点连接的实体的关系  - `temperature[number]`: 测量废水温度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tic[number]`: 进水或出水中测得的无机碳总浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tn[number]`: 测量废水中的总氮浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `toc[number]`: 进水或出水中测得的总有机碳浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `tss[number]`: 罐中测量的总悬浮固体浓度  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `type[string]`: 必须是 WasteWaterJunction。NGSI-LD 实体类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `description`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### WasteWaterJunction NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的 WasteWaterJunction 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### WasteWaterJunction NGSI-v2 normalized 示例  
下面是一个规范化 JSON-LD 格式的 WasteWaterJunction 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### WasteWaterJunction NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 WasteWaterJunction 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### WasteWaterJunction NGSI-LD normalized 示例  
下面是一个规范化 JSON-LD 格式的 WasteWaterJunction 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
