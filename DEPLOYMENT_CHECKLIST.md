# Pre-Deployment Checklist

Use this checklist before deploying to Render.com

## Code & Configuration ✓

- [ ] All files committed to Git
- [ ] `.env.example` created with required variables
- [ ] `requirements.txt` updated with all dependencies
- [ ] `Procfile` created with startup command
- [ ] `render.yaml` configured (optional but recommended)
- [ ] `app.py` updated for production (debug mode handling)

## Environment Variables ✓

- [ ] `MONGO_URI` - MongoDB Atlas connection string verified
- [ ] `SECRET_KEY` - Secure key generated (NOT default value)
- [ ] `ENVIRONMENT` - Set to "production" for Render deployment

## Testing ✓

- [ ] App runs locally without errors
- [ ] Signup functionality works
- [ ] Login functionality works
- [ ] All 4 tabs load correctly (Overview, Courses, Testimony, Contact)
- [ ] MongoDB connection is working
- [ ] Static files load (CSS styling visible)

## Deployment Steps ✓

1. [ ] Create GitHub repository
2. [ ] Push code to GitHub main branch
3. [ ] Create Render account
4. [ ] Connect GitHub to Render
5. [ ] Create new Web Service on Render
6. [ ] Configure Build and Start commands
7. [ ] Set all environment variables
8. [ ] Deploy and monitor logs
9. [ ] Test the deployed application
10. [ ] Share the live URL with students

## Post-Deployment ✓

- [ ] App is accessible at public URL
- [ ] Signup and login work
- [ ] Database operations are functional
- [ ] No errors in Render logs
- [ ] Static files loading properly
- [ ] All tabs and links working

## Monitoring ✓

- [ ] Check Render dashboard daily
- [ ] Monitor MongoDB connection
- [ ] Keep environment variables secure
- [ ] Update SECRET_KEY if compromised
- [ ] Monitor for any deployment failures

---

**Ready to deploy?** Follow the steps in `DEPLOYMENT_GUIDE.md`
