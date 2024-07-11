# imports
import os
import requests
import bs4
from zipfile import ZipFile
import shutil

# download function

def download(url: str, fileName: str):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    length = response.headers.get('content-length')
    block_size = 1000000  # default value
    if length:
        length = int(length)
        block_size = max(4096, length // 20)
    #filesize = length*10**-6
    #filesize = round(filesize, 2)
    #print(f"{fileName} size: {filesize} MB")
    with open(fileName, 'wb') as f:
        size = 0
        for buffer in response.iter_content(block_size):
            if not buffer:
                break
            f.write(buffer)
            size += len(buffer)
            if length:
                percent = int((size / length) * 100)
                print(f"Downloading {fileName}: {percent}%", end='\r')
    print(f"\nDone Downloading {fileName}")

def unzip(file:str,dir=os.getcwd()):
    zip = ZipFile(file, 'r')
    zip.extractall(dir)

aroma = 'https://aroma.foryour.cafe/api/download/base'
tiramisu = 'https://github.com/wiiu-env/Tiramisu/releases/download/v0.1.4/environmentloader-ba9c126+wiiu-nanddumper-payload-5c5ec09+fw_img_loader-c2da326+payloadloaderinstaller-ec7176d+tiramisu-f1b479d.zip'
packages = 'https://aroma.foryour.cafe/api/download?packages=environmentloader,wiiu-nanddumper-payload,fw_img_loader,bloopair,wiiload,ftpiiu,sdcafiine,screenshotplugin,swipswapme'
appstore = 'https://wiiu.cdn.fortheusers.org/zips/appstore.zip'
baseappurl = 'https://wiiu.cdn.fortheusers.org/zips/'

prompt = input("Wii U SD Card Setup Tool\n\n1. Download Aroma CFW\n2. Download Tiramisu CFW\n3. Download Reccomended Homebrew\n4. Download vWii CFW\n5. Exit\n: ")

if prompt == "1":

	# make downloads directory
	if os.path.isdir("Downloads") != True:
		os.mkdir("Downloads")

	# Download files
	download(aroma, 'Downloads/aroma-base.zip')
	download(packages, 'Downloads/packages.zip')
	download(appstore, 'Downloads/appstore.zip')

	# make sd card directory
	if os.path.isdir('SD-Card') != True:
		os.mkdir("SD-Card")

	# unzip files
	unzip('Downloads/aroma-base.zip', 'SD-Card')
	unzip('Downloads/packages.zip','SD-Card')
	unzip('Downloads/appstore.zip','SD-Card')
	shutil.rmtree('Downloads')
	print("Done Downloading Aroma files, copy the files inside the folder SD-Card to the root of your SD Card. if it prompts to replace select merge.")

elif prompt == "2":

	# make downloads directory
	if os.path.isdir("Downloads") != True:
		os.mkdir("Downloads")

	# Download Files
	download(tiramisu, "Downloads/tiramisu.zip")
	download(appstore, "Downloads/appstore.zip")

	# make sd card directory
	if os.path.isdir('SD-Card') != True:
		os.mkdir("SD-Card")
	unzip('Downloads/tiramisu.zip','SD-Card')
	unzip('Downloads/appstore.zip','SD-Card')
	shutil.rmtree('Downloads')
	print('Done Downloading Tiramisu files, copy the files inside the folder SD-Card to the root of your SD Card. if it prompts to replace select merge.')

elif prompt == "3":

	# make downloads dir
	if os.path.isdir("Downloads") != True:
		os.mkdir("Downloads")
	
	download(f"{baseappurl}retroarch.zip", 'Downloads/retroarch.zip')
	download(f"{baseappurl}Wii-U-Time-Sync.zip", 'Downloads/time-sync.zip')
	download(f"{baseappurl}NUSspli-Lite.zip", 'Downloads/nusspli.zip')
	download(f"{baseappurl}Inkay.zip", 'Downloads/Inkay.zip')
	download(f"{baseappurl}dumpling.zip", 'Downloads/dumpling.zip')
	download(f"{baseappurl}SaveMiiModWUTPort.zip", 'Downloads/savemii.zip')
	download(f"{baseappurl}SwipSwapMe_WUPS.zip", 'Downloads/swipswapme.zip')
	download(f"{baseappurl}WiiU-Shell.zip", 'Downloads/wiiushell.zip')
	download(f"{baseappurl}Utag.zip", 'Downloads/utag.zip')
	download(f"{baseappurl}evWii.zip", 'Downloads/evwii.zip')
	download(f"{baseappurl}WiiUIdent.zip", 'Downloads/ident.zip')
	download(f"{baseappurl}wudd.zip", 'Downloads/wudd.zip')
	download(f"{baseappurl}wup_installer_gx2_wuhb.zip", 'Downloads/wup.zip')
	
	if os.path.isdir('SD-Card') != True:
		os.mkdir("SD-Card")
	
	unzip('Downloads/retroarch.zip', 'SD-Card')
	unzip('Downloads/time-sync.zip', 'SD-Card')
	unzip('Downloads/nusspli.zip', 'SD-Card')
	unzip('Downloads/Inkay.zip', 'SD-Card')
	unzip('Downloads/dumpling.zip', 'SD-Card')
	unzip('Downloads/savemii.zip', 'SD-Card')
	unzip('Downloads/swipswapme.zip', 'SD-Card')
	unzip('Downloads/wiiushell.zip', 'SD-Card')
	unzip('Downloads/utag.zip', 'SD-Card')
	unzip('Downloads/evwii.zip', 'SD-Card')
	unzip('Downloads/ident.zip', 'SD-Card')
	unzip('Downloads/wudd.zip', 'SD-Card')
	unzip('Downloads/wup.zip', 'SD-Card')
	shutil.rmtree("Downloads")
	print('Done Downloading Reccomended Homebrew files, copy the files inside the folder SD-Card to the root of your SD Card. if it prompts to replace select merge.')

elif prompt == "4":
	# make downloads dir
	if os.path.isdir("Downloads") != True:
		os.mkdir("Downloads")
	download('https://wiiu.cdn.fortheusers.org/zips/CompatTitleInstaller.zip', 'Downloads/compatinstaller.zip')
	download('https://wiiu.hacks.guide/docs/files/Patched_IOS80_Installer_for_vWii.zip','Downloads/ios80.zip')
	download('https://wiiu.hacks.guide/docs/files/d2x_cIOS_Installer.zip','Downloads/d2xciosinstaller.zip')
	print("go to this url to install d2x and setup vWii cfw: https://wiiu.hacks.guide/#/archive/vwii/sd-preparation")
	
	if os.path.isdir('SD-Card') != True:
		os.mkdir("SD-Card")
	unzip('Downloads/compatinstaller.zip', 'SD-Card')
	unzip('Downloads/ios80.zip', 'SD-Card')
	unzip('Downloads/d2xciosinstaller.zip', 'SD-Card/apps')
	shutil.rmtree("Downloads")
	print('Done Downloading Reccomended Homebrew files, copy the files inside the folder SD-Card to the root of your SD Card. if it prompts to replace select merge.')
elif prompt == "5":
	''
