# SimsRadioDataTest
This repository hosts the JSON data sources for the [SimsRadio](https://github.com/simsradio/simsradio.github.io) website project.

## How it works 
1. A CSV file containing the Sims Radio Music data is pushed/uploaded onto the main branch of this repo.
2. Then Github actions will run the `csv_json_converter.py` script to generate JSON data file we need for the site. The JSON is then pushed to the `prod` branch of this repo where it can be consumed by the SimsRadio site.

## The JSON files
Currently we generate the main `simsRadioData.json` which is all the data used for the "Home" page of the site.
The playlist files `playlist.min.json` and `playlist.max.json` are used by the "Playlist" page of the site, as base data for users to view. These files are currently managed manually.
