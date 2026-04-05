import json
# before running script first keep the scrapped channels json file in same directory as "channels.json" file
try:
	fchnls=open("channels.json", "r")
	fm3u=open("akashvani.m3u", "w")
	fm3u.write("#EXTM3U\n\n")
	print("written")
	name=""
	for line in fchnls.readlines():
		if line.find(":")==-1:
			continue
		all=line.split(": ")
		left=all[0].strip(" ")
		right=all[1]
		if left.find("'")>=0:
			id=int(left.strip("'"))
			fm3u.write(f'\n#EXTINF:-1 tvg-id="{id}" ')
		else:
			if left.find("name")>=0:
				name=right.split("'")[1]
			if left.find("image")>=0:
				logo=right.split("'")[1]
				fm3u.write(f'tvg-logo="{logo}" ')
			if left.find("live_url")>=0:
				url=right.split("'")[1]
				fm3u.write(f'tvg-group="Akashvani radios",{name}\n{url}\n')
except:
	print("Problem in parsing to m3u")
finally:
	fchnls.close()
	fm3u.flush()
	fm3u.close()