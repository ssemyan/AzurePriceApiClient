import requests
import json
import urllib.parse
import csv

base_url = "https://prices.azure.com/api/retail/prices?$filter="

# Set the region
region = "westus2"

# Filter out the services you want / don't want (I ignore Low Priority and Spot pricing)
filter = f"serviceName eq 'Virtual Machines' and armRegionName eq '{region}' and endswith(meterName,'Spot') eq false and endswith(meterName,'Low Priority') eq false"
url = base_url + urllib.parse.quote(filter) 

# List to save prices to
prices = []

# Loop because API gives back prices in batches of 100
while (url):
    # make request and parse json
    print("Calling price API: " + url)
    r = requests.get(url)
    resp = json.loads(r.content)
    print("Found: " + str(len(resp["Items"])) + " items")

    # add to list
    prices.extend(resp["Items"])

    # Get the continuation URL
    url = resp["NextPageLink"]

# Write out to CSV
print("Total Prices: " + str(len(prices)))
filename = "prices_" + region + ".csv"
with open(filename, 'w') as csv_file:

    # hard-coded list of row labels
    fieldNameList = ["currencyCode","tierMinimumUnits","retailPrice","unitPrice","armRegionName","location","effectiveStartDate","meterId","meterName","productId","skuId","productName","skuName","serviceName","serviceId","serviceFamily","unitOfMeasure","type","isPrimaryMeterRegion","armSkuName","reservationTerm"]
    
    wr = csv.DictWriter(csv_file, fieldnames=fieldNameList)
    
    # write out row labels
    wr.writeheader()

    # write out rows
    for price in prices:
        wr.writerow(price)  