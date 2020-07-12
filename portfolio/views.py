from django.shortcuts import render

from .models import Projects,Portfolio,Blogs

def index(request):

    myself = '''My name is Sampath Gonnuru. I'm currently a Master's in Data Science from New Jersey Institute of Technology, Newark . I hail from a small town of Visakhapatnam, India. I started my coding journey in 2015 when I needed to build a website for my college's first of it's kind Fest. Later I iterated towards Android Application Development and worked for a startup. I was the only Android Development in the team which was challenging at times. Eventually, I took up the challenge and developed a fee payment application platform for parents and a monitoring system for school called FeEasy. It was during this development when I fell in love with all things AI and data. Since, the product also focused on building a prediction system which was to notify the bank if a particular student would be qualified for loan. Ever since then I live, love and breathe Data.'''

    # exp = Experience()
    # exp.name = 'MOVIE RECOMMENDER SYSTEM'
    # exp.desc = 'Makes a prediction of which Movie a user may like based on his activity on the system.'

    mrs = Projects()
    mrs.img = 'movies.png'
    mrs.name = 'MOVIE RECOMMENDER SYSTEM'
    mrs.desc = 'Makes a prediction of which Movie a user may like based on his activity on the system.'
    mrs.liveDemo = 'https://movierecommendersystem.herokuapp.com/'
    mrs.codeLink = 'https://github.com/gonnuru'

    # sf = Projects()
    # sf.img = 'mails.png'
    # sf.name = 'SPAM FILTER'
    # sf.desc = "A spam filter is a program that is used to detect unsolicited and unwanted email and prevent those messages from getting to a user's inbox."
    # sf.liveDemo = 'https://spam-check.herokuapp.com/'
    # sf.codeLink = 'https://github.com/gonnuru'

    hms = Projects()
    hms.img = 'hospitals.png'
    hms.name = 'House Price Prediction India'
    hms.desc = "An end to end model of Machine Learning for Real Estate Price Estimation. Deployed on Amazon Ec2 Instance"
    hms.liveDemo = 'http://ec2-35-168-1-72.compute-1.amazonaws.com/'
    hms.codeLink = 'https://github.com/Gonnuru/RealEstate_E2E_ML'

    dl = Projects()
    dl.img = 'dl.png'
    dl.name = 'IMAGE CLASSIFICATION USING RESNET50 AND RESNET152'
    dl.desc = "Classifying images of cars into various brands using FastAI library. classification done on Residual Networks 50 (ResNet50) and ResNet152."
    dl.liveDemo = ''
    dl.codeLink = 'https://github.com/Gonnuru/Image_Classification'

    covid = Projects()
    covid.img = 'covid.png'
    covid.name = 'COVID-19 Tracker'
    covid.desc = "I have created a dashboard with 6 visualizations to analyze and understand effects of Covid-19 in United States and Globally."
    covid.liveDemo = 'https://public.tableau.com/profile/sampath.gonnuru#!/vizhome/Covid-19_15891658031180/Covid-19dashboard?publish=yes'
    covid.codeLink = 'https://github.com/Gonnuru/COVID19_Tableau'

    ga = Projects()
    ga.img = 'education.png'
    ga.name = 'GRADUATE ADMISSION'
    ga.desc = "To estimate chances of graduate admission from an Indian perspective based on the features like GRE Scores, TOEFL Scores, UG CGPA, etc."
    ga.liveDemo = 'https://admission-prediction-app.herokuapp.com/'
    ga.codeLink = 'https://github.com/Gonnuru/Admission_Prediction'

    # bcp = Projects()
    # bcp.img = 'cancerx.png'
    # bcp.name = 'BREAST CANCER PREDICTION'
    # bcp.desc = "Predict whether the given patient is having Malignant or Benign tumor based on the attributes in the given dataset."
    # bcp.liveDemo = ''
    # bcp.codeLink = 'https://github.com/gonnuru'

    # ad = Projects()
    # ad.img = 'ad.png'
    # ad.name = "PREDICTION OF AD’S SUCCESS"
    # ad.desc = "A binary classification problem where the task is to predict whether an ad buy will lead to netgain."
    # ad.liveDemo = ''
    # ad.codeLink = 'https://github.com/gonnuru'

    # gsp = Projects()
    # gsp.img = 'graph.png'
    # gsp.name = "GOOGLE STOCK PRICE PREDICTION"
    # gsp.desc = "Predicting the open stock price of Google using a type of recurrent neural network known as Long Short-Term Memory (LSTM)."
    # gsp.liveDemo = ''
    # gsp.codeLink = 'https://github.com/gonnuru'

    # psc = Projects()
    # psc.img = 'security.png'
    # psc.name = "PASSWORD STRENGTH CLASSIFIER"
    # psc.desc = "The software that analyzes the strength of the password to facilitate organizations launch a multi-faceted defense against password breach."
    # psc.liveDemo = 'https://checkpasswordstrength.herokuapp.com/'
    # psc.codeLink = 'https://github.com/gonnuru'

    # food = Projects()
    # food.img = 'food.png'
    # food.name = "FOODIE"
    # food.desc = "A food delivery app developed using ReactJS that brings delicious food from your favourite local restaurant right to your door."
    # food.liveDemo = ''
    # food.codeLink = 'https://github.com/gonnuru'

    # phn = Projects()
    # phn.img = 'phone.png'
    # phn.name = "SIMPLE PHONE CALL APP"
    # phn.desc = "A mobile app that can make a phone call and send SMS. The app is developed using Android Studio. Speech Recognizer can also be used for converting speech to text in order to send long messages instead of typing."
    # phn.liveDemo = ''
    # phn.codeLink = 'https://github.com/gonnuru'

    css = Portfolio()
    css.img = "sslc.jpg"
    css.name = "CENTUM IN SCIENCE & SOCIAL SCIENCE"
    css.ctg = "Award"

    tip = Portfolio()
    tip.img = "tip.jpg"
    tip.name = "TENSORFLOW IN PRACTICE"
    tip.ctg = "Certification"

    lt = Portfolio()
    lt.img = "lt.jpg"
    lt.name = "LOONEY TUNES"
    lt.ctg = "Art"

    ml = Portfolio()
    ml.img = "ml.jpg"
    ml.name = "MACHINE LEARING"
    ml.ctg = "Certification"

    s2 = Portfolio()
    s2.img = "schl2.jpeg"
    s2.name = "SCHOOL SECOND (12TH GRADE)"
    s2.ctg = "Award"

    sql = Portfolio()
    sql.img = "sqlc.jpg"
    sql.name = "SQL FUNDAMENTALS"
    sql.ctg = "Certification"

    cpl = Portfolio()
    cpl.img = "couple.jpg"
    cpl.name = "COUPLE"
    cpl.ctg = "Art"

    md = Portfolio()
    md.img = "msv1.jpeg"
    md.name = "How to handle missing values with Python?"
    md.ctg = "Article"
    md.link = "https://medium.com/@gonnurus"

    time = Blogs()
    time.img = "time.jpg"

    time.name = "THE VALUE OF TIME"
    time.desc = "Imagine there is a bank that credits your account each morning with $86,400. It carries over no balance from day to day. Every evening deletes whatever......"
    time.link = "https://medium.com/@gonnurus"

    rel = Blogs()
    rel.img = "cpl.jpg"
    rel.name = "THE KEYS TO A SUCCESSFUL RELATIONSHIP"
    rel.desc = "Being in a loving long-term romantic relationship is one of the surest routes to long term happiness. But it ....."
    rel.link = "https://medium.com/@gonnurus"

    dtr = Blogs()
    dtr.img = "destiny1.jpg"
    dtr.name = "YOUR DETERMINATION DETERMINES YOUR DESTINY"
    dtr.desc = "What is your dream life? What kind of destiny you want to create for yourself? At one point, we have a clue what......"
    dtr.link = "https://medium.com/@gonnurus"

    gl = Blogs()
    gl.img = "goal.jpg"
    gl.name = "7 P'S OF GOAL SETTING"
    gl.desc = "When you are inspired by the generosity of philanthropists, you aspire to be one of them. However, you have to be rich. In order to be rich....."
    gl.link = "https://medium.com/@gonnurus"

    psy = Blogs()
    psy.img = "hope.jpg"
    psy.name = "THE PSYCHOLOGY OF HOPEFULNESS"
    psy.desc = "Hopefulness refers to an optimistic attitude and mindset that allows you to see the bright side of things and plan for a better future. This concept represents.... ."
    psy.link = "https://medium.com/@gonnurus"

    itm = Blogs()
    itm.img = "time.jpeg"
    itm.name = "IMPORTANCE OF TIME MANAGEMENT"
    itm.desc = "What is time management? It is a set of principles, practices, skills, tools and systems that help you use your time to accomplish what you want....."
    itm.link = "https://medium.com/@gonnurus"




    # experience = [exp]
    projects = [mrs,hms,dl,covid,ga]
    portfolio = [css,tip,lt,ml,s2,sql,cpl,md]
    blogs = [time,rel,dtr,psy,gl,itm]
    return render(request, 'index.html',{'myself':myself,'projects':projects,'portfolio':portfolio,'blogs':blogs})
