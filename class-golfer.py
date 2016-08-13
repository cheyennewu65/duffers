class Golfer:
	def __init__(self,fname,mname,lname,pemail,semail):
		self.__name = list(fname,mname,lname)
		self.__email = list(pemail,semail)
		
	def get_name(self):
		return self.__name
		
	def get_email(self):
		return self.__email
		
	def set_name(self,fname,mname,lname)
		self.__fname = fname
		self.__mname = mname
		self.__lname = lname
		# call method to update name in database
		
	def set_email(self,pemail,semail)
		self.__pemail = pemail
		self.__semail = semail
		# call method to update email addresses in database
