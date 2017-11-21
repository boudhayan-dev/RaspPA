# Include the Dropbox SDK
import dropbox,os,shutil,time
from audioSplitter import audio_convert
from sppech import speech_to_text
dbx=dropbox.Dropbox('YOUR_DROPBOX_APP_KEY')


while(1):
        dbx.users_get_current_account()
        files=dbx.files_list_folder('').entries
        files=[i.name for i in files if (i.name).endswith("mp3")==True]
        modified_status=False
        new_files=[] #stores info about new files downloaded
        for i in files:
                print(i)
                with open("//home//pi//Desktop//RasPA//Records","r+") as f:
                        ExistingRecords=f.readlines()
                        if not i+"\n" in ExistingRecords:
                                dbx.files_download_to_file("//home//pi//Desktop//RasPA//"+i,"/"+i,rev=None)
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
                        f = open(file[:-4]+"Results","rb")
                        dbx.files_upload(f.read(), "/"+file[:-4]+"Results")
                        os.remove(file[:-4]+"Results")
        print("went online now")
        time.sleep(10)





		
