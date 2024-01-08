#all sfx and bg music:
import winsound

def main_menu_background_music():
    file_path = "main_menu.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

def fan_sound():
    file_path = "fan_sfx.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def lights_sound():
    file_path = "lights_sfx.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def doors_sound():
    file_path = "doors_sfx.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def camera_sound():
    file_path = "camera_sfx.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def footsteps():
    file_path = r"C:\Users\acer\Desktop\Sherwin\FNAF_ Footsteps - Gaming Sound Effect (HD).mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

footsteps()

def animatronics_at_door():
   
    file_path = r"C:\Users\acer\Desktop\Sherwin\Fnaf 1 sound effect animatronic at door.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def jumpscare_sound():
    
    file_path = r"C:\Users\acer\Desktop\Sherwin\FNAF_ Jumpscare (FNAF 1) - Gaming Sound Effect (HD).mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def six_am_sound():
   
    file_path = r"C:\Users\acer\Desktop\Sherwin\FNAF_ 6 AM sound - Gaming Sound Effect (HD).mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def game_over_sound():
    
    file_path = r"C:\Users\acer\Desktop\Sherwin\FNAF 1 game over screen.mp3"
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
  
def load_sound_effects(self):
                self.help_sound = r""C:\Users\acer\Desktop\Sherwin\FNAF_ Buttons Won't Work - Gaming Sound Effect (HD).mp3""

def play_help_sound(self):
        winsound.PlaySound(self.help_sound, winsound.SND_FILENAME | winsound.SND_ASYNC)

 def show_instructions(self):
        instructions = (
          
        )

        messagebox.showinfo("Game Instructions", instructions)
        self.play_help_sound()
        self.main_menu()
#--------------------------------------------------------------------------------------------
#main_menu_bg
import winsound

def play_background_music(file_path, duration=10000):
    """
    Play background music using the winsound module.

    Parameters:
    - file_path (str): The path to the sound file (WAV format) for background music.
    - duration (int): The total duration to play the music in milliseconds. Default is 10 seconds.
    """
    
    repetitions = duration // winsound.PlaySound(file_path, winsound.SND_FILENAME)
    
    for _ in range(repetitions):
        winsound.PlaySound(file_path, winsound.SND_FILENAME)
    
    remaining_duration = duration % winsound.PlaySound(file_path, winsound.SND_FILENAME)
    if remaining_duration > 0:
        winsound.PlaySound(file_path, winsound.SND_FILENAME)

current_directory = os.path.dirname(os.path.realpath(__file__))

background_music_file_path = os.path.join(current_directory, 'main_menu.wav')


play_background_music(background_music_file_path)


#fan noises/sfx
import winsound
self.fan_sfx_file_path = "fan_sfx.wav"

    def play_fan_sfx(self, file_path, duration=10000):
        # Calculate the number of repetitions needed to cover the duration
        repetitions = duration // winsound.PlaySound(file_path, winsound.SND_FILENAME)

        # Play the sound in a loop
        for _ in range(repetitions):
            winsound.PlaySound(file_path, winsound.SND_FILENAME)

        # If there's any remaining time, play it
        remaining_duration = duration % winsound.PlaySound(file_path, winsound.SND_FILENAME)
        if remaining_duration > 0:
            winsound.PlaySound(file_path, winsound.SND_FILENAME)

    def run_game(self):
        self.play_background_music(self.background_music_file_path)

        # (code)

        # When game starts or resets cams, play fan sound
        self.play_fan_sfx(self.fan_sfx_file_path)

    def reset_cams(self):
        # (code for resetting cams)

        # Play fan sound when facing the office
        self.play_fan_sfx(self.fan_sfx_file_path)

#light noises
import winsound

        self.lights_sfx_file_path = "lights_sfx.wav"

    def play_lights_sfx(self, file_path):
        # Play the light sound effect
        winsound.PlaySound(file_path, winsound.SND_FILENAME)

    def turn_on_left_light(self):
        # (code for turning on the left light)
       self.play_lights_sfx(self.lights_sfx_file_path)

    def turn_on_right_light(self):
        # (code for turning on the right light)

        self.play_lights_sfx(self.lights_sfx_file_path)
      
#door_noise when opened/closed
import winsound
        self.doors_sfx_file_path = "doors_sfx.wav"

    def play_doors_sfx(self, file_path):
        # Play the doors sound effect
        winsound.PlaySound(file_path, winsound.SND_FILENAME)

    def close_left_door(self):
        #(code for closing the left door)

        self.play_doors_sfx(self.doors_sfx_file_path)

    def close_right_door(self):
        #(code for closing the right door)
      
        self.play_doors_sfx(self.doors_sfx_file_path)


#camera click noise
import winsound
        self.camera_sfx_file_path = "camera_sfx.wav"

    def play_camera_sfx(self, file_path):
     
        winsound.PlaySound(file_path, winsound.SND_FILENAME)

    def click_camera_button(self):
        self.play_camera_sfx(self.camera_sfx_file_path)
