from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    hash_pass = db.Column(db.String(255) )

    pitches = db.relationship('Pitch',backref = 'users', lazy = 'dynamic')
   
    
    
    @property
    def password(self):
        raise AttributeError("You can not read password attribute")
    
    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def set_password(self, password):
        self.hash_pass = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)
    
    
    def __repr__(self):
        return f'User {self.username}'
    
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key = True)
    pitch_content = db.Column(db.String())
    pitch_category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    

        
    
    
    