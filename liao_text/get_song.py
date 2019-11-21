import requests
url = 'http://isure.stream.qqmusic.qq.com/C400003QxEg83QZ9Mh.m4a?guid=4612303552&vkey=6FA8B367996380CC10E60EBB4C734546DC04AA25545D9AFC7EE78A29A9016B16BC3FB59585B3D572348512E2DCC74F31702D818F6B619099&uin=1276&fromtag=66'
response = requests.get(url)

with open('ch.mp3',mode = 'wb') as f :
		f.write(response.content)
