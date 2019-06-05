#!/usr/bin/env python

#Resolve Class Build
import sys
import DaVinciResolveScript


class R():

	resolve = DaVinciResolveScript.scriptapp('Resolve')
	fusion 	= DaVinciResolveScript.scriptapp('Fusion')
	pm      = resolve.GetProjectManager()
	ms		= resolve.GetMediaStorage()
	proj    = pm.GetCurrentProject()
	mp      = proj.GetMediaPool()
	timeln 	= proj.GetCurrentTimeline()
	folder  = mp.GetRootFolder()
	cfolder = mp.GetCurrentFolder()
	clips   = folder.GetClips()

	
	def __init__(self):
		pass

	def type_check(type_to_check):
		if type(type_to_check) == None:
			print("Error: Ensure Resolve is running while this script executes\nScript will close now")
			sys.exit()


	def get_current_project(self):
		print(self.proj.GetName())
		return self.proj.GetCurrentTimeline()


	def set_project_name(self, project_name):
		return self.pm.CreateProject(project_name)


	def get_root_folder(self):
		return self.mp.GetRootFolder()


	def get_current_folder(self):
		return self.mp.GetCurrentFolder()


	def set_current_folder(self, folder):
		"""returns Bool"""
		self.folder  = self.mp.GetRootFolder()
		self.cfolder = self.mp.GetCurrentFolder()
		if self.cfolder != self.folder:
			return self.mp.SetCurrentFolder(cfolder)
		return self.mp.SetCurrentFolder(folder)


	def get_sub_folders(self):
		self.folder = self.mp.GetRootFolder()
		return self.folder.GetSubFolders()


	def get_folder_name(self):
		print(self.cfolder.GetName())
		return self.cfolder.GetName()


	def add_new_folder(self, folder_name):
		"""
		add_new_folder('folder_name')

		### Adding Folders
		'Master' > 'Test1'
		R.add_new_folder("Test1") ## Always Adding 1 folder to Root level under 'Master'
		
		"""
		print('Added {} folder to rootFolder'.format(folder_name))
		return self.mp.AddSubFolder(self.folder, folder_name)


	def add_sub_folder(self, folder_name, parent_folder=None):
		"""
		Add a subfolder to a created parent folder
		add_sub_folder(String of folder name, Pass a parent Folder object(Optional))
		
		add_sub_folder("Test2") ## Adding 1 folder to most recent created folder or 'Master' if no folders exist
		.. > 'Test2' or 'Master' > 'Test2'

		### Adding Sub folder named 'test8' to parent folder 'test7' to parent folder 'Test2'
		'Master' > 'Test2' > 'test7' > 'test8'
		R.add_sub_folder("test8", R.add_sub_folder("test7", R.add_new_folder("Test2")))
		"""
		self.folder = self.mp.GetRootFolder()
		self.cfolder = self.mp.GetCurrentFolder()
		print(self.get_folder_name())
		if parent_folder == None:
			return self.mp.AddSubFolder(self.cfolder, folder_name)
		self.reveal_in_storage(parent_folder)
		setcurrentFolder = self.mp.SetCurrentFolder(parent_folder)
		if setcurrentFolder == 'None':
			print(setcurrentFolder)
			addFolder = self.mp.AddSubFolder(self.cfolder, parent_folder)
			return self.mp.AddSubFolder(addFolder, folder_name)
		else:
			print(setcurrentFolder)
			return self.mp.AddSubFolder(self.cfolder, folder_name)


	def media_sub_folders(self, folderPath):
		return self.ms.GetSubFolders(folderPath)


	def reveal_in_storage(self, path):
		return self.ms.RevealInStorage(path)


	def get_current_timeline(self):
		print(self.timeln.GetName())
		return self.proj.GetCurrentTimeline()


	def get_timeline_name(self):
		print(self.timeln.GetName())
		return self.timeln.GetName()


	def select_timeline(self, idx):
		print("There are {} timelines in this project.\nYou selected timeline number {}".format(int(self.proj.GetTimelineCount()),idx))
		return self.proj.SetCurrentTimeline(self.proj.GetTimelineByIndex(idx))


R = R()		#instantiate the Class

# list1 = R.get_sub_folders()
# print(list1)
# print(list1.values())
# print(R.get_folder_name())

# R.get_current_timeline()
# R.get_current_project()
# R.get_timeline_name()

# R.select_timeline(1)
# R.proj.GetTimelineByIndex(1)


# #Get Timeline Names and Objects  ----- Not Working
# timeline_count = int(R.proj.GetTimelineCount())
# timelinenames = []
# for i in range(timeline_count+1):
# 	R.proj.SetCurrentTimeline(i)
# 	R.get_timeline_name()
# 	R.proj.GetTimelineByIndex(i)
# 	print(R.proj.GetTimelineByIndex(i))

R.get_folder_name()
# R.get_root_folder()

### Adding Folders
# R.add_new_folder("Test1") ## Always Adding 1 folder to Root level under 'Master'
### 'Master' > 'Test1'



# if __name__ == '__main__':

# 	# Instantiate Resolve objects
# 	resolve = DaVinciResolveScript.scriptapp('Resolve')
# 	fusion 	= DaVinciResolveScript.scriptapp('Fusion')
# 	pm      = resolve.GetProjectManager()
#	ms		= resolve.GetMediaStorage()
# 	proj    = pm.GetCurrentProject()
# 	mp      = proj.GetMediaPool()
# 	folder  = mp.GetRootFolder()
# 	cfolder = mp.GetCurrentFolder()
# 	clips   = folder.GetClips()

