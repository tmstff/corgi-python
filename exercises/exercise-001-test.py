#!/usr/bin/python

##Import modules

import pytest
import Aufgabe1

## TESTS

def test_GesamtgewichtLOOP():
    assert Aufgabe1.GesamtgewichtLOOP([]) == 0
    assert Aufgabe1.GesamtgewichtLOOP([1]) == 1
    assert Aufgabe1.GesamtgewichtLOOP([6,6,6]) == 18

def test_DurchschnittsGewichtLOOP():
    assert Aufgabe1.DurchschnittsgewichtLOOP([]) == 0
    assert Aufgabe1.DurchschnittsgewichtLOOP([2]) == 2
    assert Aufgabe1.DurchschnittsgewichtLOOP([8,6,4]) == 6
	
	
def test_Corgikategorisierung():
	assert Aufgabe1.Corgikategorisierung(  []) == []
	with pytest.raises(Exception):
		Aufgabe1.Corgikategorisierung([-1])
	assert Aufgabe1.Corgikategorisierung( [5]) == ["kleiner Corgi"]
	assert Aufgabe1.Corgikategorisierung( [9]) == ["kleiner Corgi"]
	assert Aufgabe1.Corgikategorisierung([10]) == ["mittlerer Corgi"]
	assert Aufgabe1.Corgikategorisierung([15]) == ["mittlerer Corgi"]
	assert Aufgabe1.Corgikategorisierung([19]) == ["mittlerer Corgi"]
	assert Aufgabe1.Corgikategorisierung([20]) == ["grosser Corgi"]
	assert Aufgabe1.Corgikategorisierung([25]) == ["grosser Corgi"]
	
def test_DicksterCorgi():
	with pytest.raises(Exception):
		Aufgabe1.DicksterCorgi([])
	assert Aufgabe1.DicksterCorgi([0]) == 0
	assert Aufgabe1.DicksterCorgi([9, 12, 7]) == 12

	
test_GesamtgewichtLOOP()
test_DurchschnittsGewichtLOOP()
test_Corgikategorisierung()
test_DicksterCorgi()