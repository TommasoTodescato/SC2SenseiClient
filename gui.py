import customtkinter as ct
from PIL import Image as img
from upload import auto_upload
from files import Data
from os import getcwd

class Client(ct.CTk):
	def __init__(self):
		super().__init__()

		file_path = f"{getcwd()}/playerinfo.dat"
		data = Data(file_path)
		data.settings["a"] = 100
		print(data.settings)

		ct.set_appearance_mode("dark")
		ct.set_default_color_theme("dark-blue")
		self.geometry("960x540")
		self.resizable(False, False)
		self.title("Sc2SenseiClient")
		self.iconbitmap(default="logo.ico")
		
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure((1,4), weight=10)
		self.grid_columnconfigure(1, weight=1)


		#	----	SIDEBAR		----	#
		self.sidebar = ct.CTkFrame(self, corner_radius=0)
		self.sidebar.grid(row=0, column=0, rowspan=5, sticky="nsew")
		self.sidebar.grid_rowconfigure(1, weight=1)
		self.sidebar.grid_rowconfigure((2,5), weight=2)

		self.logo = ct.CTkImage(img.open("logo.png"), size=(40, 40))
		self.main_title = ct.CTkLabel(self.sidebar, text=" Sc2Sensei", image=self.logo, compound="left",
				font=ct.CTkFont(size=22, weight="bold"))
		self.main_title.grid(row=0, column=0, padx=20, pady=35)

		self.home = ct.CTkImage(img.open("image.png"), size=(20,20))
		self.home_button = ct.CTkButton(self.sidebar, image=self.home, text="Home", fg_color="transparent", 
				command=self.get_input, hover=False)
		self.home_button.grid(row=1, column=0)
		
		self.inputb = ct.CTkButton(self, text="Open CTkInputDialog", command=self.get_input)
		self.inputb.grid(row=2, column=0, padx=20, pady=(10, 10))


		#	----	UPPERBAR	----	#
		self.upperbar = ct.CTkFrame(self, corner_radius=0, height=90)
		self.upperbar.grid(row=0, column=1, columnspan=5, sticky="nsew")
		self.upperbar.grid_rowconfigure(0, weight=1)
		self.upperbar.grid_columnconfigure(0, weight=1)

		self.welcome = ct.CTkLabel(self.upperbar, height=90, text="ciao")
		self.welcome.grid(row=0, column=0)

		#	----	REPLAYS FRAME	----	#
		#	Here will be displayed last 3 uploaded replays, which will
		#	be clickable and will take to the link of the analyzed replay
		
		self.replay_info = ct.CTkButton(self, text="replay")
		self.replay_info.grid(row=2, column=1)




	def get_input(self):
		dialog = ct.CTkInputDialog(text="Type in a number:", title="")
		dialog.overrideredirect(True)
		player_name = dialog.get_input()
		self.welcome.configure(text="Welcome, " + player_name)
		# Write player name in the file


	#	----	AUTOUPLOAD	----	#
	def main(self):
		# TEMP
		replays_path = "C:/Users/tomma/sc2-sensei/upload_client/ReplayTest"
		auto_upload(replays_path)
		self.after(5000, self.main)
