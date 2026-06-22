import os

# Filter for just the years you need to save time, or keep all
YEARS = [str(i) for i in range(2010, 2021+1)] 
URLS = [
    f"https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_{year}.zip"
    for year in YEARS
]

if __name__ == "__main__":
    # Create the data directory if it doesn't exist
    if not os.path.exists('./data'):
        os.makedirs('./data')
    
    for year, url in zip(YEARS, URLS):
        print(f"--- Starting Download for Year {year} ---")
        
        # 1. Download using wget with the no-check flag
        # We use -P ./data to tell wget where to put it
        download_cmd = f"wget --no-check-certificate {url} -P ./data"
        os.system(download_cmd)
        
        print(f"--- Finished Download for {year}. Please unzip manually if extraction fails ---")

    print("Extraction Tip: Right-click the ZIPs in the /data folder and 'Extract All' to avoid Linux 'unzip' errors.")