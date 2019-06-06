#!/usr/bin/env python

#Resolve Class Build
import sys
import DaVinciResolveScript
import time

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

	def SwitchPage(self, page_number ):
		"""
		provide number 1-6 to switch pages in Resolve
		switch_page(2) = Edit Page
		1:"Media", 2:"Edit", 3:"Fusion", 4:"Color", 5:"Fairlight", 6:"Deliver"
		"""
		if type(page_number) != int:
			print('Error: Provide a number 1-6')
			return
		elif page_number > 6 or page_number < 1:
			print(f'Error: Page number {page_number} does not exist\nUse a number 1-6')
			return
		pages = {0:None, 1:"Media", 2:"Edit", 3:"Fusion", 4:"Color", 5:"Fairlight", 6:"Deliver"}
		self.resolve.OpenPage(pages[page_number])
		print(f'Page switched to {pages[page_number]}')
		return


	def GetCurrentProject(self):
		print(self.proj.GetName())
		return self.proj.GetCurrentTimeline()


	def SetProjectName(self, project_name):
		return self.pm.CreateProject(project_name)


	def GetRootFolder(self):
		return self.mp.GetRootFolder()


	def GetCurrentFolder(self):
		return self.mp.GetCurrentFolder()


	def SetCurrentFolder(self, folder):
		"""returns Bool"""
		# self.folder  = self.mp.GetRootFolder()
		# cfolder = self.mp.GetCurrentFolder()
		# if cfolder != folder:
		# 	return self.mp.SetCurrentFolder(cfolder)
		return self.mp.SetCurrentFolder(folder)


	def GetSubFolders(self):
		self.folder = self.mp.GetRootFolder()
		return self.folder.GetSubFolders()


	def GetFolderName(self):
		print(self.cfolder.GetName())
		return self.cfolder.GetName()


	def AddNewFolder(self, folder_name):
		"""
		add_new_folder('folder_name')

		### Adding Folders
		'Master' > 'Test1'
		R.add_new_folder("Test1") ## Always Adding 1 folder to Root level under 'Master'
		
		"""
		print('Added {} folder to rootFolder'.format(folder_name))
		return self.mp.AddSubFolder(self.folder, folder_name)


	def AddSubFolder(self, folder_name, parent_folder=None):
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
		self.RevealInStorage(parent_folder)
		setcurrentFolder = self.mp.SetCurrentFolder(parent_folder)
		if setcurrentFolder == 'None':
			print(setcurrentFolder)
			addFolder = self.mp.AddSubFolder(self.cfolder, parent_folder)
			return self.mp.AddSubFolder(addFolder, folder_name)
		else:
			print(setcurrentFolder)
			return self.mp.AddSubFolder(self.cfolder, folder_name)


	def GetMediaSubFolders(self, folderPath):
		return self.ms.GetSubFolders(folderPath)


	def RevealInStorage(self, path):
		return self.ms.RevealInStorage(path)


	def GetCurrentTimeline(self):
		print(self.timeln.GetName())
		return self.proj.GetCurrentTimeline()


	def GetTimeline_name(self):
		print(self.timeln.GetName())
		return self.timeln.GetName()


	def SelectTimeline(self, idx):
		print("There are {} timelines in this project.\nYou selected timeline number {}".format(int(self.proj.GetTimelineCount()),idx))
		return self.proj.SetCurrentTimeline(self.proj.GetTimelineByIndex(idx))

	# DR Included in script Functions
	def DisplayProjectsWithinFolder(self, pm, folderString = "- ", projectString = "  " ):
		folderString = "  " + folderString
		projectString = "  " + projectString
		
		projects = sorted(self.pm.GetProjectsInCurrentFolder().values())
		for projectName in projects:
			print(projectString + projectName)
		
		folders = sorted(self.pm.GetFoldersInCurrentFolder().values())
		for folderName in folders:
			print(folderString + folderName)
			if self.pm.OpenFolder(folderName):
				self.DisplayProjectsWithinFolder(self.pm, folderString, projectString)
				pm.GotoParentFolder()
		return

	def DisplayProjectTree(self, resolve ):
		self.pm.GotoRootFolder()
		print("- Root folder")
		self.DisplayProjectsWithinFolder(self.pm)
		return

	def DisplayTimelineTrack(self, timeln, trackType, displayShift ):
		trackCount = self.timeln.GetTrackCount(trackType)
		for index in range (1, int(trackCount) + 1):
			print(displayShift + "- " + trackType + " " + str(index))
			clips = timeln.GetItemsInTrack(trackType, index)
			for clipIndex in clips:
				print(displayShift + "    " + clips[clipIndex].GetName())
		return

	def DisplayTimelineInfo(self, timeline, displayShift ):
		print(displayShift + "- " + timeline.GetName())
		displayShift = "  " + displayShift
		self.DisplayTimelineTrack(timeline , "video", displayShift)
		self.DisplayTimelineTrack(timeline , "audio", displayShift)
		self.DisplayTimelineTrack(timeline , "subtitle", displayShift)
		return

	def DisplayTimelinesInfo(self, project ):
		print("- Timelines")
		timelineCount = self.proj.GetTimelineCount()
		
		for index in range (0, int(timelineCount)):
			self.DisplayTimelineInfo(self.project.GetTimelineByIndex(index + 1), "  ")
		return

	def DisplayFolderInfo(self, folder, displayShift ):
		print(displayShift + "- " + folder.GetName())
		clips = folder.GetClips()
		for clipIndex in clips:
			print(displayShift + "  " + clips[clipIndex].self.GetClipProperty("File Name")["File Name"])
		
		displayShift = "  " + displayShift
		
		folders = folder.GetSubFolders()
		for folderIndex in folders:
			self.DisplayFolderInfo(folders[folderIndex], displayShift)
		return

	def DisplayMediaPoolInfo(self, proj ):
		self.mp # = proj.GetMediaPool()
		print("- Media pool")
		self.DisplayFolderInfo(self.folder, "  ")
		return

	def DisplayProjectInfo(self, proj ):
		print("-----------")
		print("Project '" + self.proj.GetName() +"':")
		print("  Framerate " + self.proj.GetSetting("timelineFrameRate"))
		print("  Resolution " + self.proj.GetSetting("timelineResolutionWidth") + "x" + self.proj.GetSetting("timelineResolutionHeight"))
		
		self.DisplayTimelinesInfo(proj)
		print("")
		self.DisplayMediaPoolInfo(self.proj)
		return

	def AddTimelineToRender(self, proj, timeline, presetName, targetDirectory, renderFormat, renderCodec ):
		self.proj.SetCurrentTimeline(timeline)
		self.proj.LoadRenderPreset(presetName)
		
		if not self.proj.SetCurrentRenderFormatAndCodec(renderFormat, renderCodec):
			return False
		
		self.proj.SetRenderSettings({"SelectAllFrames" : 1, "TargetDir" : targetDirectory})
		return self.proj.AddRenderJob()

	def RenderAllTimelines(self, resolve, presetName, targetDirectory, renderFormat, renderCodec ):
		self.pm
		self.proj = pm.GetCurrentProject()
		if not project:
			return False
		
		resolve.OpenPage("Deliver")
		timelineCount = self.proj.GetTimelineCount()
		
		for index in range (0, int(timelineCount)):
			if not self.AddTimelineToRender(self.proj, self.proj.GetTimelineByIndex(index + 1), presetName, targetDirectory, renderFormat, renderCodec):
				return False
		return self.proj.StartRendering()

	def IsRenderingInProgress(self, resolve ):
		self.pm
		self.proj = self.pm.GetCurrentProject()
		if not self.proj:
			return False
			
		return self.proj.IsRenderingInProgress()

	def WaitForRenderingCompletion(self, resolve ):
		while self.IsRenderingInProgress(self.resolve):
			time.sleep(1)

		return

	def DeleteAllRenderJobs(self, resolve ):
		pm = self.resolve.GetProjectManager()
		proj = self.pm.GetCurrentProject()
		proj.DeleteAllRenderJobs()
		return


R = R()		#instantiate the Class

# R.WaitForRenderingCompletion(R.resolve)
# R.DeleteAllRenderJobs(R.resolve)
	
# R.DisplayProjectInfo(R.proj)
# R.DisplayProjectTree(R.resolve)

# R.SwitchPage(2)
# R.SelectTimeline(1)


print(R.GetCurrentFolder().GetName())
print(R.GetRootFolder().GetSubFolders()[1].GetName())
R.SetCurrentFolder(R.GetRootFolder())




# if R.get_sub_folders():
# 	print('True')
# 	R.get_current_folder()
# 	R.get_folder_name()
# else:
# 	print('False')
# R.get_root_folder()
# R.get_folder_name()

# R.set_current_folder(R.get_root_folder())
# R.get_folder_name()


# if R.GetRootFolder():
# 	print('True')
# else:
# 	print('False')

# if R.SetProjectName('Two'):
# 	print('True')
# else:
# 	print('False')




# list1 = R.GetSubFolders()
# print(list1)
# print(list1.values())
# print(R.GetFolderName())

# R.GetCurrentTimeline()
# R.GetCurrentProject()
# R.GetTimelineName()

# R.select_timeline(1)
# R.proj.GetTimelineByIndex(1)


# #Get Timeline Names and Objects  ----- Not Working
# timeline_count = int(R.proj.GetTimelineCount())
# timelinenames = []
# for i in range(timeline_count+1):
# 	R.proj.SetCurrentTimeline(i)
# 	R.GetTimelineName()
# 	R.proj.GetTimelineByIndex(i)
# 	print(R.proj.GetTimelineByIndex(i))

# R.GetFolderName()
# R.GetRootFolder()

### Adding Folders
# R.add_new_folder("Test1") ## Always Adding 1 folder to Root level under 'Master'
### 'Master' > 'Test1'



if __name__ == '__main__':

	# Instantiate Resolve objects
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

