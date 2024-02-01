from estate_finder import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"('{self.name}')"
    

class PropertyType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"('{self.name}')"

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_type_id = db.Column(db.Integer, db.ForeignKey('property_type.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    status = db.Column(db.String(12), nullable=False) # for sell or rent
    size_sqft = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_img = db.Column(db.String(255), nullable=False, default="default.jpg")
    property_type = db.relationship('PropertyType', backref=db.backref('properties', lazy=True))
    location = db.relationship('Location', backref=db.backref('properties', lazy=True))
    
    def __repr__(self):
        return (
            f"('{self.status}', "
            f"'{self.size_sqft}', "
            f"'{self.bedrooms}', "
            f"'{self.bathrooms}', "
            f"'{self.price}', "
            f"'{self.property_img}', "
            f"'{self.property_type}', "
            f"'{self.location}')"
        )

    
class PropertAgent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)
    # agent_img = db.Column(db.String(255), nullable=False, default="default.jpg")
    
    def __repr__(self):
        return f"('{self.name}', '{self.contact_info}')"
    
class Testimonials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), nullable=True)
    testimonial_text = db.Column(db.Text)
    # client_img = db.Column(db.String(255), nullable=False, default="default.jpg")
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    property = db.relationship('Property', backref=db.backref('testimonials', lazy=True))
    
    def __repr__(self):
        return f"('{self.client_name}', '{self.testimonial_text}', '{self.property}')" 