import web

urls = (
    '/foo', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class Index(object):
    def GET(self):
	    return render.foo_form()
	
    def POST(self):
        form = web.input(
			firstname=None, lastname=None, gender=None, dob=None, telno=None, 
		    email=None, usname=None, psw=None, region=None, qty=None, 
		    aboutus=None, holla=None, myfile=None
		)
		        
        Firstname = form.firstname
        Lastname = form.lastname
        Gender = form.gender
        Dob = form.dob
        Telno = form.telno
        Email = form.email
        Usname = form.usname
        Psw = form.psw
        Region = form.region
        Qty = form.qty
        Aboutus = form.aboutus
        Holla = form.holla
        Myfile = form.myfile
		
        return render.foo(
		           Firstname, Lastname, Gender, Dob, 
				   Telno, Email, Usname, Psw, 
				   Region, Qty, Aboutus, Holla, Myfile
			    )
        			
			
if __name__ == "__main__":
	app.run()