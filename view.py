from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
import sys
sys.path.append('ui/')
from page import * 

#cookie
cookie = QNetworkCookieJar()
mgr = QNetworkAccessManager()
mgr.setCookieJar(cookie)

class View(QWidget,Ui_page):
	def __init__(self,parent,url):
		super(View,self).__init__()
		#to call tab window function
		self.parent = parent
		#number of tab of the current webview
		self.index = 0
		self.setupUi(self)
		#cookies
		page = self.qwebview.page()
		page.setNetworkAccessManager(mgr)
		print "cookie gestion enabled"
		#plugin
		QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
		#js
		QWebSettings.globalSettings().setAttribute(QWebSettings.JavascriptEnabled, True)
		#for icon connection
		QWebSettings.setIconDatabasePath('data/')
		QWebSettings.globalSettings().setLocalStoragePath('data/')
		if url=="":
			self.qwebview.setUrl(QUrl('http://start.ubuntu.com'))
		else:
			self.qwebview.setUrl(QUrl(url))

	def viewLoading(self,value):
		self.progressBar.setValue(value)
		if value==100:
			self.progressBar.setValue(0)
     
	def viewReload(self):
		self.qwebview.reload()
    
	def viewStop(self):
		self.qwebview.stop()
    
	def viewForward(self):
		self.qwebview.forward()
  
	def viewBack(self):
		self.qwebview.back()
    
	def viewHome(self):
		self.qwebview.setUrl(QUrl('http://start.ubuntu.com'))
    
	def viewTitle(self,title):
		self.parent.tabTitle(title,self.index)
    
	def viewIcon(self):
		self.parent.tabIcon(self.qwebview.icon(),self.index)
    
	def viewUrl(self,url):
		self.lineEdit.setText(url.toString())
   
	def viewGo(self):
		url = self.lineEdit.text()
		self.qwebview.setUrl(QUrl(url))