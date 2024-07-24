## project3

# Project purpose
The Vacation rental property finder/comparison tool aims to assist users in finding, comparing, and suggesting rental properties for their stays based on destination, price, ratings, and amenities. Whether planning a getaway or relocating, users can explore available properties, filter based on preferences, and visualize essential information.
With an emphasis on the data visualization track.

# Instructions on how to use and interact with the project -- Mark to add how to use the HTML FLask App

# At least one paragraph summarizing efforts for ethical considerations made in the project
In our project focused on vacation rental properties in Southwest Florida, we have made significant efforts to ensure ethical considerations are thoroughly addressed. We have prioritized data privacy by anonymizing any personal information collected during our data scraping process from platforms like Airbnb and VRBO. Also, we have followed the terms of service of these websites to avoid any unauthorized data extraction. Our data analysis and visualization practices are designed to be transparent and unbiased, ensuring that the insights generated are accurate and fair. We have also taken steps to ensure that our findings do not inadvertently harm property owners or renters by avoiding any misrepresentation of data. Overall, our commitment to ethical standards has been a guiding principle throughout the project, ensuring that our work is both responsible and respectful of all stakeholders involved.

Additionally, when we were looking at the data, we made sure that we didn't get any proprietary information and if we were we would need to take into consideration on what items we would need to show or state where we gathered the data from. Such as including an image of their logo in our presentation. We also wanted to look at certain dates to see what rental locations were available so we aren’t gathering data that wouldn’t be used in our project or for potential future works. Also, we narrowed down our location areas so we can get a more defined dataset for our needs and not slow down our systems by having large datasets.


# References for the data source(s):
Airbnb webpages
https://www.airbnb.com/s/Southwest-Florida-International-Airport-RSW--Terminal-Access-Road--Fort-Myers--FL--USA/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-08-01&monthly_length=3&monthly_end_date=2024-11-01&price_filter_input_type=0&channel=EXPLORE&query=Southwest%20Florida%20International%20Airport%20%28RSW%29%2C%20Fort%20Myers%2C%20FL&place_id=ChIJgQUlvz8T24gRRk4VTw6fGPw&location_bb=QdRQtcKjgZ1B1CH%2BwqODFw%3D%3D&date_picker_type=calendar&checkin=2024-11-01&checkout=2024-12-31&source=structured_search_input_header&search_type=autocomplete_click\"\n"

https://www.airbnb.com/rooms/1064874240378019486?search_mode=regular_search&check_in=2024-11-01&check_out=2024-12-31&source_impression_id=p3_1721599691_P3mGUVwtRLZ4WARJ&previous_page_section_name=1000&federated_search_id=b542efc9-8747-4545-82ef-8ba73c6c9204


VRBO webpages
url = "https://www.vrbo.com/search?adults=2&children=&regionId=6233839&destination=Southwest%20Florida%2C%20Florida%2C%20United%20States%20of%20America&latLong=26.682838%2C-81.795225&chkin=2024-12-01&chkout=2025-01-31&d1=2024-12-01&d2=2025-01-31&startDate=2024-12-01&endDate=2025-01-31&privacyTrackingState=CAN_TRACK&searchId=bae94e74-c608-4667-ad76-eb74864c5446&searchIdTest=test&sort=RECOMMENDED&useRewards=SHOP_WITH_POINTS&theme=&pwaDialog=&semdtl=&userIntent="

https://www.vrbo.com/3894161?chkin=2024-11-01&chkout=2024-12-31&d1=2024-11-01&d2=2024-12-31&startDate=2024-11-01&endDate=2024-12-31&x_pwa=1&rfrr=HSR&pwa_ts=1721373179972&referrerUrl=aHR0cHM6Ly93d3cudnJiby5jb20vSG90ZWwtU2VhcmNo&useRewards=true&adults=2&destination=43111+Greenway+Blvd%2C+Punta+Gorda%2C+FL+33982%2C+USA&destType=ADDRESS&latLong=26.7948913%2C-81.7353078&bedroom_count_gt=3&nearby_activities_group=golfing&pricing_group=nightly_price&privacyTrackingState=CAN_TRACK&property_type_group=apartment_or_condo&searchId=067bab4e-10fa-4324-826e-0da44123aaf3&us_bathroom_count_gt=2&sort=RECOMMENDED&top_dp=125&top_cur=USD&userIntent=&selectedRoomType=103028702&selectedRatePlan=0004ebad9607617a43148548e503d1e4d3ea&expediaPropertyId=103028702&propertyName=Luxe+3-Bed+Condo+in+Babcock+National+Golf+%26+Country+Club+with+Golf+Membership

#url = "https://www.vrbo.com/search?destination=43111%20Greenway%20Blvd%2C%20Punta%20Gorda%2C%20FL%2033982%2C%20USA&flexibility=0_DAY&d1=2024-11-01&startDate=2024-11-01&d2=2024-12-31&endDate=2024-12-31&adults=2&theme=&userIntent=&semdtl=&sort=RECOMMENDED"

#url = "https://www.vrbo.com/search?destination=Naples%2C%20Florida%2C%20United%20States%20of%20America&d1=2024-11-01&startDate=2025-01-31&d2=2024-12-31&endDate=2025-02-01&adults=2&theme=&userIntent=&semdtl=&latLong=26.141261%2C-81.794586&regionId=602724&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=false&amenities=&sort=RECOMMENDED"

#url = "https://www.vrbo.com/search?destination=Fort%20Myers%2C%20Florida%2C%20United%20States%20of%20America&d1=2024-11-01&startDate=2024-12-01&d2=2024-12-31&endDate=2025-01-31&adults=2&theme=&userIntent=&semdtl=&latLong=26.640629%2C-81.872307&regionId=602729&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=false&sort=RECOMMENDED&amenities="

#url = "https://www.vrbo.com/search?destination=Cape%20Coral%2C%20Florida%2C%20United%20States%20of%20America&d1=2024-11-01&startDate=2024-12-01&d2=2024-12-31&endDate=2025-01-31&adults=2&theme=&userIntent=&semdtl=&latLong=26.562853%2C-81.949532&regionId=6521&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=true&amenities=&sort=RECOMMENDED"    



# References for any code used that is not your own
Leveraged Xpert Learning Assistant, Google, ChatGPT, and Copilot as/where needed to develop/validate/troubleshoot code/data/functions. The Python and data science community for their invaluable resources.

