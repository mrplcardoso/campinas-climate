from ClimaticData import ClimaticData

climaticData = ClimaticData("Campinas Climatic History.csv")
climaticData.set_columns_names(['SRAD', 'TMAX', 'TMIN', 'RAIN'], ['Solar Radiation', 'Max Temperature', 'Min Temperature', 'Preciptation'])
print(climaticData.data.head())



