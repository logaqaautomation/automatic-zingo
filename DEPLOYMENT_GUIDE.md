# Deployment Guide - Render.com

This guide will help you deploy your Loga QA Automation student enrollment application to Render.com.

## Prerequisites

- A GitHub account with your project repository
- A Render.com account (free tier available)
- MongoDB Atlas connection string (already set up)

## Step 1: Prepare Your Code for Deployment

### 1.1 Create a GitHub Repository

```bash
cd /Users/logan/Documents/workspace/automatic-zingo/automatic-zingo

# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Loga QA Automation app"

# Add GitHub remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/automatic-zingo.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 2: Deploy on Render.com

### 2.1 Create New Web Service on Render

1. Go to [https://render.com](https://render.com)
2. Sign up or log in
3. Click **"New +"** button → **"Web Service"**
4. Connect your GitHub account and select the `automatic-zingo` repository
5. Fill in the details:
   - **Name**: `loga-qa-automation`
   - **Region**: Choose closest to you (e.g., Oregon, Northern Virginia)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`

### 2.2 Set Environment Variables

In the Render dashboard, go to **Environment** section and add:

```
MONGO_URI=mongodb+srv://dbuser:test123@cluster0.ler3cub.mongodb.net/student_enrollment?retryWrites=true&w=majority&appName=Cluster0

SECRET_KEY=your-super-secure-random-key-here-change-this-in-production

ENVIRONMENT=production
```

**Important**: Generate a secure SECRET_KEY. Use this command:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 2.3 Deploy

1. Click **"Create Web Service"**
2. Render will automatically:
   - Build your application
   - Install dependencies from `requirements.txt`
   - Start your app with Gunicorn
   - Assign a public URL (e.g., `https://loga-qa-automation.onrender.com`)

## Step 3: Test Your Deployment

1. Wait for the build to complete (watch the logs)
2. Once deployed, your app will be available at the provided URL
3. Test the signup and login functionality
4. Verify MongoDB connection is working

## Step 4: Update DNS or Share Your Link

Your application is now live and accessible at:
```
https://loga-qa-automation.onrender.com
```

## Troubleshooting

### Issue: Deployment Failed

**Check the logs**:
1. Go to Render dashboard
2. Click on your service
3. Check **Logs** tab for error messages
4. Common issues:
   - Missing environment variables
   - MongoDB connection string incorrect
   - Python version mismatch

### Issue: Static Files Not Loading

Already handled! Flask will serve CSS files from the `static` folder automatically.

### Issue: Database Connection Error

- Verify `MONGO_URI` is correct in environment variables
- Ensure MongoDB Atlas IP whitelist includes `0.0.0.0/0` (or Render's IP)
- Check credentials in the connection string

### Issue: Slow First Load

- Render's free tier may have cold starts (5-10 seconds)
- Consider upgrading to paid plan for faster performance

## Performance Tips for Free Tier

1. **Cold Start**: First request after inactivity takes ~10 seconds
2. **Memory**: Limited to 512MB (sufficient for this app)
3. **Storage**: No persistent storage between deploys
4. **Concurrency**: Limited to 100 concurrent connections

For production use, consider **Render's Starter plan** or upgrade to:
- 1GB RAM
- 0.5 vCPU
- Faster performance
- Better uptime

## Monitoring & Maintenance

### Check App Status
- Go to Render dashboard
- Service shows green dot when running
- Check **Logs** tab for errors

### Update Your App
1. Make changes locally
2. Commit and push to GitHub
3. Render automatically deploys (if auto-deploy enabled)

### Restart Service
If needed, go to Management → Restart Service

## Updating Environment Variables

If you need to change `MONGO_URI` or `SECRET_KEY`:
1. Go to Render dashboard
2. Click on your service
3. Go to **Environment**
4. Update the variable
5. Service automatically restarts

## Cost Information

**Free Tier ($0/month)**:
- 750 hours/month (always available)
- Resources: 512MB RAM, 0.5 vCPU
- Cold starts (5-30 seconds)
- Database: Use MongoDB Atlas free tier

**Starter Tier ($7/month)**:
- 730 hours/month
- Resources: 1GB RAM, 0.5 vCPU
- Better performance
- Professional use recommended

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Deploy on Render
3. ✅ Add your domain (optional)
4. ✅ Set up auto-deploy from GitHub
5. ✅ Monitor application logs

## Support

- **Render Docs**: [https://render.com/docs](https://render.com/docs)
- **Flask Docs**: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- **MongoDB Atlas**: [https://www.mongodb.com/docs/atlas](https://www.mongodb.com/docs/atlas)

---

**Your app is now production-ready and deployable!** 🚀
