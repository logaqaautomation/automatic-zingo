from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from functools import wraps
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

# MongoDB Connection
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://your-username:your-password@your-cluster.mongodb.net/student_enrollment?retryWrites=true&w=majority')
client = MongoClient(MONGO_URI)
db = client['student_enrollment']
students_collection = db['students']

# Create unique index for email and user_id
students_collection.create_index("email", unique=True)
students_collection.create_index("user_id", unique=True)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validation
        if not all([email, first_name, last_name, user_id, password, confirm_password]):
            return render_template('signup.html', error='All fields are required')

        if password != confirm_password:
            return render_template('signup.html', error='Passwords do not match')

        if len(password) < 6:
            return render_template('signup.html', error='Password must be at least 6 characters')

        # Check if user already exists
        if students_collection.find_one({'$or': [{'email': email}, {'user_id': user_id}]}):
            return render_template('signup.html', error='Email or User ID already exists')

        # Hash password
        hashed_password = generate_password_hash(password)

        # Insert student
        student_data = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'user_id': user_id,
            'password': hashed_password,
            'has_logged_in_before': False
        }
        result = students_collection.insert_one(student_data)
        registration_id = str(result.inserted_id)

        session['user_id'] = user_id
        session['registration_id'] = registration_id
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['is_first_login'] = True

        return redirect(url_for('home'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')

        if not user_id or not password:
            return render_template('login.html', error='User ID and password are required')

        # Find student
        student = students_collection.find_one({'user_id': user_id})

        if student and check_password_hash(student['password'], password):
            session['user_id'] = user_id
            session['registration_id'] = str(student['_id'])
            session['first_name'] = student['first_name']
            session['last_name'] = student['last_name']
            
            # Check if this is first login
            is_first_login = not student.get('has_logged_in_before', False)
            session['is_first_login'] = is_first_login
            
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid User ID or password')

    return render_template('login.html')


@app.route('/home')
@login_required
def home():
    user_id = session.get('user_id')
    registration_id = session.get('registration_id')
    first_name = session.get('first_name')
    last_name = session.get('last_name')
    is_first_login = session.get('is_first_login', False)
    
    # Mark first login as done in database
    if is_first_login:
        students_collection.update_one(
            {'user_id': user_id},
            {'$set': {'has_logged_in_before': True}}
        )
        session['is_first_login'] = False

    return render_template('home.html',
                         user_id=user_id,
                         registration_id=registration_id,
                         first_name=first_name,
                         last_name=last_name,
                         is_first_login=is_first_login)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ========== AUTOMATION PRACTICE APPLICATION ==========

@app.route('/practice')
@login_required
def practice_step1():
    return render_template('practice/step1_personal_info.html')


@app.route('/practice/step1', methods=['POST'])
@login_required
def practice_step1_submit():
    session['practice_name'] = request.form.get('name')
    session['practice_address'] = request.form.get('address')
    session['practice_age'] = request.form.get('age')
    return redirect(url_for('practice_step2'))


@app.route('/practice/step2')
@login_required
def practice_step2():
    return render_template('practice/step2_lob.html')


@app.route('/practice/step2', methods=['POST'])
@login_required
def practice_step2_submit():
    session['practice_lob'] = request.form.get('lob')
    return redirect(url_for('practice_step3'))


@app.route('/practice/step3')
@login_required
def practice_step3():
    return render_template('practice/step3_coverage.html')


@app.route('/practice/step3', methods=['POST'])
@login_required
def practice_step3_submit():
    coverages = request.form.getlist('coverage')
    session['practice_coverages'] = ', '.join(coverages)
    return redirect(url_for('practice_step4'))


@app.route('/practice/step4')
@login_required
def practice_step4():
    # Calculate premium based on age and LOB
    age = int(session.get('practice_age', 30))
    lob = session.get('practice_lob', 'Auto')
    
    # Premium calculation logic
    base_premium = {'Auto': 1200, 'Home': 800, 'Health': 500, 'Life': 300}
    premium = base_premium.get(lob, 1000)
    
    # Age adjustment
    if age > 50:
        premium = premium * 1.25
    elif age < 25:
        premium = premium * 1.15
    
    session['practice_premium'] = round(premium, 2)
    
    return render_template('practice/step4_premium.html', 
                         premium=session['practice_premium'],
                         lob=lob)


@app.route('/practice/step5')
@login_required
def practice_step5():
    import datetime
    import random
    
    # Generate policy number
    policy_number = f"POL{datetime.datetime.now().strftime('%Y%m%d')}{random.randint(10000, 99999)}"
    session['practice_policy_number'] = policy_number
    
    return render_template('practice/step5_policy_issued.html',
                         name=session.get('practice_name'),
                         address=session.get('practice_address'),
                         age=session.get('practice_age'),
                         lob=session.get('practice_lob'),
                         coverages=session.get('practice_coverages'),
                         premium=session.get('practice_premium'),
                         policy_number=policy_number)


@app.route('/practice/reset')
@login_required
def practice_reset():
    # Clear practice session data
    for key in list(session.keys()):
        if key.startswith('practice_'):
            session.pop(key)
    return redirect(url_for('home'))


if __name__ == '__main__':
    # Set debug mode based on environment
    is_production = os.environ.get('ENVIRONMENT', 'development') == 'production'
    
    print("=" * 60)
    print("Flask Student Enrollment App")
    print("=" * 60)
    print("✓ MongoDB connected to: cluster0.ler3cub.mongodb.net")
    print("✓ Starting Flask server...")
    
    if is_production:
        print("→ Production Mode - Use Gunicorn")
    else:
        print("→ Visit: http://localhost:3000")
    
    print("=" * 60)
    app.run(debug=not is_production, host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
