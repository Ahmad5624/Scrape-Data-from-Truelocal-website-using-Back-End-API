import csv
import requests
# URL for the website
url = "https://api.truelocal.com.au/rest/listings"
#  Total States of Australia you can edit the states here:
States = ['nsw', 'sa', 'vic', 'tas', 'qld', 'act', 'wa', 'nt']

#  Regions of every state
# STATE 1: NSW REGIONS
nsw_regions = ['act-gungahlin',
               'act-inner-south',
               'act-woden-valley-and-weston-creek',
               'blue-mountains',
               'central-tablelands',
               'illawarra-region',
               'murray-region',
               'north-coast',
               'north-west',
               'riverina',
               'snowy-mountains',
               'south-coast',
               'tamworth-region',
               'wollongong',
               'qld-south',
               'qld-townsville-region',
               'sydney-bankstown-region',
               'sydney-city',
               'sydney-eastern-suburbs',
               'sydney-greater-metro',
               'sydney-hawkesbury-region',
               'sydney-hills-district',
               'sydney-inner-west',
               'sydney-liverpool-region']
# STATE 2: SA REGIONS
sa_regions = [
    'adelaide-city',
    'adelaide-east',
    'adelaide-greater-metro',
    'adelaide-north',
    'adelaide-south',
    'adelaide-west',
    'nt-south',
    'eyre',
    'glenelg',
    'kangaroo-island',
    'murray-lands',
    'northern',
    'outer-adelaide',
    'port-adelaide',
    'yorke-peninsula']
# STATE 3: VIC REGIONS
vic_regions = ['ballarat-region',
               'bellarine-region',
               'colac',
               'geelong-city',
               'geelong-outer',
               'melbourne-bayside',
               'melbourne-city',
               'melbourne-east',
               'melbourne-greater-metro',
               'melbourne-inner-east',
               'melbourne-mornington-peninsula',
               'melbourne-north',
               'melbourne-north-west',
               'melbourne-south-east',
               'melbourne-south-west',
               'melbourne-west',
               'nsw-murray-region',
               'geelong-region',
               'gippsland',
               'north',
               'north-east',
               'south-west',
               'yarra-valley']
# STATE 4: TAS REGIONS
tas_regions = [
    'hobart-central',
    'hobart-east',
    'hobart-greater-metro',
    'hobart-west',
    'east-coast',
    'north',
    'north-east',
    'west-coast']
# STATE 5: QLD REGIONS
qld_regions = ['brisbane-city',
               'brisbane-greater-metro',
               'brisbane-north',
               'brisbane-south',
               'brisbane-south-east',
               'brisbane-west',
               'nsw-tamworth-region',
               'cairns-region',
               'central',
               'far-north',
               'gold-coast',
               'south',
               'sunshine-coast',
               'townsville-region']
# STATE 6: ACT REGIONS
act_regions = ['belconnen',
               'gungahlin',
               'kingston',
               'queanbeyan',
               'tuggeranong',
               'woden-valley-and-weston-creek',
               'canberra-city',
               'nsw-south-coast']
# STATE 7: WA REGIONS
wa_regions = ['perth-city',
              'perth-greater-metro',
              'armadale',
              'north',
              'south-coast']
# STATE 8: NT REGIONS
nt_regions = ['darwin-city',
              'north',
              'qld-central']

# CATEGORIES
categories = [
    'florists',
    'mobile-phones',
    'shopping-centres',
    'antiques',
    'arts-crafts',
    'art-supplies',
    'stationery',
    'fabric-stores',
    'frames',
    'book-shop',
    'comic-books',
    'newsagent',
    'movie-games-rental',
    'bridal',
    'computers',
    'cosmetics',
    'department-store',
    'pharmacy',
    'household-appliances',
    'home-entertainment',
    'eyewear',
    'clothing-retailers',
    'leather',
    'lingerie',
    'maternity',
    'shoes',
    'second-hand-clothes',
    'cards-gift-shop',
    'hobby-shops',
    'furniture',
    'hardware',
    'home-decor',
    'kitchen-bath',
    'nurseries-gardening',
    'jewellery-watches',
    'luggage',
    'musical-instruments',
    'office-equipment',
    'camera-stores',
    'bike',
    'outdoor-gear',
    'sports-goods',
    'tobacco-shops',
    'toys-computer-games',
    'photo',
    'wholesalers',
    'boat',
    'factory-outlets',
    'used-goods-retailers',
    'general-retailing',
    'promotional-products',
    'caravan',
    'music-video-dvd',
    'trailer-retailer',

]

# File Name
OUTPUT_FILE_NAME = 'Data.csv'
HEADER_FILE = ['Link Name', 'Name', 'Category', 'Address', 'State', 'Postcode', 'Phone Number', 'Website']


# 1. Main Function
def main_function():
    for state in States:
        # 1. NSW STATE
        if state == "nsw":
            for category in categories:
                for region in nsw_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 2. SA STATE
        if state == "sa":
            for category in categories:
                for region in sa_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 3. VIC STATE
        if state == "vic":
            for category in categories:
                for region in vic_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 4. TAS STATE
        if state == "tas":
            for category in categories:
                for region in tas_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 5. QLD STATE
        if state == "qld":
            for category in categories:
                for region in qld_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 6. ACT STATE
        if state == "act":
            for category in categories:
                for region in act_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 7. WA STATE
        if state == "wa":
            for category in categories:
                for region in wa_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()
        # 8. NT STATE
        if state == "nt":
            for category in categories:
                for region in nt_regions:
                    # Sending the requests
                    response = send_the_requests(category, state, region)
                    # FUNCTION FOR SCRAPING THE DATA
                    scrape_data(response, category)
        remove_the_duplication()


# 2. Sending the back-end requests
def send_the_requests(category, state, region):
    # Query for the back end API
    querystring = {"category": category, "inventory": "true", "limit": "10000", "offset": "0",
                   "showCopyPoints": "true",
                   "type": "browse", "state": state, "location": region, "region": region,
                   "passToken": "V0MxbDBlV2VNUw=="}
    payload = ""
    # Header
    headers = {
        "authority": "api.truelocal.com.au",
        "accept": "application/truelocal-2.0+json",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "_vwo_uuid_v2=DDA8B756FC88E9FA952B27CE8710FDFB8^|af054f446d4edd02d19380de3426361b; _vwo_uuid=DDA8B756FC88E9FA952B27CE8710FDFB8; _vwo_ds=3^%^3At_0^%^2Ca_0^%^3A0^%^241678424340^%^3A13.49852095^%^3A^%^3A^%^3A6_0^%^3A0; ab.storage.deviceId.a9882122-ac6c-486a-bc3b-fab39ef624c5=^%^7B^%^22g^%^22^%^3A^%^22b2e6d54e-d33d-6d94-fe6e-053fb755bd34^%^22^%^2C^%^22c^%^22^%^3A1679041238875^%^2C^%^22l^%^22^%^3A1679041238875^%^7D; _vis_opt_s=12^%^7C; _vis_opt_test_cookie=1; tl_trackingid=4F0AD5E01CCE87640379CAF6B7ECAC9A; AKA_A2=A; ak_bmsc=A2D0F3819AE5DA41F5250127A305D548~000000000000000000000000000000~YAAQBB0gF2EcFv+GAQAAs0bIBRPCrfgMgEPeLjlsz1GSypDWODhC9Ot5mqT0YMN1Hxyfl2Rk+jPKq2lA5z3OXfxyUugqD38mPkoXgwoGHwqEM58RjAMcklU9i3cFtP4FCEVCdDI0eIXONcNj/UyVh6sDZwdpBBbxcnbozadgDdjjDjYD2xv86swqbHBqTOtGB/pNw+6iI5b7od38jkkW6MSP/P7P2T/eNDpQaO0sC43wMRnn2TTjOoh0/Wj0FZ2WeRs5ug9TWL0W6qR1GIDPjK/jLfjm6bWrChq2RyBM6s8h+SpDGwZBGLu8MIIdTZ18erRzUQRMNs69w/RjR0QuBMh00jRQtSUzfcLyeOwJEAWwmPf4KO8OOXYpqyNAUr+MMWS93+1GAYtYgbgedwtlV+L7HwolVtUiQCTy2RUodOxxLhX70WblsU+GAggmxCFRUJODRWSyWZZyCtoH2GyTboKJ93Ryn6M94oQi6yZU5WzP8jKq3hDjBbZIhTYI9XOEGJA=; tl_trackingid_expires=1679436424149; _vwo_sn=1006798; bm_sv=CE36450AE216ED16E8F55D2F9AE4372D~YAAQBB0gF89sGv+GAQAAX9TtBRPvZ+VLzghDqk2HM+cLrR2KoYO+rQ4vgS4iMSPLkVu4eXrF2RHKlMlFEQuapBUZ6RuHIULIhNHAf7Z/mWRtVnnHzrIVRHdurkjTCtrqj2vK/22hOxod0S/Ote5P73EYCmbL/yGcT4W2CFaGQo0cGWI8mJrtHSBQRP1VLrMEvYSx7piBaxPSnoOQuj+py1mkq5vQaZ3K4rkjK/bPw4Ukamid1w1b5PVwPjkc4fCeUL/akMca9w==~1",
        "origin": "https://www.truelocal.com.au",
        "referer": "https://www.truelocal.com.au/",
        "sec-ch-ua": "^\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    # PRINT THE CATEGORY
    print("*****************************")
    print("Category Name:", category)
    print("State:", state)
    print("Region:", region)
    return response


# 3. Scrape the data
def scrape_data(response, category):
    data = response.json()
    # Firstly calculate the size of the list
    size_of_the_list = data['data']['size']

    print("Size of the list:", size_of_the_list)
    # if the size of the list is 0 then there will be no data exist.
    if size_of_the_list == 0:
        print(f"No data found")
    # Access the items list
    count = 1
    for i in range(size_of_the_list):
        address = 'Address Not found'
        state = 'State Not found'
        postCode = 'Post Code not found'
        website = 'Website not found'
        phone = 'Phone Number not found'
        # check for the limit of the list must be <= 10,000
        if count == 10001:
            print('limit reached')
            break
        # Extract data from json
        else:
            print(".....List No.:", count, "(", category, ").....")
            # 1. Link
            Link = data['data']['listing'][i]['seoUrl']
            Link = 'https://www.truelocal.com.au/business/' + Link
            # 2.  Name
            Name = data['data']['listing'][i]['name']
            # 3. Category
            try:
                Category = data['data']['listing'][i]['categories']['category'][0]['name']
            except:
                Category = 'Category Not Found'

            # 4. Address
            try:
                addressLine1 = data['data']['listing'][i]['addresses']['address'][0]['addressLine1']
                addressLine2 = data['data']['listing'][i]['addresses']['address'][0]['addressLine2']
                streetNumber = data['data']['listing'][i]['addresses']['address'][0]['streetNumber']
                streetName = data['data']['listing'][i]['addresses']['address'][0]['streetName']
                streetType = data['data']['listing'][i]['addresses']['address'][0]['streetType']
                suburb = data['data']['listing'][i]['addresses']['address'][0]['suburb']
                state = data['data']['listing'][i]['addresses']['address'][0]['state']
                postCode = data['data']['listing'][i]['addresses']['address'][0]['postCode']

                address_parts = [addressLine1, addressLine2, streetNumber, streetName, streetType, suburb]
                # Filter out any empty address parts
                address_parts = [part for part in address_parts if part]

                # Check if both streetType and suburb are present
                if streetType and suburb:
                    # Find the index of streetType in the address_parts list
                    street_type_index = address_parts.index(streetType)
                    # Insert a comma after streetType
                    address_parts[street_type_index] += ','
                # Check if addressLine1 is present
                if addressLine1:
                    addressLine1_index = address_parts.index(addressLine1)
                    # Insert a comma after streetType
                    address_parts[addressLine1_index] += ','
                # Join the address parts with a space
                address = ' '.join(address_parts)
            except:
                pass

            # 5. Phone Number and Website
            try:
                r = data['data']['listing'][i]['contacts']['contact']
                # Loop through each item in the JSON array
                # 1. Website
                for item in r:
                    if item['type'] == 'website':
                        website = item['value']
                        break
                # 2. Phone,mobile,national,fax
                for item in r:
                    if item['type'] == 'phone':
                        phone = item['value']
                        break
                    elif item['type'] == 'mobile':
                        phone = item['value']
                        break
                    elif item['type'] == 'national':
                        phone = item['value']
                        break
                    elif item['type'] == 'fax':
                        phone = item['value']
                        break
            except:
                pass

            print("Link:", Link)
            print("Name:", Name)
            print("Category:", Category)
            print("Address:", address)
            print("State:", state)
            print("Post Code:", postCode)
            print("Phone Number:", phone)
            print("Website:", website)

            #  Write data to file
            output_result = [Link] + [Name] + [Category] + [address] + [state] + [postCode] + [phone] + [website]
            write_to_file([output_result])
        count += 1


# 4. Write Data to the file
def write_to_file(rows):
    file = open(OUTPUT_FILE_NAME, 'a', encoding="utf-8-sig", newline="")
    writer = csv.writer(file)
    writer.writerows(rows)
    file.close()


# 5. Remove duplication from the file
def remove_the_duplication():
    # Read the CSV file and store its data in a list
    rows = []
    with open(OUTPUT_FILE_NAME, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    # Use set() to remove duplicates from the list
    non_duplicate_rows = list(set(tuple(row) for row in rows))

    # Write the non-duplicate data back to the CSV file
    with open(OUTPUT_FILE_NAME, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(non_duplicate_rows)


if __name__ == '__main__':
    write_to_file([HEADER_FILE])
    main_function()
