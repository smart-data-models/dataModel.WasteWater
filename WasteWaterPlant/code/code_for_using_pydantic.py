from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class MunicipalityInfo(BaseModel):
    cityId: Optional[str] = Field(
        None, description='City Id corresponding to this observation'
    )
    cityName: Optional[str] = Field(
        None, description='City name corresponding to this observation'
    )
    district: Optional[str] = Field(
        None, description='District name corresponding to this observation'
    )
    stateName: Optional[str] = Field(
        None, description='Name of the state corresponding to this observation'
    )
    ulbName: Optional[str] = Field(
        None,
        description='Name of the Urban Local Body corresponding to this observation',
    )
    wardId: Optional[str] = Field(
        None, description='Ward Id corresponding to this observation'
    )
    wardName: Optional[str] = Field(
        None, description='Ward name corresponding to this observation'
    )
    wardNum: Optional[float] = Field(
        None, description='Ward number corresponding to this observation'
    )
    zoneId: Optional[str] = Field(
        None, description='Zone Id corresponding to this observation'
    )
    zoneName: Optional[str] = Field(
        None, description='Zone name corresponding to this observation'
    )


class PHTSA(BaseModel):
    avgOverTime: Optional[float] = Field(
        None,
        description='Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    instValue: Optional[float] = Field(
        None,
        description='Describes the instantaneous value (associated with the current timestamp) of a time varying quantity',
    )
    maxOverTime: Optional[float] = Field(
        None,
        description='Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    minOverTime: Optional[float] = Field(
        None,
        description='Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )


class Type6(Enum):
    WasteWaterPlant = 'WasteWaterPlant'


class WasteWaterPlant(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bod: Optional[float] = Field(
        None,
        description='Biological Oxygen Demand concentration measured in the waste-water treatment plant corresponding to this observation',
    )
    cod: Optional[float] = Field(
        None,
        description='Chemical Oxygen Demand concentration measured in the waste-water treatment plant corresponding to this observation',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    do: Optional[float] = Field(
        None,
        description='Dissolved oxygen measured in the waste-water treatment plant corresponding to this observation',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    inFlow: Optional[float] = Field(
        None,
        description='In-flow amount into the treatment plant/reservoir corresponding to this observation',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nh4: Optional[float] = Field(
        None,
        description='Ammonium concentration measured in the waste-water treatment plant corresponding to this observation',
    )
    no3: Optional[float] = Field(
        None,
        description='Nitrate concentration measured in waste-water treatment plant corresponding to this observation',
    )
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    outFlow: Optional[float] = Field(
        None,
        description='Out-flow amount into the treatment plant/reservoir corresponding to this observation',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    pHTSA: Optional[PHTSA] = Field(
        None,
        description='Acidity level or basicity level observed in the water. Object defining the temporal processing of the magnitude property during a period. It provides maximum, minimum, instant value and average',
    )
    po4: Optional[float] = Field(
        None,
        description='Ortho-phosphate concentration measured in the waste-water treatment plant corresponding to this observation',
    )
    redox: Optional[float] = Field(
        None,
        description='Reduction potential or oxidation measured in waste-water treatment plant corresponding to this observation',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tic: Optional[float] = Field(
        None,
        description='Total Inorganic Carbon concentration measured in the waste-water treatment plant corresponding to this observation',
    )
    tn: Optional[float] = Field(
        None,
        description='Total Nitrogen concentration measured in waste-water treatment plant corresponding to this observation',
    )
    toc: Optional[float] = Field(
        None,
        description='Total Organic Carbon concentration measured in the waste-water treatment plant corresponding to this observation',
    )
    treatmentPlantCapacity: Optional[float] = Field(
        None,
        description='Handling capacity of the waste-water treatment plant corresponding to this observation',
    )
    treatmentPlantCode: Optional[str] = Field(
        None,
        description='Unique code for the waste-water treatment plant corresponding to this observation',
    )
    treatmentPlantId: Optional[float] = Field(
        None,
        description='Unique identification number for the waste-water treatment plant corresponding to this observation',
    )
    treatmentPlantName: Optional[str] = Field(
        None,
        description='Name of the waste-water treatment plant corresponding to this observation',
    )
    tss: Optional[float] = Field(
        None,
        description='Total suspended solids concentration measured in a waste-water treatment plant corresponding to this observation',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be WasteWaterPlant'
    )
