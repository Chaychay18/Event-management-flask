from applications import app
from applications import db
from applications import bcrypt
from applications import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
     return member.query.get(int(user_id))



class member(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    mobile_number = db.Column(db.String(50), nullable=False, unique=True)
    email_address = db.Column(db.String(30), nullable=False, unique=True)
    address = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.String(length=60))
    bookings = db.relationship('Booking', backref='user', lazy=True)


    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    app.app_context().push()


      
    def __repr__(self):
         return f'<member   {self.email_address} {self.first_name} {self.mobile_number} {self.last_name} {self.address} {self.city}>'

    
 
    
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.String(20), nullable=False)
    payment_method = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)