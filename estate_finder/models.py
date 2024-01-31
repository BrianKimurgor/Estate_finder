from estate_finder import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"('{self.id}', '{self.name}')"
    

class PropertyType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_type_id = db.Column(db.Integer, db.ForeignKey('property_type.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    status = db.Column(db.String(12), nullable=False) # for sell or rent
    size_sqft = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_type = db.relationship('PropertyType', backref=db.backref('properties', lazy=True))
    location = db.relationship('Location', backref=db.backref('properties', lazy=True))
    
    
class PropertAgent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)
    
    
class Testimonials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), nullable=True)
    testimonial_text = db.Column(db.Text)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    property = db.relationship('Property', backref=db.backref('testimonials', lazy=True))    