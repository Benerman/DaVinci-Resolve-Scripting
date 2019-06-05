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
		return self.pm.GetCurrentProject()

	def set_project_name(self, project_name):
		return self.pm.CreateProject(project_name)

	def add_new_folder(self, folder_name):
		print('Added {} folder to rootFolder'.format(folder_name))
		return self.mp.AddSubFolder(folder, folder_name)

	def set_root_folder(self):
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
		# self.cfolder = self.mp.GetCurrentFolder()
		return self.cfolder.GetName()


	def add_sub_folder(self, folder_name='new folder', parent_folder=None):
		"""
		Add a subfolder to a created parent folder
		add_sub_folder(String of folder name, Pass a parent folder)
		"""
		self.folder = self.mp.GetRootFolder()
		self.cfolder = self.mp.GetCurrentFolder()
		print(self.get_folder_name())
		if parent_folder == None:
			return self.mp.AddSubFolder(self.cfolder, folder_name)
		self.reveal_in_storage(parent_folder)
		# setcurrentFolder = self.mp.SetCurrentFolder(parent_folder)
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




R = R()		

R.add_sub_folder("test1", 'Master')


# if __name__ == '__main__':

# 	# Instantiate Resolve objects
# 	resolve = DaVinciResolveScript.scriptapp('Resolve')
# 	fusion 	= DaVinciResolveScript.scriptapp('Fusion')
# 	pm      = resolve.GetProjectManager()
#	  ms		  = resolve.GetMediaStorage()
# 	proj    = pm.GetCurrentProject()
# 	mp      = proj.GetMediaPool()
# 	folder  = mp.GetRootFolder()
# 	cfolder = mp.GetCurrentFolder()
# 	clips   = folder.GetClips()

