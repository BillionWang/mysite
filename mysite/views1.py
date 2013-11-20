from django.shortcuts import render_to_response
import MySQLdb

def book_list(request):
	db =MYSQLdb.connect(usr='me',db='mydb',passwd='secret',host='localhost')
	cursor=db.cursur()
	cursor=execute('select name from books order by name')
	names=[row[0] for row in coursor.fetchall()]
	db.close()
	return render_to_response('book_list.html',{'names':names})
