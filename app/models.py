from app import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), index=True)
    last_name = db.Column(db.String(100), index=True)
    username = db.Column(db.String(100), index=True)
    password = db.Column(db.String(100), index=True)

    # Relation to the notes table
    note = db.relationship('Notes', backref="user", cascade="all, delete-orphan" , lazy='dynamic')
    def __repr__(self):
    	return 'User : %r' %(self.username)



	
class Notes(db.Model)	:
	id = db.Column(db.Integer, primary_key=True)
	note_body = db.Column(db.Text, nullable=False)
	note_date = db.Column(db.Date)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return "Note : %r" %(self.note_body)