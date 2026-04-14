# Exposure database

Exposure data for critical infrastructure (CI) assets is one of the first steps in conducting a Climate Risk Assessment. There are multiple ways to access information on critical infrastructure. For country-level assessments, government and public agencies generally publish datasets on roads, railways, and power networks. These datasets often provide high accuracy, comprehensive attributes, and consistent data. However, access to certain information or specific infrastructure assets may be limited.

Other sources of data come from international organizations and research institutes, which build on public data sources and combine them with additional inputs such as satellite imagery or models. These datasets enable broader coverage across regions, but they may have more limited attributes compared to government datasets and often require further processing.

Within MIRACA, the main goal is to provide a framework that supports the assessment of climate change impacts and adaptation measures in a consistent way at the Pan-European level. To achieve the same level of detail and granularity across countries, while ensuring completeness for all critical infrastructure assets, we have sourced critical infrastructure data from OpenStreetMap (OSM).

![Screenshot](figures/flowchart.png)

## OpenStreetMap (OSM)

OpenStreetMap is a globally collaborative geographic database that is free to access and that includes data about roads, buildings, addresses, shops and businesses, points of interest, railways, trails, transit, land use and natural features, and much more. You can explore OpenStreetMaps in the following link: [https://www.openstreetmap.org/](https://www.openstreetmap.org/)


## Accessing and downloading OSM data

[OSMnx](https://osmnx.readthedocs.io/en/stable/) is a Python package to allows to easily download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap (Boeing et a., 2025).


## References

- Boeing, G. (2025). Modeling and Analyzing Urban Networks and Amenities with OSMnx. Geographical Analysis, published online ahead of print. doi:10.1111/gean.70009
