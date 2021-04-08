# AzurePriceApiClient
This is a python script that pulls pricing data from Azure and saves to a CSV file

This script makes use of the [Azure pricing API](https://docs.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices)

This script as written pulls VM pricing for the US West 2 region, ignoring Spot and Low Priority instance pricing. 

Data is output in CSV format which can be opened in Excel. An example of the output is included. 
