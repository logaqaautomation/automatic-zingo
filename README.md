# Student Enrollment Web Application

A Flask-based web application for student enrollment with authentication. Students can sign up with their email, name, user ID, and password, then log in to view their profile information.

## Features

- **Student Sign Up**: Register with email, first name, last name, user ID, and password
- **Student Login**: Secure login with user ID and password
- **Dashboard**: View personalized welcome message and registration details
- **MongoDB Integration**: Cloud database storage with MongoDB Atlas
- **Password Hashing**: Secure password storage using Werkzeug

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MongoDB Atlas (Free Cloud Database)
- **Frontend**: HTML, CSS, JavaScript
- **Hosting**: Ready for Vercel deployment

## Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (free tier available)
- pip (Python package manager)

## Setup Instructions

### 1. Create a MongoDB Atlas Account and Database

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up for a free account
3. Create a new cluster (M0 free tier)
4. Create a database user with username and password
5. Get your connection string (looks like: `mongodb+srv://username:password@cluster.mongodb.net/student_enrollment?retryWrites=true&w=majority`)

### 2. Clone and Setup the Project

```bash
# Navigate to the project directory
cd automatic-zingo

# Create a virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your MongoDB URI and secret key
# Replace <username>, <password>, and <cluster> with your MongoDB Atlas credentials
```

**Example .env file:**
```
MONGO_URI=mongodb+srv://studentuser:mypassword123@mycluster.mongodb.net/student_enrollment?retryWrites=true&w=majority
SECRET_KEY=your-super-secret-key-here
```

### 4. Run the Application

```bash
# Make sure virtual environment is activated
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
automatic-zingo/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── .env.example          # Environment variables template
├── .env                  # Environment variables (git ignored)
├── templates/
│   ├── base.html         # Base template
│   ├── signup.html       # Sign up page
│   ├── login.html        # Login page
│   └── home.html         # Dashboard page
└── static/
    └── css/
        └── style.css     # Styling
```

## Usage

### Sign Up
1. Go to `http://localhost:5000`
2. Click "Sign up here" link
3. Fill in all fields:
   - Email address
   - First name
   - Last name
   - User ID (unique identifier)
   - Password (minimum 6 characters)
   - Confirm password
4. Click "Sign Up"

### Login
1. Go to `http://localhost:5000/login`
2. Enter your User ID and Password
3. Click "Login"

### Dashboard
After login, you'll see:
- Welcome message with your name
- Your student name
- Your unique student registration ID
- Your user ID
- Logout button

## Deployment to Vercel

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. Set environment variables in Vercel dashboard:
   - Add your `MONGO_URI`
   - Add your `SECRET_KEY`

4. Add a `vercel.json` file to the project root:
   ```json
   {
     "buildCommand": "pip install -r requirements.txt",
     "env": {
       "PYTHON_VERSION": "3.11"
     }
   }
   ```

## Security Notes

- Change the `SECRET_KEY` in production
- Use strong passwords
- Keep your MongoDB credentials secure
- Use environment variables for sensitive data
- Never commit `.env` file to version control

## Troubleshooting

### MongoDB Connection Error
- Verify your MongoDB URI is correct
- Check that your MongoDB Atlas cluster is active
- Ensure your IP address is whitelisted in MongoDB Atlas (or allow all IPs: 0.0.0.0/0)

### Port Already in Use
```bash
# Run on a different port
python app.py --port 5001
```

### Virtual Environment Issues
```bash
# Delete and recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Future Enhancements

- Email verification
- Password reset functionality
- Student profile editing
- Course enrollment
- Grade tracking
- Email notifications

## License

This project is open source and available under the MIT License.
