import datetime
import copy

from ckanext.publicamundi.lib.metadata.types import *

## Objects ##

pt1 = Point(x=0.76, y=0.23)

contact1 = ContactInfo(
    email = u'somebody@example.com', 
    address = PostalAddress(address=u'Nowhere Land', postalcode=u'12321'))

poly1 = Polygon(name = u'Poly1', points=[
    Point(x=0.6, y=0.5), Point(x=0.7, y=0.1),
    Point(x=1.6, y=0.2), Point(x=0.6, y=0.5),])

poly2 = Polygon(name = u'Poly2', points=[
    Point(x=7.9, y=0.8), Point(x=1.3, y=0.2),
    Point(x=1.6, y=0.2), Point(x=7.9, y=0.8),])

dt1 = TemporalExtent(
    start = datetime.date(2014, 5, 27),
    end = datetime.date(2014, 5, 29))

foo1 = Foo(
    baz = u'Bazzz',
    title = u'Ababoua Ababoua',
    tags = [ u'alpha', u'beta', u'gamma'],
    url = 'http://example.com',
    contact_info = ContactInfo(email=u'nomad@somewhere.com', address=None),
    contacts = {
        'personal':  ContactInfo(email=u'nobody@example.com', address=PostalAddress(address=u'North Pole', postalcode=u'54321')),
        'office': ContactInfo(email=None, address=PostalAddress(address=u'South Pole', postalcode=u'12345')),
    },
    geometry = [[ poly1, poly2 ]],
    reviewed = False,
    created = datetime.datetime(2014, 06, 11),
    wakeup_time = datetime.time(8, 0, 0),
    notes = u'Hello World',
    thematic_category = 'economy',
    temporal_extent = dt1,
    rating = 0,
    grade = 13.7,
    password = u'secret',
)

# Find schema validation errors: originating_vocabulary,date_type
fkw1 = FreeKeyword(value = u"val", reference_date = datetime.date(1000,1,1),date_type = "creationn")

# Find schema validation invariant error - not all fields set
fkw2 = FreeKeyword(value = u"val", reference_date = datetime.date.today(),date_time = 'creation')

# Validate correct schema
fkw_correct = FreeKeyword(
    value = u"val",
    originating_vocabulary = u"original",
    reference_date = datetime.date.today(),
    date_type = 'creation')

# Find schema validation errors: all not float
gbb1 = GeographicBoundingBox(nblat = 50,sblat = 50,wblng = 40,eblng= 30)

# Find schema validation errors - nblat, wblng greater than max allowed
gbb2 = GeographicBoundingBox(nblat = -1235.0,sblat = 0.0 ,eblng = 123.123 ,wblng = 1235.0)

# Validate correct schema
gbb_correct = GeographicBoundingBox(nblat = -50.0, sblat = -20.12, wblng = 15.0, eblng = 1.0)

# Find schema validation errors: start missing
te1 = TemporalExtent(end = datetime.date.today())

# Find schema validation errors: start not date
te2 = TemporalExtent(start = 2015, end = datetime.date.today())

# Find schema invariant error - start date greater than end date
te3 = TemporalExtent(start = datetime.date(2015,01,01),end = datetime.date.today())

# Validate correct schema
te_correct = TemporalExtent(start = datetime.date.today(), end = datetime.date(2015,01,01))

# Find schema validation errors date, creation, degree'''
cnf1 = Conformity(title = u"lala", date = 2015,date_type = "creationn", degree = "confofrmant")
# '''Validate correct schema'''
cnf_correct = Conformity(title = u"lala",date = datetime.date.today(),date_type = "creation", degree = "conformant")

# Find schema validation error - distance not int
sr1 = SpatialResolution(distance = 5.0, uom = u"lala")

# Find schema invariant error - not all values set
sr2 = SpatialResolution(distance = 5)

# Validate correct schema - no values set
sr3 = SpatialResolution()

# Validate correct schema
sr_correct = SpatialResolution(distance = 5, uom = u"lala")

# Thesauri
thesaurus_gemet_concepts = Thesaurus(
    title = u'GEMET Concepts',
    name = 'keywords-gemet-concepts',
    reference_date = datetime.date(2014, 1, 1),
    date_type = 'creation'
)

thesaurus_gemet_themes = Thesaurus(
    title = u'GEMET Themes',
    name = 'keywords-gemet-themes',
    reference_date = datetime.date(2014, 5, 1),
    date_type = 'creation'
)

thesaurus_gemet_inspire_data_themes = Thesaurus(
    title = u'GEMET INSPIRE Data Themes',
    name = 'keywords-gemet-inspire-data-themes',
    reference_date = datetime.date(2014, 6, 1),
    date_type = 'publication'
)
