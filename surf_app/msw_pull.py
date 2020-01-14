import requests

key = "3d56b802f319631a4a55eea0b642fead"
spots = [382,2159]

# pull data from MSW
sitedata=requests.get("http://magicseaweed.com/api/" + key + "/forecast/?spot_id=" + str(spots[1]))

print(sitedata.status_code)
print(sitedata.json())


# save data somewhere

# outfile = open("data.txt", "a") # "a" flag will append lines

# outfile.write(sitedata.json())
# outfile.write("\n\n")

# outfile.close()
