# Geospatial-Data-ETL

Nairobi Roads Data Pipeline
This project demonstrates a data engineering pipeline with a GIS focus, extracting road data (primary, secondary, residential) from OpenStreetMap (OSM) for Nairobi County, transforming it into a structured format, and loading it into a PostgreSQL database. The pipeline leverages the Overpass API for data extraction, Python libraries (Pandas, GeoPandas, Shapely) for transformation, and SQLAlchemy for database loading. Key steps include querying OSM data using Overpass QL, converting road geometries to Well-Known Text (WKT) format, cleaning the dataset, and storing it in a PostgreSQL schema.

