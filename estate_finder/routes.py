from flask import render_template
from estate_finder import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/property-list')
def property_list():
    return render_template('property-list.html')


@app.route('/property-type')
def property_type():
    return render_template('property-type.html')


@app.route('/property-agent')
def property_agent():
    return render_template('property-agent.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')