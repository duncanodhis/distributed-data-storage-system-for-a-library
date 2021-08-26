from Pyro5.api import expose, behavior, serve, Daemon
from bisect import bisect_left 
@expose
@behavior(instance_mode="single")

class library(object):
	def __init__(self):
		self.user =[]
		self.author = []
		self.book = []
		self.book_loaned=[]

	def add_user(self,user_name):
		self.user.append(user_name)
		
	def return_users(self):
		return self.user
		
	def add_author(self,author_name,author_genre):
		self.author.append((author_name,author_genre))
	def return_authors(self):
		return self.author

	def add_book_copy(self, author_name, book_title):
		self.book.append((author_name,book_title))
		return self.book
	# self.books_not_onloan=[add_book_copy(author_name, book_title)]
	def return_books_not_loan(self):
		return self.book

	def loan_book(self, user_name, book_title, year, month, day):
		userslist =set((user_name, book_title))
		 # if userslist in book_loaned :
		if userslist in self.book_loaned :
			print("Element exist")
		else :

       		 self.book_loaned.append((user_name, book_title, year, month, day))


	def return_books_loan(self):
		
		return self.book_loaned

	def return_book(self, user_name, book_title, year, month, day):
		for list in self.book_loaned :
		    	if self.book in list :
		    		self.book_loaned.remove(list)
		    		self.book.append(list)

		return self.book
	def delete_book(self, book_title):
		if book_title in self.book :
			self.book.remove(book_title)
	def delete_user(self, user_name):
		self.user.remove(user_name)

	def user_loans_date(self, user_name, start_year, start_month, start_day, end_year,end_month, end_day):
		if user_name in self.book :
			d1 = datetime.datetime(start_year, start_month, start_day)
			d2 = datetime.datetime(end_year, end_month,end_day)
			for book_title in sefl.book :

				return self.books



daemon = Daemon()
serve({library: "example.library"}, daemon=daemon, use_ns=True)