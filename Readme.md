# conversion-units
This package provide a unified collection of method to **convert values from one unit to another.** 
Yet i start with only 4 physical size namely <strong> distance, time, mass and temperature </strong>

## 1. Installation

Run the following code in a terminal to install the conversion package in you python environnement

```python
pip install conversion-units
```
or
```python
pip install conversion_units
```

## 2. Availables dimensions

At this point, the only dimension that have being implement in the package are : 
<ul>
    <li> Mass   </li>
    <li> Distance   </li>
    <li> Time   </li>
    <li> Temperature   </li>
</ul>

## 3. Import

You can make can a conversion by simply import a module name after the physical size you want to use. Every modules contain multiple method that can help you doing the conversion you need.
```python

from conversion_units import mass
from conversion_units import time
from conversion_units import distance
from conversion_units import temperature

```

## 4. Usage

a - <strong> Temperature conversion </strong>
```python

from conversion_units import temperature
print(temperature.kelvin_to_celcius( 0. ) )
print( temperature.kelvin_to_rankine(62))
```
b - <strong> distance conversion </strong>

```python

from conversion_units import distance
print(meter_to_kilometer(23000))

```
## 5. Author

<ul>
    <li> Full Name : <strong> Brice KENGNI ZANGUIM </strong>  </li>
    <li> Email : <strong> kenzabri2@yahoo.com </strong>   </li>
</ul>

## 6. Contributors


