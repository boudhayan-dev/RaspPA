import speech_recognition as sr , os,time

def speech_to_text(file_name):

	r = sr.Recognizer()
	list_audio= os.listdir("C:\\Users\\Boudhayan Dev\\Desktop\\tes\\audio_split")
	list_audio=[x[0:len(x)-4] for x in list_audio ]
	list_audio.sort(key=int)

	for audio in list_audio:
		audio_path=os.path.join(os.getcwd()+"\\audio_split\\"+audio+".wav")
		print(audio_path)

		AUDIO_FILE = (audio_path)
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)  
	 
		try:
			print("Transcribing file -" + AUDIO_FILE)
			line_counter=1
			text=r.recognize_google(audio).split()
			with open(file_name[:-4]+"Results.txt","a+") as f:
				for words in text:
					if (line_counter%25)==0:
						f.write(words)
						f.write("\n")
						line_counter+=1
						continue
					f.write(words)
					f.write(" ")
					line_counter+=1
	 
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
	 
		except sr.RequestError as e:
			print("Could not request results from Google Speech  Recognition service; {0}".format(e))
		time.sleep(2)







