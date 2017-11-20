
from pydub import AudioSegment
def audio_convert(file_name):
	sound = AudioSegment.from_mp3("C:\\Users\\Boudhayan Dev\\Desktop\\tes\\"+file_name)
	length=len(sound)

	remaining_length=20000
	if remaining_length>length:
		remaining_length=length

	initial=0
	final=remaining_length
	counter=0
	file_small=False
	while True:
		if remaining_length>length:
			if counter==0:
				file_small=True
			break
		try:
			sound_half=sound[initial:final]
		except:
			sound_half=sound[initial:length]

		initial=remaining_length
		remaining_length+=20000
		final=remaining_length

		sound_half.export("C:\\Users\\Boudhayan Dev\\Desktop\\tes\\audio_split\\"+str(counter)+".wav", format="wav")
		counter+=1

	if file_small==True:
		sound_half=sound[0:length]
		sound_half.export("C:\\Users\\Boudhayan Dev\\Desktop\\tes\\audio_split\\"+str(0)+".wav", format="wav")


