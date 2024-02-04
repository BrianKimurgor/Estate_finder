# Start by importing necessary modules and creating the Flask app and SQLAlchemy instance
from estate_finder import app, db
from estate_finder.models import Location, PropertyType, Property

# Use the app's context to interact with the database
with app.app_context():
    # Create some instances of Location and PropertyType if not already present
    location1 = Location(name='City A')
    location2 = Location(name='City B')

    property_type1 = PropertyType(name='House')
    property_type2 = PropertyType(name='Apartment')

    # Add the instances to the session
    db.session.add_all([location1, location2, property_type1, property_type2])

    # Commit the changes to the database
    db.session.commit()

    # Create instances of Property and link them to Location and PropertyType
    property1 = Property(
        image_file='property1.jpg',
        property_type=property_type1,
        location=location1,
        status='For Sale',
        size_sqft=2000,
        bedrooms=3,
        bathrooms=2,
        price=500000.0
    )

    property2 = Property(
        image_file='property2.jpg',
        property_type=property_type2,
        location=location2,
        status='For Rent',
        size_sqft=1500,
        bedrooms=2,
        bathrooms=1,
        price=1200.0
    )

    # Add the instances to the session
    db.session.add_all([property1, property2])

    # Commit the changes to the database
    db.session.commit()

    print("Data added successfully.")
