#from/import flask is taken this downladed coding framework that will allow you to use multiple coding langauges and routes to get the website running. the render template piece will be further discussed in the css sheet. In short it has to do with rendering the specific templates of the dimensions of the particular css layout that is being used
from flask import Flask, render_template

#app is the actual site itself, we create this variable and set it equal to Flask(__name__) so that the site will be able to run on a particular host. The host is a custom direction that allows the site to be searched in a particular manner where it cna be launched.
app = Flask(__name__)

#in order to get the seperate pages to be classified and to be able to run, you need to use the @.route("/") feature. in this we are refering to "app" since we want the page to be directly corrolated to the running site we are using.
#the way you can create a page (or a branchout of the site) is by using ("/"). in order to make the html file recognized, you have to define a new function so that when you return the html you want, it has to be returned to this particular format so that the page will load in. this is why you create the "static" and "templates" folders, so that all this information will be stored across all possible pages that are created.  After you define your new function (I made them the same as the title of my html documents so that they could be easily recognizable and linear for the sake of the project), you have to retuern the rendered_template of the particular html doc you are trying to print onto the page. for example, the insta fucntion will return the insta.html file so that it will print that html when that particular page is loaded up. This porcess is used for all my links, even the first page that I have labeled as "index", inside the paretheses is just ("/" since this is the first page that will be loaded up when you access the site (the Home Page)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/instagram")
def insta():
    return render_template('insta.html')

@app.route("/youtube")
def yt():
    return render_template('yt.html')

@app.route("/xbox")
def xbox():
    return render_template('xbox.html')

@app.route("/twitch")
def twitch():
    return render_template('twitch.html')

# __name__ is being referenced again here to make the "__main__" true so that the site can run. __main__ is used to that the statement will alwways be true no matter whatb kinds of content you are trying to put on the site. the host 0.0.0.0 allows for any PC to be able to run this particular network to run when the code is running.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')