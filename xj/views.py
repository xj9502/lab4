from django.shortcuts import *
from django.template import *
from django.shortcuts import *
from django import forms
from models import *
# Create your views here.
def index(request):
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    c = Context({'book_list':book_list,'author_list':author_list})
    return render_to_response("index.html", c)

def add_book(request):
    try:
        if request.POST:
            post = request.POST
            if(not Author.objects.filter(Name = post["author"])):
                return HttpResponse('''
                            <html>
    					<head><title>ERROR</title></head>
    					<body bgcolor = #c3ddd1>
    						<center>
    						<p><h1>作者不存在</h1></p>
                                      <p><a href="../add_author/">添加作者</a></p>
                                      <p><a href="../index/">返回首页</a></p>
    						</center>
    					</body>
    				</html>
    				'''
                )
            now_author = Author.objects.get(Name = post["author"])
            new_book = Book(
                Title = post["title"],
                ISBN = post["ISBN"],
                AuthorID = now_author,
                Publisher = post["publisher"],
    		PublishDate = post["publishdate"],
    		Price = post["price"],
            )           
            new_book.save()
        return render_to_response("add_book.html")
    except:
        return HttpResponse('''
            <html>
            <head><title>ERROR</title></head>
                <body  bgcolor = #c3ddd1>
          
                  <p><a href="../add_book">填写信息有误,点此返回重新填写</a></p>	
                
	          </body>
           </html>
           '''
        )
def add_author(request):  
    try:
        if request.POST:
            post = request.POST
            if(Author.objects.filter(AuthorID = post.get("authorID"))):
    		    	return HttpResponse('''
    		            <html>
    			            <head><title>ERROR</title></head>
    			            <body bgcolor = #c3ddd1>
    			                <center>
    			                <p><h1>作者已存在</h1></p><p><a href="../add_author/">点此返回</a></p>
    			                </center>
    			            </body>
    		            </html>
    			        '''
    	            )
            
            new_author = Author(
                AuthorID = post.get("authorID"),
                Name = post.get("name"),
                #Name = post["name"],
                Age = post["age"],
                Country = post["country"],
    		)           
            new_author.save()
        return render_to_response("add_author.html")
    except:
        return HttpResponse('''
            <html>
            <head><title>ERROR</title></head>
                <body  bgcolor = #c3ddd1>
          
                  <p><a href="../add_book">填写信息有误,点此返回重新填写</a></p>	
                
	          </body>
           </html>
           '''
        )       
def delete_book(request):
	dltid = request.GET["id"]
	Book.objects.filter(ISBN=dltid).delete()
	return HttpResponse('''
		<html>
			<head><title>删除书籍</title></head>
			<body bgcolor = #c3ddd1>
			<center>
			<p><h1>删除成功</h1></p><p><a href="../index/">点此返回</a></p>
			</center>
			</body>
		</html>
			'''
	)
 
def updata_book(request):
    book = Book.objects.get(ISBN=request.GET["id"])
    author_list = Author.objects.all()
    date = str(book.PublishDate)
    c = Context({"book": book,"author":author_list,"DATE":date})
    return render_to_response("updata_book.html", c)

def do_updata_book(request):
    if request.POST:
        post = request.POST
        if(not Author.objects.filter(Name = post["author"])):
            return HttpResponse('''
                        <html>
                        <head><title>ERROR</title></head>
					<body bgcolor = #c3ddd1>
						<center>
						<p><h1>作者不存在</h1></p>
                                  <p><a href="/add_author/">添加作者</a></p>
                                  <p><a href="/index/">返回首页</a></p>
						</center>
					</body>
				</html>
				'''
            )
        now_author = Author.objects.get(Name = post["author"])
        book = Book.objects.get(ISBN=post["ISBN"])
        book.Title = post["title"]
        book.AuthorID = now_author
        book.Publisher = post["publisher"]
        book.PublishDate = post["publishdate"]
			#PublishDate = "1999-9-19",
        book.Price = post["price"]
        book.save()
        return HttpResponse('''
            <html>
            <head><title>更新成功</title></head>
                <body bgcolor = #c3ddd1>
                    <center>
                         <p><h1>更新成功</h1></p><p><a href="../../index/">点此返回</a></p>
                    </center>
                </body>
            </html>
        '''
        )
def the_book(request):
    book = Book.objects.get(ISBN=request.GET["id"])
    author = book.AuthorID
    c = Context({"book": book,"author":author})
    return render_to_response("book.html", c)
def search(request):
    if request.POST:
        post = request.POST
        if(not  Author.objects.filter(Name = post["name"])):
            return HttpResponse('''
            <html>
            <head><title>更新成功</title></head>
                <body bgcolor = #c3ddd1>
                    <a href="../index/">此作者不存在,点此返回首页</a></font>
                </body>
            </html>
            '''
            )
        book_list = Book.objects.filter(AuthorID = Author.objects.get(Name = post["name"]))
        c = Context({'book_list':book_list})
        return render_to_response("search.html", c)
# modify 2
