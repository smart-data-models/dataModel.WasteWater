<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。水过程  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WaterProcess/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该数据模型旨在提供有关净水厂或水处理厂的水处理过程的信息**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alkalinity[number]`: 泵站的吸入量。所有单位都接受[CEFACT](https://www.unece.org/cefact.html)代码。  . Model: [https://schema.org/Number](https://schema.org/Number)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: 生化需氧量（BOD）是指在特定的温度下，在特定的时间段内，好氧生物体分解存在于特定水样中的有机物所需要（即需求）的溶解氧量。  - `chromaticity[number]`: 处理后的水的色度。所有单位都接受[CEFACT](https://www.unece.org/cefact.html)代码。  . Model: [https://schema.org/Number](https://schema.org/Number)- `cod[number]`: 化学需氧量（COD）是衡量被测溶液中可被反应消耗掉的氧气量的指示性指标  - `contactPoint[object]`: 与该物品联系的细节。  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `operationStatus[string]`:   . Model: [https://schema.org/Text.ss The operation status of the water proce.](https://schema.org/Text.ss The operation status of the water proce.)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pH[number]`: 水溶液的酸度或碱度。  - `residualChlorine[number]`: 泵站的吸入量。所有单位都接受[CEFACT](https://www.unece.org/cefact.html)代码。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `temperature[number]`: 处理过的水的温度。所有单位都接受[CEFACT](https://www.unece.org/cefact.html)代码。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tn[number]`: 总氮  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 总磷  . Model: [https://schema.org/Number](https://schema.org/Number)- `tss[number]`: 悬浮物总量  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidity[number]`: 水体中的颗粒散射的光量。单位：'NTU  - `type[string]`: NGSI实体类型。它必须是WaterProcess  - `waterProcessType[string]`: 净水厂或水处理厂（又称废水处理厂）的水工艺类型。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
## ＃＃＃＃有效载荷的例子  
#### WaterProcess NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为关键值的WaterProcess的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### WaterProcess NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的WaterProcess的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### WaterProcess NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为关键值的WaterProcess的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### WaterProcess NGSI-LD 归一化实例  
下面是一个以JSON-LD格式规范化的WaterProcess的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
