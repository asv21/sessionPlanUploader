import sys
import warnings
import os
import logging


from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QObject,QThread,pyqtSignal,QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from pytesseract import image_to_string 
from PIL import Image
import pytesseract

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

import time

from pandas.core.dtypes.missing import isna
import pandas as pd

from PyQt5.QtWidgets import QSystemTrayIcon
from main_window import Ui_MainWindow
from sessionPlainUploaderHelpDiaglogUI import Ui_help

import os
import sys


# This webdriver can directly attach to an existing session.
class uploadBotWorker(QThread):
        progress = pyqtSignal(int)
        sessionNumber=pyqtSignal(int)
        finished = pyqtSignal()
        messagePasser=pyqtSignal(str)
        session_id= "none"
        url="none"
        def __init__(self, parent=None):
            super(uploadBotWorker, self).__init__(parent)
            self.username=None
            self.mypassword=None
            self.startingSessionNo=None
            self.sessionPlanFilePath=None
            self.academicYear=None
            self.semester=None
            self.Offeredto=None
            self.ltps=None
            self.courseCode=None

        def create_driver_session(self, session_id, executor_url):
            from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

            # Save the original function, so we can revert our patch
            org_command_execute = RemoteWebDriver.execute

            def new_command_execute(self, command, params=None):
                if command == "newSession":
                    # Mock the response
                    return {'success': 0, 'value': None, 'sessionId': session_id}
                else:
                    return org_command_execute(self, command, params)

            # Patch the function before creating the driver object
            RemoteWebDriver.execute = new_command_execute

            new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
            new_driver.session_id = session_id

            # Replace the patched function with original function
            RemoteWebDriver.execute = org_command_execute

            return new_driver

        def get_captcha_text(self,location,size):
            pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
            im = Image.open('screenshot.png') # uses PIL library to open image in memory

            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']


            im = im.crop((left, top, right, bottom)) # defines crop points
            im.save('screenshot.png')
            captcha_text = image_to_string(Image.open('screenshot.png')).lower()
            os.remove('screenshot.png')
            return captcha_text.strip()

        def readSessionPlan(self,sheet_index):     
            session_types=['lecture','tutorial','practical','skilling']
            session_type=session_types[int(sheet_index)] 
            sessionPlanPath=['/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[1]/div/div/div[2]/div/div/ul/li[2]/a',\
                '/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[1]/div/div/div[2]/div/div/ul/li[4]/a',\
                '/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[1]/div/div/div[2]/div/div/ul/li[3]/a',\
                '/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[1]/div/div/div[2]/div/div/ul/li[5]/a']
            addButtonPath=['/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[2]/div/div[1]/div[1]/a/span',\
                '/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[2]/div/div[3]/div[1]/a/span',\
                '/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[2]/div/div[2]/div[1]/a',\
                '/html/body/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div/div[2]/div/div[4]/div[1]/a'\
                ]
            teachingComponentPath=["Chalk","Talk","PPT"]
            evalComponentPath=["Semester in Exam-I",\
                               "ALM",\
                               "Lab Continuous Evaluation",\
                               "Lab Internal Test",\
                               "LAB PROJECT CONTINIOUS EVALUATION",\
                               "Attendance",\
                               "Home Assignment",\
                               "Tutorial",\
                               "SEM End Project",\
                               "Surpize Quiz",\
                               "Semester in Exam-II",\
                               "Lab Weekly exercise",\
                               "Mini /Capstone Project",\
                               "Surprise Quiz (min 2)",\
                               "Home Assignment and Textbook",\
                               "Lab In Semester Exam",\
                               "Exam – Viva",\
                               "Exam – Exercise",\
                               "Exam – Report",\
                               "External Review",\
                               "National Paper publication",\
                               "International Paper publication",\
                               "End Semester Exam",\
                               "Review for Project",\
                               "Report",\
                               "Presentation",\
                               "Exercise",\
                               "Questions &amp;Answers",\
                               "End Semester Exam (online MCQ)",\
                               "Continuous Evaluation - Lab Exercise",\
                               "Continuous Evaluation -Project",\
                               "Continuous(weekly)  - Test (40 MCQ)",\
                               "SemIn-Makeup Test 1",\
                               "SemIn-Makeup Test 2",\
                               "Lab End Semester Exam",\
                               "MOOCs Review",\
                               "Ratings on Global Platforms",\
                               "Skilling Continuous Evaluation",\
                               "Weekly Contest",\
                               "Hackathon",\
                               "Field-study Review",\
                               "Prototype Review",\
                               "Group Discussion",\
                               "Peer-Review",\
                               "MOOCs Certification",\
                               "Leaderboard ranking for Global Challenges",\
                               "Skill In-Sem Exam",\
                               "Industry-connect exam",\
                               "Industry certification",\
                               "Prototype Demonstration",\
                               "Paper Publication",\
                               "Global Certification",\
                               "Collaborator Certification",\
                               "Skill Sem-End Exam",\
                               "Poster Presentation",\
                               "Product/Prototype Demonstration",\
                               "Sem-in Exam (MOOCs)",\
                               "Review of Outcomes",\
                               "Active Participation",\
                               "Mock Test",\
                               "Seminar Review",\
                               "Quiz"]
            bltMap=["Select BTL",\
                    "Remembering ",\
                    "Understanding",\
                    "Applying",\
                    "Analyzing",\
                    "Evaluating",\
                    "Creating"
                    ]
                                       
            # self.leFilePath.setText("G:/My Drive/avinash.s.vaidya@klh.edu.in 2020-10-09 10 05/SEMI-2021-22/SKE3/19TS4003_session_plan.xlsx")    
            try:
                if self.sessionPlanFilePath:
                    filePath=str(self.sessionPlanFilePath).replace('\\','/')                    
                    sessionPlanData=pd.read_excel(filePath,sheet_name=session_type,header=None)
                    topicList=pd.read_excel(filePath,sheet_name=session_type+"-topics",header=None)
                else:
                    self.messagePasser.emit("Oops...!You forgot to select the file path")
                    logging.error("Oops...!You forgot to select the file path")
                    return                
            except Exception as e:
                self.messagePasser.emit(str(e))
                logging.error("Excel opening error: "+str(e))
            try:                
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,sessionPlanPath[sheet_index])))
                self.driver.find_element(By.XPATH,sessionPlanPath[sheet_index]).click() 
                time.sleep(2)                                                   
                currentRow=2
                                                   
                while currentRow<=sessionPlanData.last_valid_index():
                    self.driver.find_element(By.XPATH,addButtonPath[sheet_index]).click()
                    time.sleep(2)
                    self.sessionNumber.emit(int(str(sessionPlanData.loc[currentRow,1]).strip()))                    
                    if int(str(sessionPlanData.loc[currentRow,1]).strip())<=self.startingSessionNo:
                        while True:
                            if str(sessionPlanData.loc[currentRow,0]).lower() == "session number" :
                                logging.info("Session number: "+ str(sessionPlanData.loc[currentRow,1]).strip())
                                if int(str(sessionPlanData.loc[currentRow,1]).strip())==self.startingSessionNo:
                                    self.sessionNumber.emit(int(str(sessionPlanData.loc[currentRow,1]).strip()))                                    
                                    break                                                                                       
                            currentRow+=1                            
                            if currentRow>=sessionPlanData.last_valid_index():
                                self.messagePasser.emit("Oh no...!Could not find the requested session number!")
                                logging.error("Oh no...!Could not find the requested session number!")
                                return                                  
                    ## Session number
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="coursehandoutdeliveryplan-chdp_session_no"]/option[text()='+str(sessionPlanData.loc[currentRow,1])+']')))
                    self.driver.find_element(By.XPATH,'//*[@id="coursehandoutdeliveryplan-chdp_session_no"]/option[text()='+str(sessionPlanData.loc[currentRow,1])+']').click()                                      
                    #topics title                   
                    self.driver.find_element(By.XPATH,'//*[@id="coursehandoutdeliveryplan-chdp_topics"]').send_keys(str(topicList.loc[int(sessionPlanData.loc[currentRow,1]),3]).strip().replace('\n'," "))                    
                    #textbook
                    self.driver.find_element(By.XPATH,'//*[@id="coursehandoutdeliveryplan-chdp_book_chapter_page_no"]').send_keys(str(topicList.loc[int(sessionPlanData.loc[currentRow,1]),4]).strip().replace('\n'," "))                                        
                    #co
                    self.driver.find_element(By.XPATH,'//*[@id="cat-id1"]/option[text()="'+str(topicList.loc[int(sessionPlanData.loc[currentRow,1]),1]).strip()+'"]').click()
                    #coi
                    time.sleep(2)                        
                    self.driver.find_element(By.XPATH,'//*[@id="subcat-id1"]/option[text()="'+str(topicList.loc[int(sessionPlanData.loc[currentRow,1]),2]).strip()+'"]').click()
                    #teaching components                    
                    teachingComponents= str(topicList.loc[int(sessionPlanData.loc[currentRow,1]),5]).split(",")
                    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[8]/span/div/button/span').click()                    
                    for teachingComponent in teachingComponents:                                                                                     
                        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[8]/span/div/ul/li['+str(teachingComponentPath.index(str(teachingComponent).strip())+2)+']/a/label').click()                        
                    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[8]/span/div/button/span').click()                    
                    #evalcomponents                                         
                    evalComponents = str(topicList.loc[int(sessionPlanData.loc[currentRow,1]),6]).split(",")
                    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[9]/span/div/button/span').click()                    
                    for evalComponent in evalComponents:
                        # Select(self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[9]/span/div/button')).select_by_visible_text(evalComponent)                                
                        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[9]/span/div/ul/li['+str(evalComponentPath.index(str(evalComponent).strip())+2)+']/a/label').click()                        
                        time.sleep(1)                      
                    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/div[9]/span/div/button/span').click()
                    time.sleep(2)  
                    ##Outcomes                              
                    currentRow+=1                                                       
                    while pd.notna(sessionPlanData.loc[currentRow,1]):                           
                        outcomeNumber=sessionPlanData.loc[currentRow,1]
                        outcome=sessionPlanData.loc[currentRow,2]      
                        if outcomeNumber>1:
                            self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/i').click()
                            time.sleep(2)
                        self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionoutcomemappinginfo-'+str(int(outcomeNumber)-1)+'-csomi_course_outcome_number"]/option[text()="'+str(outcomeNumber).strip()+'"]').click()      
                        self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionoutcomemappinginfo-'+str(int(outcomeNumber)-1)+'-csomi_desc"]').send_keys(str(outcome).strip().replace('\n'," "))
                        currentRow+=1   
                        time.sleep(2)                         
                    currentRow+=1
                    ##session topics        
                    topicNumber=0 
                    while currentRow<=sessionPlanData.last_valid_index():
                        if(pd.notna(sessionPlanData.loc[currentRow,1])):
                            if topicNumber>0:
                                self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[8]/div/i').click()
                                time.sleep(2)
                            self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionplan-'+str(topicNumber)+'-chsp_session_minutes"]/option[text()="'+str(sessionPlanData.loc[currentRow,0]).strip()+'"]').click()                                                        
                            time.sleep(2)
                            self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionplan-'+str(topicNumber)+'-chsp_topics"]').send_keys(sessionPlanData.loc[currentRow,1].strip().replace('\n'," "))
                            time.sleep(2)
                            Select(self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionplan-'+str(topicNumber)+'-chpsi_btl_id"]')).select_by_index(int(str(sessionPlanData.loc[currentRow,2]).strip()))
                            time.sleep(2)                               
                            self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionplan-'+str(topicNumber)+'-chsp_teaching_learning_id"]/option[text()="'+str(sessionPlanData.loc[currentRow,3]).strip()+'"]').click()
                            time.sleep(2)
                            alm=str(sessionPlanData.loc[currentRow,4]).strip().replace('\n'," ")                            
                            alm='--- NOT APPLICABLE ---' if alm=='nan' else alm 
                            logging.info("ALM :" + alm)                                                               
                            self.driver.find_element(By.XPATH,'//*[@id="coursehandoutsessionplan-'+str(topicNumber)+'-chsp_delivery_alm"]/option[contains(text(),"'+alm+'")]').click()                        
                            topicNumber+=1
                            currentRow+=1
                            time.sleep(2)
                        else:
                            break
                    currentRow+=1  
                    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/form/div/div[2]/button').click()  
                    time.sleep(2)
                    progessPercentage=round((int(sessionPlanData.loc[currentRow,1])-1)/int(sessionPlanData.loc[1,1])*100)
                    self.progress.emit(progessPercentage)
                                   
                return
            except Exception as e:
                exc_type, exc_obj, exc_tb=sys.exc_info()
                logging.error(str(e)+":"+str(exc_tb.tb_lineno))  
                self.messagePasser.emit(str(e)+":"+str(exc_tb.tb_lineno))

        def run(self):
            try:                
                # determine if application is a script file or frozen exe                
                                                                
                try:
                    if self.session_id =="none" and self.url=="none":                                
                        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install())) 
                    else:
                        self.create_driver_session(self.session_id,self.url)
                except:
                    self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))                 

                self.driver.get("https://newerp.kluniversity.in")
                self.driver.maximize_window()
                self.session_id=self.driver.session_id
                self.url=self.driver.command_executor._url

                # assert "KL University ERP" in self.driver.title            
                time.sleep(2)
            except Exception as e:
                self.session_id="none"
                self.url="none"
                self.messagePasser.emit(str(e))
                logging.error(str(e))
            try:
                '''
                /html/body/div[1]/div[1]/div/div/div/a/span/i
                '''
                self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/a/span/i").click()            
                time.sleep(2)

                #captcha image xpath //*[@id="loginform-captcha-image"]

                element=self.driver.find_element(By.XPATH,"//*[@id='loginform-captcha-image']")
                location = element.location
                size = element.size
                self.driver.save_screenshot('screenshot.png')

                uname=self.driver.find_element(By.XPATH,"//*[@id='loginform-username']")
                uname.clear()
                uname.send_keys(Keys.HOME)
                uname.send_keys(self.username)


                pwrd=self.driver.find_element(By.XPATH,"//*[@id='loginform-password']")
                pwrd.clear()
                pwrd.send_keys(Keys.HOME)
                pwrd.send_keys(self.mypassword)

                captcha=self.driver.find_element(By.XPATH,'//*[@id="loginform-captcha"]')
                captcha.clear()
                captcha_text=self.get_captcha_text(location,size)
                captcha.send_keys(captcha_text)


                bt_login = self.driver.find_element_by_link_text("Login")
                WebDriverWait(self.driver, timeout=100, poll_frequency=1).until(EC.staleness_of(bt_login))
                logging.info("submitted and logged in")
            except Exception as e:
                logging.info("You are already logged in...")                
            
            try:
                time.sleep(2)                
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar11')))
                    logging.info("Page is ready")
                except TimeoutException:
                    logging.error("Loading error")      
                      
                # self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[1]/div/div/div/ul/li[5]/a').click()     #  My CC List       
                # time.sleep(2)
                self.driver.get("https://newerp.kluniversity.in/index.php?r=courses%2Fcourseprogramcoordinatormappingview%2Ftab_index_personal")
                time.sleep(2)
                self.driver.find_element(By.XPATH,'//*[@id="dynamicmodel-academicyear"]/option[text()="'+self.academicYear+'"]').click()
                self.driver.find_element(By.XPATH,'//*[@id="dynamicmodel-semesterid"]/option[text()="'+self.semester+'"]').click()
                self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div/div/form/div/div[3]/button[1]').click()
                time.sleep(2)
                try:
                    numberOfCourses_elem=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/div/b[2]')))
                    numberOfCourses=int(numberOfCourses_elem.text)
                except TimeoutException:
                    logging.error("Total number of courses not found")
                courseFound=0
                for i in range(numberOfCourses):
                    '''
                    //*[@id="w0"]/table/tbody/tr[1]/td[3]
                    '''
                    courseCode_text=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr['+str(i+1)+']/td[3]').text
                    Offeredto_text=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr['+str(i+1)+']/td[6]').text
                    logging.info("Course code: "+str(courseCode_text) +"  Offered To: "+ str(Offeredto_text))                    
                    if courseCode_text == self.courseCode and Offeredto_text==self.Offeredto:
                        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr['+str(i+1)+']/td[13]/a[2]').click()
                        courseFound=1
                        break
                if courseFound==0:
                    logging.error("no course found")
                    self.messagePasser.emit("Oh No...!Could not find the course")                    
                    return
                else:
                    logging.info("Course found. Continuing to uploading page..!")                                            
                
                # self.ltps=[0,0,0,4]                
                for index,value in enumerate(self.ltps):
                    if value!=0:
                        self.readSessionPlan(index)                                
                self.messagePasser.emit("End of File. Hope everything went well ;) If not, do not give up. Try and try till you succeed")
                logging.info("End of File. Hope everything went well ;) If not, do not give up. Try and try till you succeed")
                # self.driver.close()
                # self.session_id="none"
                # self.url="none"
            except Exception as e:
                self.messagePasser.emit(str(e))
                logging.error(str(e))
class uploadBot(QMainWindow, Ui_MainWindow):
        
        

        def showErrorMessage(self,msgToDisplay):
            msgBox=QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText(msgToDisplay)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
            msgBox.setEscapeButton(QMessageBox.StandardButton.Ok)
            msgBox.exec_()
            msgBox.setFocus()

        def reportProgress(self,n):
            self.progressBar.setValue(n)

        def updateSessionNo(self,n):
            self.leStartingSession.setText(str(n))    

        def startUpload(self):
            if self.leUserName.text() !="" and self.lePassword !="" and self.leFilePath.text() !="":
                self.worker.username=self.leUserName.text()
                self.worker.mypassword=self.lePassword.text()                              
                self.worker.academicYear=self.cbAcademicYear.currentText()
                self.worker.semester=self.cbSem.currentText()
                self.worker.sessionPlanFilePath=self.leFilePath.text()
                self.worker.courseCode=self.leCourseCode.text()
                if self.leStartingSession.text() !="":
                    self.worker.startingSessionNo=int(str(self.leStartingSession.text()).strip())
                else:
                    self.worker.startingSessionNo=1
                self.worker.Offeredto=str(self.leOfferedTo.text()).strip().upper() if self.leOfferedTo.text() !="" else "ECE"
                self.worker.ltps=[int(self.cbLectureHours.currentText()),int(self.cbTutHours.currentText()),int(self.cbPracticalHours.currentText()),int(self.cbSkillingHours.currentText())]
                if self.worker.ltps ==[0,0,0,0]:
                    self.showErrorMessage("oh...!Forgot LTPS structure? Please select LTPS structure")
                    logging.error("oh...!Forgot LTPS structure? Please select LTPS structure")
                    return
            else:
                self.showErrorMessage("AAh...!Forgot something? Enter all the details")
                logging.error("AAh...!Forgot something? Enter all the details")
                return  
            self.worker.start()    
      

        
        def browseForFilePath(self):
            filePath=QtWidgets.QFileDialog.getOpenFileName(self,"Select the session plan file","./",filter="Excel (*.xlsx *.xls)")
            logging.info("SessionPlan filepath:"+ str(filePath[0]))
            self.leFilePath.setText(filePath[0])
            

        def exitApp(self):
            sys.exit()
        
        def clearAll(self):
            self.leUserName.setText("")
            self.lePassword.setText("")
            self.leCourseCode.setText("")
            self.leFilePath.setText("")
            self.leStartingSession.setText("")
            self.cbLectureHours.setCurrentIndex(0)
            self.cbTutHours.setCurrentIndex(0)
            self.cbPracticalHours.setCurrentIndex(0)
            self.cbSkillingHours.setCurrentIndex(0)
        
        def openHelp(self):
            self.window=QtWidgets.QDialog()
            self.ui=Ui_help()
            self.ui.setupUi(self.window)
            self.window.show()

        def openSampleFile(self):
            try:
                os.startfile('sampleSessionPlan.xlsx')
            except Exception as e:
                self.showErrorMessage(e)

        def __init__(self,parent=None):
            super().__init__(parent)
            self.setupUi(self)
            self.pbRun.clicked.connect(self.startUpload)
            self.pbBrowse.clicked.connect(self.browseForFilePath)
            self.pbExit.clicked.connect(self.exitApp)  
            self.pbClear.clicked.connect(self.clearAll)
            self.actionSample_Session_Plan.triggered.connect(self.openSampleFile)
            self.actionInstructions.triggered.connect(self.openHelp)
            self.progressBar.setValue(0)
            self.worker=uploadBotWorker()                        
            self.worker.finished.connect(self.worker.quit)
            self.worker.finished.connect(self.worker.deleteLater)            
            self.worker.progress.connect(self.reportProgress)
            self.worker.messagePasser.connect(self.showErrorMessage)
            self.worker.sessionNumber.connect(self.updateSessionNo)

            logging.basicConfig(filename='appLog.log', format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.DEBUG , filemode='a') 
                 
                      

def main():
   app = QApplication(sys.argv)
   app.setApplicationName('KLH Course Handout Session Plan Uploader')   
   ex = uploadBot()
#    app_icon = QtGui.QIcon()
#    app_icon.addFile('icon_16x16.png', QtCore.QSize(16,16))
#    app_icon.addFile('icon_24x24.png', QtCore.QSize(24,24))
#    app_icon.addFile('icon_32x32.png', QtCore.QSize(32,32))
#    app_icon.addFile('icon_48x48.png', QtCore.QSize(48,48))
#    app_icon.addFile('icon_256x256.png', QtCore.QSize(256,256))
   ex.setWindowIcon(QIcon('logo_48x48.png'))
   ex.setIconSize(QSize(48,48))
   ex.setWindowTitle('KLH Course Handout Session Plan Uploader')   
#    trayIcon=QSystemTrayIcon('logo_48x48.png', parent=ex)
#    trayIcon.setToolTip('session plan uploader')
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
