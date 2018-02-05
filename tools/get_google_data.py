
import urllib
import json

# Assign keys - the following are for an example only
# Google custom search engine api key
api_key = "AIzaSyBjQwm5LJxN90ydAwEYIzZhC-1P5dHyIGA"

# Use google custom search engine to perform searches on items for our store
# get 20 results per item.

# The google custom search engine setup is where you specify which web sites
# to include in your search. For this app, the site is "amazon.com".

# WARNING - the google cse base version has limits on how many searches you
# can do. You will have to create a new instance of you reach your max.

# Search for pants, shirts, and shoes
urls = [
    #"https://www.googleapis.com/customsearch/v1?q=black+and+decker+steam_iron&key=" + api_key"
    "https://www.amazon.com/gp/product/B0006ZUHR0/ref=s9u_simh_gw_i1?ie=UTF8&fpl=fresh&pd_rd_i=B0006ZUHR0&pd_rd_r=f4542d3c-b69c-11e7-9821-4b13dd402765&pd_rd_w=j9YdE&pd_rd_wg=SNUkC&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=VDYW3BCPRSNGJ41HV2Y8&pf_rd_t=36701&pf_rd_p=1cf9d009-399c-49e1-901a-7b8786e59436&pf_rd_i=desktop"
]

# Convert results into json
jsonResps = []
for url in urls:
    print("Getting search results for: " + url)
    resp = urllib.urlopen(url).read()
    print(resp)
    type(resp)
    print("Converting to JSON")
    jsonResp = json.loads(resp)
    jsonResps.append(jsonResp)
    print("Done")
#print(jsonResps)
results = []
counter = 0

# Process each result
#for resp in jsonResps:
#    for item in resp.get('items', []):
#        link = item['link']
#        # Only process links to product web pages (not lists)
#        if '/dp/' in link:
#            print("Processing: " + link)
#            counter += 1
#            html = urllib.urlopen(link).read()
#            file_object = open(str(counter) + '.html', 'w')
#            # Store the page url at the bottom of the file
#            html = html + "<a href=" + link.encode('utf8') + ">"
#            file_object.write(html)
#            file_object.close()
