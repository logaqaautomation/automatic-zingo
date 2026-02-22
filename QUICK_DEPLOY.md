# Quick Deploy to Render.com - 5 Minute Setup

## What You Need

✅ Application is ready for production deployment
✅ All configuration files created:
- `Procfile` - Tells Render how to run your app
- `render.yaml` - Render configuration
- `requirements.txt` - Updated with Gunicorn
- `DEPLOYMENT_GUIDE.md` - Complete deployment instructions
- `DEPLOYMENT_CHECKLIST.md` - Pre-deployment checklist

## Quick Steps

### Step 1: Push Code to GitHub (2 min)

```bash
cd /Users/logan/Documents/workspace/automatic-zingo/automatic-zingo

# Initialize git if not already done
git init
git add .
git commit -m "Deployment ready: Added Procfile, render.yaml, and gunicorn"

# Create a repository on GitHub first at github.com/new
# Then add remote and push
git remote add origin https://github.com/YOUR_USERNAME/automatic-zingo.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render (3 min)

1. Go to [https://render.com](https://render.com)
2. Sign up with GitHub
3. Click **Create** → **Web Service**
4. Select your `automatic-zingo` repository
5. Configure:
   - **Name**: `loga-qa-automation`
   - **Build**: `pip install -r requirements.txt`
   - **Start**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`

### Step 3: Set Environment Variables (1 min)

In Render dashboard, add these:

```
MONGO_URI=mongodb+srv://dbuser:test123@cluster0.ler3cub.mongodb.net/student_enrollment?retryWrites=true&w=majority&appName=Cluster0

SECRET_KEY=<generate-with-command-below>

ENVIRONMENT=production
```

**Generate Secure Secret Key:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

Then copy the output and paste in `SECRET_KEY` field.

### Step 4: Deploy!

Click **"Create Web Service"** and wait for deployment (2-3 minutes).

Your app will be live at: `https://loga-qa-automation.onrender.com`

## What Happens During Deployment

1. Render pulls your code from GitHub
2. Installs Python 3.11
3. Runs `pip install -r requirements.txt`
4. Starts your app with Gunicorn
5. Assigns a public URL

## Test Your Deployment

1. Visit `https://loga-qa-automation.onrender.com/login`
2. Create a test account
3. Verify all tabs work (Overview, Courses, Testimony, Contact)
4. Check YouTube link opens correctly

## Troubleshooting

**Build Failed?**
- Check Render logs for errors
- Verify all environment variables are set
- Ensure `Procfile` and `render.yaml` are correct

**App Not Loading?**
- Wait 30 seconds (free tier has cold start)
- Check MongoDB URI is correct
- Verify IP whitelist on MongoDB Atlas

**Need More Help?**
See `DEPLOYMENT_GUIDE.md` for detailed instructions

## Production Checklist Before Sharing

- [ ] Change `SECRET_KEY` to a new secure value
- [ ] Test signup and login
- [ ] Verify all pages load correctly
- [ ] Test on mobile device
- [ ] Check all links work
- [ ] Share the live URL with students!

---

**Congratulations! Your app is production-ready!** 🚀

For detailed information, see:
- `DEPLOYMENT_GUIDE.md` - Complete setup guide
- `DEPLOYMENT_CHECKLIST.md` - Pre-deployment checklist
