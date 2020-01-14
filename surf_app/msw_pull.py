import requests

key = "3d56b802f319631a4a55eea0b642fead"
sitedata=requests.get("http://magicseaweed.com/api/" + key + "/forecast/?spot_id=382")

print(sitedata)
print(key)

outfile = open("data.txt", "a") # "a" flag will append lines

outfile.write(sitedata)
outfile.write("\n")
outfile.write("\n")

outfile.close()
