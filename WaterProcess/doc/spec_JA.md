<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティウォータープロセス    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.WasteWater/blob/master/WaterProcess/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**このデータモデルは、浄水場または浄水処理場における水のプロセスに関する情報を提供することを意図している。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alkalinity[number]`: ポンプステーションの取水量。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コード。  . Model: [https://schema.org/Number](https://schema.org/Number)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: 生物化学的酸素要求量（BOD）とは、ある水試料中に存在する有機物を、ある温度で、ある時間にわたって分解するために、好気性生物によって必要とされる（すなわち要求される）溶存酸素（DO）の量のことである。  - `chromaticity[number]`: 処理水の色度。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コード。  . Model: [https://schema.org/Number](https://schema.org/Number)- `cod[number]`: 化学的酸素要求量（COD）は、測定された溶液中の反応によって消費される酸素の量を示す指標である。  - `contactPoint[object]`: 商品に関するお問い合わせ先  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: サービスまたは提供品が提供される地理的地域。serviceAreaより優先されます。      
	- `availabilityRestriction[*]`: このプロパティは、コンタクトポイントと、そのコンタクトポイントが利用できない時間帯に関する情報とをリンクする。詳細は、営業時間指定クラスを使用して提供されます。  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)    
	- `availableLanguage[*]`: そのアイテム、サービス、場所で誰かが使う可能性のある言語。IETF BCP 47標準の言語コードのいずれかを使用してください。Text」オプションが実装されていますが、「Language」でもかまいません。  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)    
	- `contactOption[*]`: このコンタクトポイントで利用可能なオプション（フリーダイヤルや聴覚障害者へのサポートなど）  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)    
	- `contactType[string]`: このアイテムのコンタクトタイプ      
	- `email[idn-email]`: 所有者のEメールアドレス      
	- `faxNumber[string]`: ファックス番号  . Model: [http://schema.org/Text](http://schema.org/Text)    
	- `name[string]`: このアイテムの名前      
	- `productSupported[string]`: このサポートコンタクトポイントが関連する製品またはサービス（特定の製品ラインの製品サポートなど）。これは、特定の製品または製品ライン（例：「iPhone」）または製品やサービスの一般的なカテゴリ（例：「スマートフォン」）とすることができます。  . Model: [http://schema.org/Text](http://schema.org/Text)    
	- `telephone[string]`: 連絡先の電話番号      
- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `operationStatus[string]`:   . Model: [https://schema.org/Text.ss The operation status of the water proce](https://schema.org/Text.ss The operation status of the water proce)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pH[number]`: 水溶液の酸性度または塩基性度  - `residualChlorine[number]`: ポンプステーションの取水量。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コード。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `temperature[number]`: 処理水の温度。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コード。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tn[number]`: 全窒素  . Model: [https://schema.org/Number](https://schema.org/Number)- `tp[number]`: 全リン  . Model: [https://schema.org/Number](https://schema.org/Number)- `tss[number]`: 総懸濁物質  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidity[number]`: 水柱中の粒子によって散乱される光の量。単位：NTU  - `type[string]`: NGSIエンティティタイプ。WaterProcessでなければならない。  - `waterProcessType[string]`: 浄水場または水処理場（別名：排水処理場）における水処理の種類  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
    alkalinity:      
      description: 'The intake volume of the pump station. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
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
      description: 'The chromaticity of the processed water. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
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
      description: The details to contact with the item      
      properties:      
        areaServed:      
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea      
          type: string      
          x-ngsi:      
            type: Property      
        availabilityRestriction:      
          anyOf:      
            - description: Array of identifiers format of any NGSI entity      
              items:      
                maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
              type: array      
              x-ngsi:      
                type: Property      
            - description: Array of identifiers format of any NGSI entity      
              items:      
                format: uri      
                type: string      
              type: array      
              x-ngsi:      
                type: Property      
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class      
          x-ngsi:      
            model: http://schema.org/hoursAvailable      
            type: Relationship      
        availableLanguage:      
          anyOf:      
            - anyOf:      
                - type: string      
                - items:      
                    type: string      
                  type: array      
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'      
          x-ngsi:      
            model: http://schema.org/availableLanguage      
            type: Property      
        contactOption:      
          anyOf:      
            - type: string      
            - items:      
                type: string      
              type: array      
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)      
          x-ngsi:      
            model: http://schema.org/contactOption      
            type: Property      
        contactType:      
          description: Contact type of this item      
          type: string      
          x-ngsi:      
            type: Property      
        email:      
          description: Email address of owner      
          format: idn-email      
          type: string      
          x-ngsi:      
            type: Property      
        faxNumber:      
          description: The fax number      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        name:      
          description: The name of this item      
          type: string      
          x-ngsi:      
            type: Property      
        productSupported:      
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        telephone:      
          description: Telephone of this contact      
          type: string      
          x-ngsi:      
            type: Property      
        url:      
          description: URL which provides a description or further information about this item      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/ContactPoint      
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
    operationStatus:      
      description: ""      
      enum:      
        - normal      
        - watch      
        - warning      
      type: string      
      x-ngsi:      
        model: 'https://schema.org/Text.ss The operation status of the water proce'      
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
    pH:      
      description: Acidity or basicity of an aqueous solution      
      maximum: 14      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    residualChlorine:      
      description: 'The intake volume of the pump station. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    temperature:      
      description: 'The temperature of the processed water. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
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
      description: The type of water process at water purification plant or water treatment plant (aka. waste water treatment plant)      
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
## ペイロードの例    
#### WaterProcess NGSI-v2 キー値の例    
JSON-LD形式のWaterProcessのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
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
#### WaterProcess NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のWaterProcessの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:waterdna:haemil:WaterProcess_01",  
  "type": "WaterProcess",  
  "location": {  
    "type": "geo:json",  
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
#### WaterProcess NGSI-LD キー値の例    
JSON-LD形式のWaterProcessのkey-valuesの例である。これはNGSI-LDと互換性があり、`options=keyValues`を使うと個々のエンティティのコンテキストデータを返す。    
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
#### WaterProcess NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のWaterProcessの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
