
# coding: utf-8

# In[1]:


import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText, ControlButton, ControlDir, ControlFile, ControlFilesTree, ControlImage, ControlBoundingSlider
from pyforms.controls import ControlButton, ControlCheckBox, ControlCheckBoxList, ControlPlayer, ControlSlider
from pyforms import controls 
import glob
import cv2
# from glob import *

# print(glob.glob("C:\Workspace\CorrNet\w50_cor.70\images\*.gif"))


# In[2]:


class VideoPlayer(BaseWidget):
    def __init__(self):
        super(VideoPlayer, self).__init__('Video Player')
        
        #Defnition of the form fields
        
#         self._dirname = ControlText('Directory', 'Default Value')
        self._button_play = ControlButton("Play")
        self._button_play.value = self.__play_all
        
        self._button_pause = ControlButton("Pause")
        self._button_pause.value = self.__pause_all
        
        self._button_refresh = ControlButton("Reload")
        self._button_refresh.value = self.__refresh_all
        
        self._button_print = ControlButton("Print")
        self._button_print.value = self.__print_value
#         self.formset = [{'Tab1':['_dirname'],},'_button']
        
#         self._directory = ControlDir('Choose a directory')
        self._file1 = ControlFile('File 1')
        self._file2 = ControlFile('File 2')
#         print(self._file.value)
        self._filetree = ControlFilesTree('Choose a file')


#         self._filetree.value = 'C:\\Users\\Ashwini Naik\\Videos\\Captures'
        
#         self._checkbox = ControlCheckBox('Choose a directory')
#         self._checkboxList = ControlCheckBoxList('Choose a file')
        self._player = ControlPlayer('Choose a file')
        self._player1 = ControlPlayer('Choose a file')
#         self._slider = ControlSlider('Slider')
    
        
        self._player.value = '_file.value'
#         self._player.refresh()
        self.formset = [ ('_button_play','_button_pause','_button_refresh') ,('_file1','_file2'),( '_player', '_player1')]
#         self._control.changed_event = self.__print_value
    

    
    def __print_value(self):
        print("Player 1" + self._player.value)
        print("Player 2" + self._player1.value)
        print("File 1" + self._file1.value)
        print("File 2" + self._file2.value)
        
    def __play_all(self):

        self._player.show()
        self._player.value = self._file1.value
        
        self._player1.show()
        self._player1.value = self._file2.value
        
        self._player.play()
        self._player1.play()
            
    def __pause_all(self):
        self._player.stop()
        self._player1.stop()
            
    def __refresh_all(self):
        self._player.value = self._file1.value
        self._player1.value = self._file2.value
            


#Execute the application

if __name__ == "__main__": pyforms.start_app(VideoPlayer)
    

    

