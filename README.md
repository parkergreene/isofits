# ISOFITS

This package contains functions for calculating hole/shaft tolerances and fits per ISO 286

# Installation
`isofits` is available on [PYPI](https://pypi.org/project/isofits/).  Install with `pip`:
```
pip install isofits
```

# Usage

Import the package:
```
from isofits import *
```

# Documentation

See below for a list of function and their usages

## isotol 
```
upper_tolerance = isotol('hole', '10', 'H7', 'upper') #returns upper tolerance in microns

lower_tolerance = isotol('hole', '10', 'H7', 'lower') #returns lower tolerance in microns

upper_tolerance, lower_tolerance = isotol('hole', '10', 'H7', 'both') #returns both tolerances in microns

```

## isofit
```
mmc, lmc = isofit(10, 'H7', 'h6') #returns mmc and lmc of hole/shaft fit
```

## isoreport
```
isoreport(10, 'H7', 'h6') #returns printed report of mmc and lmc of hole/shaft fit
```