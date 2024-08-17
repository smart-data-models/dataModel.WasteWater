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


class Type6(Enum):
    WasteWaterJunction = 'WasteWaterJunction'


class WasteWaterJunction(BaseModel):
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
        description='Biological Oxygen Demand concentration measured in the influent or effluent',
    )
    cod: Optional[float] = Field(
        None,
        description='Chemical Oxygen Demand concentration measured in the influent or effluent',
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
        None, description='Dissolved Oxygen concentration measured in wastewater'
    )
    emissionFlow: Optional[float] = Field(
        None,
        description='Gas emission flow volume measured at a junction prior to being emitted in an off-gas stack',
    )
    endsAt: Optional[AnyUrl] = Field(
        None,
        description='A relationship indicating the entity the junction is connected to in the downstream point',
    )
    flowrate: Optional[float] = Field(None, description='Flowrate of wastewater')
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nh4: Optional[float] = Field(
        None, description='Ammonium concentration measured in a tank'
    )
    no3: Optional[float] = Field(
        None, description='Nitrate concentration measured in wastewater'
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
    pH: Optional[float] = Field(None, description='Water pH level measured')
    po4: Optional[float] = Field(
        None, description='Ortho-phosphate concentration measured in wastewater'
    )
    pressure: Optional[float] = Field(
        None,
        description='Pressure measured at given location. Most relevant for airflow as provided by blowers to wastewater tanks',
    )
    redox: Optional[float] = Field(
        None, description='Redox level measured in wastewater'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startsAt: Optional[AnyUrl] = Field(
        None,
        description='A relationship indicating the entity the junction is connected to in the upstream point',
    )
    temperature: Optional[float] = Field(
        None, description='Wastewater temperature measured'
    )
    tic: Optional[float] = Field(
        None,
        description='Total Inorganic Carbon concentration measured in the influent or effluent',
    )
    tn: Optional[float] = Field(
        None, description='Total Nitrogen concentration measured in wastewater'
    )
    toc: Optional[float] = Field(
        None,
        description='Total Organic Carbon concentration measured in the influent or effluent',
    )
    tss: Optional[float] = Field(
        None, description='total suspended solids concentration measured in a tank'
    )
    type: Optional[Type6] = Field(
        None, description='It has to be WasteWaterJunction. NGSI-LD Entity Type'
    )
