import zope.interface
import zope.schema
import copy
import json
import datetime
from ckanext.publicamundi.tests.helpers import assert_faulty_keys
from ckanext.publicamundi.lib.metadata.types import *

#
# Responsible Party
#

# Fixtures 

# Schema validation errors, name, email not list
rp1 = ResponsibleParty(organization = "Non unicode name", email = "non unicode email",role = "Author")

# Schema validation errors, empty fields
rp2 = ResponsibleParty(organization = u"org",email = [u""])

# Schema validation errors, email not correct
rp3 = ResponsibleParty(organization = u"unicode name",email = ["unicodenon@email"],role = u"author")

# No schema errors
rp_correct = ResponsibleParty(organization = u"org",email = [u"correct@email.com",u"asd@asda.asd",u"asdasd@asdasd.asd"],role = "author")

# Tests 

def test_rp1():
    ''' Responsible Party validation errors, name, email not list'''
    assert_faulty_keys(field=rp1, expected_keys=set(['organization', 'email', 'role']))


def test_rp2():
    ''' Responsible Party validation errors, empty fields'''
    assert_faulty_keys(field=rp2, expected_keys=set(['email', 'role']))


def test_rp3():
    ''' Responsible Party validation errors, email not correct'''
    assert_faulty_keys(field=rp3, expected_keys=set(['email']))


def test_rp4():
    '''Responsible Party correct schema'''
    assert_faulty_keys(field=rp_correct)


#
# Conformity
#

# Fixtures

# '''Find schema validation errors date, creation, degree'''
cnf1 = Conformity(title = u"lala", date = 2015,date_type = "creationn", degree = "confofrmant")
# '''Validate correct schema'''
cnf_correct = Conformity(title = u"lala",date = datetime.date.today(),date_type = "creation", degree = "conformant")

# Tests

def test_cnf1():
    '''Conformity validation errors date, creation, degree'''
    assert_faulty_keys(field=cnf1, expected_keys=set(['date', 'date_type', 'degree']))


def test_cnf2():
    '''Conformity correct schema'''
    assert_faulty_keys(field=cnf_correct)


#
# Free keywords
#

# Fixtures

# '''Find schema validation errors: originating_vocabulary,date_type'''
fkw1 = FreeKeyword(value = u"val", reference_date = datetime.date(1000,1,1),date_type = "creationn")

# '''Find schema validation invariant error - not all fields set'''
fkw2 = FreeKeyword(value = u"val", reference_date = datetime.date.today(),date_time = 'creation')

# '''Validate correct schema'''
fkw_correct = FreeKeyword(value = u"val",originating_vocabulary = u"original",reference_date = datetime.date.today(),date_type = 'creation')

# Tests

def test_fkw1():
    '''Free Keywords validation errors: originating_vocabulary,date_type'''
    assert_faulty_keys(field=fkw1, expected_keys=set(['date_type']))


def test_fkw2():
    '''Free Keywords validation invariant error - not all fields set'''
    assert_faulty_keys(field=fkw2, expected_keys=set(['__after']), expected_invariants=["You need to fill in the rest Free Keyword fields"])


def test_fkw3():
    '''Free Keywords correct schema'''
    assert_faulty_keys(field=fkw_correct)



#
# Geographic BBox
#

# Fixtures

# '''Find schema validation errors: all not float'''
gbb1 = GeographicBoundingBox(nblat = 50,sblat = 50,wblng = 40,eblng= 30)

#'''Find schema validation errors - nblat, wblng greater than max allowed'''
gbb2 = GeographicBoundingBox(nblat = -1235.0,sblat = 0.0 ,eblng = 123.123 ,wblng = 1235.0)

# '''Validate correct schema'''
gbb_correct = GeographicBoundingBox(nblat = -50.0, sblat = -20.12, wblng = 15.0, eblng = 1.0)

# Tests

def test_gbb1():
    '''GBBox validation errors: all not float'''
    assert_faulty_keys(field=gbb1, expected_keys=set(['nblat', 'sblat', 'eblng', 'wblng']))


def test_gbb2():
    '''GBBox validation errors - nblat, wblng greater than max allowed'''
    assert_faulty_keys(field=gbb2, expected_keys=set(['nblat', 'wblng']))


def test_gbb3():
    '''GBBox correct schema'''
    assert_faulty_keys(field=gbb_correct)


#
# Temporal Extent
#

# Fixtures

# '''Find schema validation errors: start missing'''
te1 = TemporalExtent(end = datetime.date.today())

# '''Find schema validation errors: start not date'''
te2 = TemporalExtent(start = 2015, end = datetime.date.today())

# '''Find schema invariant error - start date greater than end date'''
te3 = TemporalExtent(start = datetime.date(2015,01,01),end = datetime.date.today())

# '''Validate correct schema'''
te_correct = TemporalExtent(start = datetime.date.today(), end = datetime.date(2015,01,01))

# Tests

def test_te1():
    '''Temporal Extent validation errors: start not date'''
    assert_faulty_keys(field=te1, expected_keys=set(['start']))


def test_te2():
    '''Temporal Extent validation errors: start not date'''
    assert_faulty_keys(field=te2, expected_keys=set(['start']))


def test_te3():
    '''Temporal Extent invariant error - start date greater than end date'''
    assert_faulty_keys(field=te3, expected_keys=set(['__after']), expected_invariants=["later than end date"])


def test_te4():
    '''Temporal Extent correct schema'''
    assert_faulty_keys(field=te_correct)


#
# Spatial Resolution
#

# Fixtures

# '''Find schema validation error - distance not int '''
sr1 = SpatialResolution(distance = 5.0, uom = u"lala")

# '''Find schema invariant error - not all values set'''
sr2 = SpatialResolution(distance = 5)

# '''Validate correct schema - no values set'''
sr3 = SpatialResolution()

#'''Validate correct schema'''
sr_correct = SpatialResolution(distance = 5, uom = u"lala")

# Tests

def test_sr1():
    '''Spatial Resolution validation error - distance not int '''
    assert_faulty_keys(field=sr1, expected_keys=set(['distance']))


def test_sr2():
    '''Spatial Resolution invariant error - not all values set'''
    assert_faulty_keys(field=sr2, expected_keys=set(['__after']), expected_invariants=["You need to fill in the rest Spatial Resolution fields"])


def test_sr3():
    '''Spatial Resolution correct schema - no values set'''
    assert_faulty_keys(field=sr3)


def test_sr4():
    '''Spatial Resolution correct schema'''
    assert_faulty_keys(field=sr_correct)


# Main #

if __name__ == '__main__':
    test_rp1()
    test_rp2()
    test_rp3()
    test_rp4()
