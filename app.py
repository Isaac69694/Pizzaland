from flask import Flask,render_template,request,redirect,url_for,flash,session,abort
from flask_bootstrap import Bootstrap

app=Flask(__name__,template_folder='../vista',static_folder='../static')
Bootstrap(app)

@app.route("/")
def inicio():
    #return "Bienvenido a Pizzaland"
    return render_template('principal.html')


if __name__=='__main__':
    app.run(debug=True)



