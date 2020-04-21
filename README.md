# india-district-locator
How to know the District Name, State name and other address info from lat-long geo coordinates.

This repo is a basic version where users can pass lat-long coordinates as arguments to the function and get district name and state name as result.

Currently, this works only for India and also Indian map data is not updated to it's latest. Hopefully I will be updating new geojson file as and when i get some bandwidth to work on this.

## Installation
Tested on Mac & Ubuntu. Should work on any -nix based operating systems.  
```
virtualenv -ppython3 gisenv
source gisenv/bin/activate

```

git clone https://github.com/satishvmadala/india-district-locator.git

cd india-district-locator

```
pip install -r requirements.txt

```
Dependencies are installed.

### How to run the file

* After activating the virtual environment:

** python index.py *longitude* *latitude*

## Example Input & Output

Input:
```
python index.py 80.5164523 16.5130887
```

Output:

{'State': 'Andhra Pradesh', 'District': 'Guntur'}
