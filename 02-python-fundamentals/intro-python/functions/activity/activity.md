# Activity 2: Functions
The purpose of this activity is to use this [webscrapper script](webscrapper-open-data.py) to download the data from open data from [Portal de Datos Abiertos](https://datos.cdmx.gob.mx/dataset).

> HINT  
Do not forget to create a virtual environment.

## Part 1: Download files
Change the code to download the following files and save them in the same folder. If the file is in `ZIP` format, unzip it in a folder using Python.

### 1. Afluencia diaria de Metrobús CDMX
Webscrap the [Afluencia diaria de Metrobús CDMX](https://datos.cdmx.gob.mx/dataset/afluencia-diaria-de-metrobus-cdmx) website and download the following CSV files:
1. Afluencia Diaria del Metrobús (Simple)  
    Downloadable data set in CSV format.
2. Afluencia Diaria del Metrobús (Desglosada)  
    Downloadable data set in CSV format.  
3. Diccionario de Datos
    Downloadable data set in CSV format.  
4. Diccionario Afluencia Desglosada - MB  
    Downloadable data set in CSV format.

### 2. Catálogo inmuebles afectos al patrimonio cultural urbano
Webscrap the [Catálogo inmuebles afectos al patrimonio cultural urbano](https://datos.cdmx.gob.mx/dataset/inmuebles-catalogados) website and download the following CSV files:
1. Catálogo inmuebles afectos al patrimonio...  
    Downloadable data set in CSV format.
2. Inmuebles Catalogados  
    Geographical data set in ShP Downloadable format in ZIP.
3. Inmuebles Catalogados  
    Downloadable geographical data set in JSON.


## Part 2: Create functions
Once you have successfully downloaded the data, change the code to see what kind of behaviours you can reuse in the code, for example:
1. You can create a function to download a any kind of file.
    ```python
    ...
    def download_file(url: str, index: int) -> requests.models.Response:
        # YOUR CODE HERE
    ```
2. Create a function to extract the filename.
    ```python
    ...
    def extract_name(url: str) -> str:
        # YOUR CODE HERE
    ```

The goal is to reuse the code in loops for every file.

