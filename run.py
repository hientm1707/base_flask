from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

#Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.ecommerce_bookstore.controllers import first_mod as first_mod


# Register blueprint(s)
app.register_blueprint(first_mod)

