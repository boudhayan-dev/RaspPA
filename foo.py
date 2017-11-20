# Include the Dropbox SDK
import dropbox,os,shutil,time
from audioSplitter import audio_convert
from sppech import speech_to_text
dbx=dropbox.Dropbox('YOUR_DROPBOX_APP_KEY')


while(1):
	dbx.users_get_current_account() # getcurrent account details.
	files=dbx.files_list_folder('').entries # find all files/subfolders inside the folder .
	files=[i.name for i in files if (i.name).endswith("mp3")==True] # filter the mp3 files.

	modified_status=False # Flag to check if files have changed since last time.
	new_files=[] #stores info about new files downloaded
	
	for i in files:
		with open("Records.txt","r+") as f:
			ExistingRecords=f.readlines()
			if not i+"\n" in ExistingRecords:
				dbx.files_download_to_file("C:\\Users\\Boudhayan Dev\\Desktop\\tes\\"+i,"/"+i,rev=None)
				f.write(i+"\n")
				new_files.append(i)
				modified_status=True

	if modified_status==True:

		for file in new_files:
			print("splitting -"+file)
			audio_convert(file)

			speech_to_text(file)
			#break
			print("deleting and recreating audio folder")
			shutil.rmtree("audio_split")
			os.remove(file)
			os.makedirs("audio_split")
			f = open(file[:-4]+"Results.txt","rb")
			dbx.files_upload(f.read(), "/"+file[:-4]+"Results.txt")

	#print("went online now")
	time.sleep(30*60)






		
