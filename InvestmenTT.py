import smtplib

from flask import Flask, render_template, request, session, redirect, jsonify
from DBConnection import Db

app = Flask(__name__)
app.secret_key="123"


@app.route('/')
def login():
    return render_template('login_index.html')


@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="SELECT * FROM login WHERE `user_name`='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['login_id']
        if res['type']=='admin':
            return redirect('/a_home')
        elif res['type']=='company':
            return redirect('/c_home')
        else :
            return '''<script>alert('invalid');window.location='/'</script>'''
    else :
        return '''<script>alert('invalid');window.location='/'</script>'''


@app.route('/logout')
def logout():
    session['lid']=''
    return redirect('/')


@app.route('/approve_company/<id>')
def approve_company(id):
    if session['lid'] != '':
        db=Db()
        qry="UPDATE `company`SET`status`='approved' WHERE `C_id`='"+id+"'"
        res=db.update(qry)
        return '''<script>alert('approved');window.location='/company_list'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/rejected_company/<id>')
def rejected_company(id):
    if session['lid'] != '':
        db=Db()
        qry="UPDATE `company`SET`status`='rejected' WHERE `C_id`='"+id+"'"
        res=db.update(qry)
        return '''<script>alert('rejected');window.location='/company_list'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/approved_list')
def approved_list():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM company WHERE STATUS='approved'"
        res = db.select(qry)
        return render_template("admin/APPROVED LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/rejected_list')
def rejected_list():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM company WHERE STATUS='rejected'"
        res=db.select(qry)
        return render_template("admin/REJECTED LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/change_password')
def change_password():
    if session['lid'] != '':
        return render_template("admin/change passsword.html")
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    if session['lid'] != '':
        CURRENTPASSWORD=request.form['textfield']
        NEWPASSWORD=request.form['textfield2']
        CONFIRMPASSWORD=request.form['textfield4']
        db=Db()
        qry="SELECT * FROM login WHERE `password`='"+CURRENTPASSWORD+"' AND `login_id`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        if NEWPASSWORD==CONFIRMPASSWORD :
            db=Db()
            qry="UPDATE login SET `password`='"+CONFIRMPASSWORD+"' WHERE `login_id`='"+str(session['lid'])+"'"
            res=db.update(qry)
            return '''<script>alert('Sucessfully changed');window.location='/'</script>'''
        else :
            return '''<script>alert('Invalid credentials');window.location='/change_password'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/company_list')
def company_list():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM company where status='pending'"
        res = db.select(qry)
        return render_template("admin/COMPANY LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/company_list_post',methods=['post'])
def company_list_post():
    if session['lid'] != '':
        search=request.form['textfield']
        db=Db()
        qry="SELECT * FROM company WHERE STATUS='pending' and `c_name` LIKE '%"+search+"%'"
        res=db.select(qry)
        return render_template("admin/COMPANY LIST.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/send_reply/<id>')
def complaint_reply(id):
    if session['lid'] != '':
        return render_template("admin/COMPLAINT  REPLY.html",id=id)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/complaint_reply_post',methods=['post'])
def complaint_reply_post():
    if session['lid'] != '':
        reply=request.form['textarea']
        id=request.form['complaint_id']
        db=Db()
        qry="UPDATE `complaint`SET `reply`='"+reply+"',`status`='replied' WHERE `complaint_id`='"+id+"'"
        res=db.update(qry)
        return '''<script>alert('sending');window.location='/complaints'</script>'''
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/complaints')
def complaints():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM `complaint`INNER JOIN `trader` ON `complaint`.`user_id`=`trader`.`l_id`"
        res=db.select(qry)
        return render_template("admin/COMPLAINTS.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/feedback')
def feedback():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM `feedback` INNER JOIN `trader`ON feedback.user_id=`trader`.`l_id` "
        res=db.select(qry)
        return render_template("admin/FEEDBACK.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/view_traders')
def view_traders():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM trader"
        res = db.select(qry)
        return render_template("admin/VIEW TRADER.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/view_complaints')
def view_complaints():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM `complaint` INNER JOIN `trader` ON `trader`.`user_id`=`complaint`.`user_id`  "
        res = db.select(qry)
        return render_template("admin/COMPLAINTS.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/view_complaints_post',methods=['post'])
def view_complaints_post():
    if session['lid'] != '':
        from_date=request.form['textfield']
        to=request.form['textfield2']
        db=Db()
        qry="SELECT * FROM `complaint` INNER JOIN `trader` ON `trader`.`user_id`=`complaint`.`user_id` WHERE `date` BETWEEN '"+from_date+"' AND '"+to+"'"
        res=db.select(qry)
        return render_template("admin/COMPLAINTS.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/a_home')
def a_home():
    if session['lid']!='':
        return render_template("admin/home_index.html")
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''



# ========================================== COMPANY=====================================================================#

@app.route('/signup_1')
def signup_1():
    return render_template("sindex.html")



@app.route('/signup_1_post',methods=['post'])
def signup_1_post():
    EMAIL= request.form['textfield']
    VERIFICATIONCODE = request.form['textfield2']
    CREATEPASSWORD = request.form['textfield4']
    VERIFYPASSWORD= request.form['textfield4']
    db=Db()
    return "ok"



@app.route('/registration_form')
def registration_form():
    return render_template("company/registration_form.html")

@app.route('/regstration_form_post',methods=['post'])
def registration_fotm_post():
    COMPANY_NAME = request.form['textfield']
    TAX_ID = request.form['textfield3']
    LEGAL_STATUS = request.form['textfield6']
    FIELD_OF_BUSINESS = request.form['textfield7']
    REGISTERED_OFFICE = request.form['textfield8']
    STATE = request.form['textfield4']
    REGION = request.form['textfield5']
    MUNCIPALITY = request.form['textfield9']
    POSTAL_CODE = request.form['textfield10']
    STREET = request.form['textfield11']
    NUMBER = request.form['textfield12']
    EMAIL = request.form['textfield13']
    TELEPHONE = request.form['textfield14']
    FAX = request.form['textfield15']
    POSTAL_ADDRESS = request.form['textfield16']
    LOGO = request.files['fileField']
    from  datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    LOGO.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\LOGO\\" + dt + ".jpg")
    path = "/static/company/LOGO/" + dt + ".jpg"
    CITY = request.form['textfield19']
    COUNTRY = request.form['textfield20']
    BANK = request.form['textfield21']
    ACCOUNT_NUMBER = request.form['textfield22']
    IFSC = request.form['textfield23']
    TITLE = request.form['textfield24']
    NAME = request.form['textfield26']
    SURNAME = request.form['textfield27']
    DOB = request.form['textfield25']

    PROOF_OF_FINANCIAL_ELIGIBILITY = request.files['fileField']
    from  datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    PROOF_OF_FINANCIAL_ELIGIBILITY.save(
        "C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\PROOF\\" + dt + ".jpg")
    path1 = "/static/company/PROOF/" + dt + ".jpg"
    BANK_GUARANTEE = request.files['fileField2']
    from  datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    BANK_GUARANTEE.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\BANK_PROOF\\" + dt + ".jpg")
    path2 = "/static/company/BANK_PROOF/" + dt + ".jpg"
    checkbox = request.form['textfield4']
    db=Db()
    qry="INSERT INTO `company` (`l_id`,`logo`,`c_name`,`tax_id`,`legal_status`,`field_of_business`,`registered_office`,`state`,`region`,`muncipality`,`postcode`,`street`,`phone_number`,`email`,`telephone`,`fax`,`postal_address`,`city`,`country`,`bank_name`,`bank_number`,`ifsc_code`,`director_name`,`director_title`,`director_surname`,`director_dob`,`bankguarantee`,`proof_of_financialeligibility`) VALUES ('"+str(session['lid'])+"','"+path+"','"+COMPANY_NAME+"','"+TAX_ID+"','"+LEGAL_STATUS+"','"+FIELD_OF_BUSINESS+"','"+REGISTERED_OFFICE+"','"+STATE+"','"+REGION+"','"+MUNCIPALITY+"','"+POSTAL_CODE+"','"+STREET+"','"+NUMBER+"','"+EMAIL+"','"+TELEPHONE+"','"+FAX+"','"+POSTAL_ADDRESS+"','"+CITY+"','"+COUNTRY+"','"+BANK+"','"+ACCOUNT_NUMBER+"','"+IFSC+"','"+NAME+"','"+TITLE+"','"+SURNAME+"','"+DOB+"','"+path1+"','"+path2+"')"
    res=db.insert(qry)
    return '''<script>alert('sucessfully registered');window.location='/'</script>'''



@app.route('/view_profile')
def view_profile():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM company WHERE `l_id`='"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template("company/view_profile.html", data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/edit_profile')
def edit_profile():
    if session['lid'] != '':
        db=Db()
        qry="SELECT * FROM `company` WHERE `l_id`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        return render_template("company/edit_Profile.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/edit_profile_post',methods=['post'])
def edit_profile_post():
    if session['lid'] != '':
        COMPANY_NAME = request.form['textfield']
        TAX_ID = request.form['textfield3']
        LEGAL_STATUS = request.form['textfield6']
        FIELD_OF_BUSINESS = request.form['textfield7']
        REGISTERED_OFFICE = request.form['textfield8']
        STATE = request.form['textfield4']
        REGION = request.form['textfield5']
        MUNCIPALITY = request.form['textfield9']
        POSTAL_CODE = request.form['textfield10']
        STREET = request.form['textfield11']
        NUMBER = request.form['textfield12']
        EMAIL = request.form['textfield13']
        TELEPHONE = request.form['textfield14']
        FAX = request.form['textfield15']
        POSTAL_ADDRESS = request.form['textfield16']
        LOGO = request.files['fileField']
        from  datetime import datetime
        dt=datetime.now().strftime("%Y%m%d-%H%M%S")
        LOGO.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\LOGO\\"+ dt +".jpg")
        path="/static/company/LOGO/"+dt+".jpg"
        CITY = request.form['textfield19']
        COUNTRY = request.form['textfield20']
        BANK = request.form['textfield21']
        ACCOUNT_NUMBER = request.form['textfield22']
        IFSC = request.form['textfield23']
        TITLE = request.form['textfield24']
        NAME = request.form['textfield26']
        SURNAME = request.form['textfield27']
        DOB = request.form['textfield25']
        TITLE = request.form['textfield28']
        NAME = request.form['textfield29']
        SURNAME = request.form['textfield29']
        DOB = request.form['textfield29']
        TITLE = request.form['textfield29']
        NAME = request.form['textfield29']
        SURNAME = request.form['textfield29']
        DOB = request.form['textfield29']
        PROOF_OF_FINANCIAL_ELIGIBILITY = request.files['fileField']
        from  datetime import datetime
        dt = datetime.now().strftime("%Y%m%d-%H%M%S")
        PROOF_OF_FINANCIAL_ELIGIBILITY.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\PROOF\\" + dt + ".jpg")
        path1 = "/static/company/PROOF/" + dt + ".jpg"
        BANK_GUARANTEE = request.files['fileField2']
        from  datetime import datetime
        dt = datetime.now().strftime("%Y%m%d-%H%M%S")
        BANK_GUARANTEE.save("C:\\Users\\sabar\\PycharmProjects\\Investment\\static\\company\\BANK_PROOF\\" + dt + ".jpg")
        path2 = "/static/company/BANK_PROOF/" + dt + ".jpg"
        checkbox = request.form['textfield4']
        db = Db()
        qry = "UPDATE `company` SET `logo`='"+path+"',`c_name`='"+COMPANY_NAME+"',`tax_id`='"+TAX_ID+"',`legal_status`='"+LEGAL_STATUS+"',`field_of_business`='"+FIELD_OF_BUSINESS+"',`registered_office`='"+REGISTERED_OFFICE+"',`state`='"+STATE+"',`region`='"+REGION+"',`muncipality`='"+MUNCIPALITY+"',`postcode`='"+POSTAL_CODE+"',`street`='"+STREET+"',`email`='"+EMAIL+"',`fax`='"+FAX+"',`postal_address`='"+POSTAL_ADDRESS+"',`city`='"+CITY+"',`country`='"+COUNTRY+"',`bank_name`='"+BANK+"',`bank_number`='"+ACCOUNT_NUMBER+"',`ifsc_code`='"+IFSC+"',`director_name`='"+NAME+"',`director_title`='"+TITLE+"',`director_surname`='"+SURNAME+"',`director_dob`='"+DOB+"',`bankguarantee`='"+path2+"',`proof_of_financialeligibility`='"+path1+"' WHERE `l_id`='"+str(session['lid'])+"' "
        res = db.update(qry)
        return '''<script>alert('Sucessfully changed');window.location='/'</script>'''
        return "ok"
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''

@app.route('/view_orders')
def view_orders():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM `orders` "
        res = db.select(qry)
        return render_template("company/view_orders.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/view_trader')
def view_trader():
    if session['lid'] != '':
        db = Db()
        qry = "SELECT * FROM trader"
        res = db.select(qry)
        return render_template("company/view_trader.html",data=res)
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''


@app.route('/c_home')
def c_home():
    if session['lid'] != '':
        return render_template("company/company_index.html")
    else:
        return '''<script>alert('you are logged out');window.location='/'</script>'''
# ========================================== TRADER=====================================================================#


@app.route('/and_login', methods=['POST'])
def and_login():
    db=Db()
    username=request.form['username']
    password=request.form['password']
    qry = "SELECT * FROM login WHERE `user_name`='" + username + "' AND `password`='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        qry2="SELECT * FROM `trader` WHERE l_id='"+str(res['login_id'])+"'"
        res2=db.selectOne(qry2)
        return jsonify(status="ok",type=res['type'],lid=res['login_id'],name=res2['user_name'],email=res2['email'],photo=res2['photo'])
    else:
        return jsonify(status="not ok")



@app.route('/signup_t1',methods=['post'])
def signup_t1():
    EMAIL = request.form['EMAIL']
    db=Db()
    qry = "SELECT * FROM login WHERE `user_name`='" + EMAIL + "' "
    res = db.selectOne(qry)
    if res is None:



        import random
        v=random.randint(000000,999999)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("investunlisted000@gmail.com","wypygvjwttrtpiyv")

        subject = "verification mail"
        body = "your OTP/verification code is "+str(v)
        msg = "subject: "+subject+"\n\n"+body
        server.sendmail("investunlisted000@gmail.com",EMAIL,msg)
        server.quit()

        return jsonify(status="ok",otp=str(v))
    else:
        return jsonify(status="not ok")

@app.route('/signup_t1_post',methods=['post'])
def signup_t1_post():
    OTP=request.form['textfield2']
    db=Db()
    qry=""
    return "ok"


@app.route('/signup_t2_post',methods=['post'])
def signup_t2_post():
    DOB=request.form['textfield2']
    WHAT_IS_YOUR_GENDER=request.form['select2']
    MARITAL_STATUS=request.form['select2']
    WHAT_IS_YOUR_ANNUAL_INCOME=request.form['select2']
    WHAT_IS_YOUR_OCCUPATION=request.form['select']
    SELECT_YOUR_COUNTRY=request.form['select2']
    DECLARATION=request.form['checkbox']
    db=Db()
    qry="INSERT INTO `trader`(dob`,`gender`,`marital_status`,`annual_income`,`occuppation`,`country`) VALUES ('"+DOB+"','"+WHAT_IS_YOUR_GENDER+"','"+MARITAL_STATUS+"','"+WHAT_IS_YOUR_ANNUAL_INCOME+"','"+WHAT_IS_YOUR_OCCUPATION+"','"+SELECT_YOUR_COUNTRY+"')"
    res=db.insert(qry)
    return '''<script>alert('sucessfull');window.location='/signup_t3'</script>'''

@app.route('/signup_t3')
def signup_t3():
    return render_template("trader/Signup_t3.html")

@app.route('/signup_t3_post',methods=['post'])
def signup_t3_post():
    Account_Holder_Name=request.form['accountname']
    IFSC_CODE=request.form['ifsc']
    BANK_ACCOUNT_NUMBER=request.form['accountnumber']
    ACCOUNT_TYPE=request.form['accounttype']

    DOB = request.form['vdob']
    WHAT_IS_YOUR_GENDER = request.form['vgender']
    MARITAL_STATUS = request.form['vmaritalstatus']
    WHAT_IS_YOUR_ANNUAL_INCOME = request.form['vannualincome']
    WHAT_IS_YOUR_OCCUPATION = request.form['voccupation']
    SELECT_YOUR_COUNTRY = request.form['vcountry']

    EMAIL = request.form['vemail']
    password=request.form['vpassword']
    ivuploaddocs=request.form['ivuploaddocs']
    import base64
    from datetime import datetime
    ss=base64.b64decode(ivuploaddocs)
    xx=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    with open(r"C:\Users\sabar\PycharmProjects\Investment\static\trader\proof\\"+xx,'wb') as fs:
        fs.write(ss)
    path="/static/trader/proof/"+xx
    db = Db()

    qrylogin="INSERT INTO `login`(`user_name`,`password`,`type`) VALUES('"+EMAIL+"','"+password+"','trader')"
    res1=db.insert(qrylogin)

    qry = "INSERT INTO `trader`(l_id,`accountholder_name`,`ifsc_code`,`account_number`,`account_type`,`dob`,`gender`,`marital_status`,`annual_income`,`occuppation`,`country`,`email`,`photo`) VALUES ('"+str(res1)+"','"+Account_Holder_Name+"','"+IFSC_CODE+"','"+BANK_ACCOUNT_NUMBER+"','"+ACCOUNT_TYPE+"','"+DOB+"','"+WHAT_IS_YOUR_GENDER+"','"+MARITAL_STATUS+"','"+WHAT_IS_YOUR_ANNUAL_INCOME+"','"+WHAT_IS_YOUR_OCCUPATION+"','"+SELECT_YOUR_COUNTRY+"','"+EMAIL+"','"+path+"')"
    res=db.insert(qry)
    return jsonify(status="ok")



@app.route('/changepassword_post',methods=['post'])
def changepassword_post():
    currentpassword=request.form['currentpassword']
    newpassword=request.form['newpassword']
    confirmpassword=request.form['confirmpassword']
    lid=request.form['lid']
    db=Db()
    db = Db()
    qry = "SELECT * FROM login WHERE `password`='" + currentpassword + "' AND `login_id`='" + lid + "'"
    res = db.selectOne(qry)
    if newpassword == confirmpassword:
        db = Db()
        qry = "UPDATE login SET `password`='" + confirmpassword + "' WHERE `login_id`='" + lid + "'"
        res = db.update(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="not ok")


@app.route('/and_viewprofile', methods=['POST'])
def and_viewprofile():
    db = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM `trader`WHERE `l_id`='"+lid+"'"
    res = db.selectOne(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_sentcomplaint', methods=['POST'])
def and_sentcomplaint():
    sentcomplaint=request.form['complaint']
    lid = request.form['lid']
    db = Db()
    qry = "INSERT INTO`complaint`(`date`,`user_id`,`complaint`,`reply`,`status`) VALUES (CURDATE(),'"+lid+"','"+sentcomplaint+"','pending','pending')"
    res = db.insert(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_viewreply', methods=['POST'])
def and_viewreply():
    db = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM`complaint`WHERE `user_id`='"+lid+"'"
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_newsfeed', methods=['POST'])
def and_newsfeed():
    db = Db()
    qry = "SELECT * FROM `newsfeed`"
    res = db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_portifolio', methods=['POST'])
def and_portifolio():
    db = Db()
    qry = "SELECT * FROM `portifolio`"
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_feedback', methods=['POST'])
def and_feedbacl():
    feedback=request.form['feedback']
    rating=request.form['rating']
    lid = request.form['lid']
    db = Db()
    qry = "INSERT INTO`feedback`(`user_id`,`date`,`feedback`,`rating`) VALUES ('"+lid+"',CURDATE(),'"+feedback+"','"+rating+"')"
    res = db.insert(qry)
    return jsonify(status="ok")




@app.route('/and_watchlist', methods=['POST'])
def and_watchlist():
    db = Db()
    lid=request.form['lid']
    qry = "SELECT * FROM`watchlist` INNER JOIN `company` ON `watchlist`.`c_id`=`company`.`l_id`"
    res = db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_delete_watchlist', methods=['POST'])
def and_delete_watchlist():
    db = Db()
    wid=request.form['wid']
    qry = "DELETE FROM `watchlist` WHERE `watch_id`='"+wid+"'"
    res = db.delete(qry)
    return jsonify(status="ok")




@app.route('/and_add_watchlist', methods=['POST'])
def and_add_watchlist():
    lid=request.form['lid']
    cid=request.form['cid']
    print(cid,"ooooooooooooooo")
    qry2="SELECT * FROM `watchlist` WHERE `c_id`='"+cid+"' AND `uid`='"+lid+"'"
    db=Db()
    res=db.selectOne(qry2)
    if res is None:
        qry="INSERT INTO `watchlist` (`c_id`,`uid`) VALUES('"+cid+"','"+lid+"')"
        db=Db()
        db.insert(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="no")

















#================================Blockchain======================================================




@app.route('/and_forgot_password', methods=['POST'])
def and_forgot_password():

    email=request.form['email']

    qry="SELECT * FROM `login` WHERE `user_name`='"+email+"'"
    db=Db()
    res=db.selectOne(qry)

    import smtplib
    from email.message import EmailMessage

    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender, recipients, and subject of the email
    msg['From'] = 'tradechain4@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Tradechain Password'

    # Set the body of the email
    msg.set_content("This is your password:"+str(res['password']))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start the TLS encryption
        smtp.starttls()

        # Log in to your email account
        smtp.login('tradechain4@gmail.com', 'barulvmjpehkynls')

        # Send the email
        smtp.send_message(msg)

    return jsonify(status="ok")






@app.route('/forgotpassword')
def forgotpassword():
    return render_template("forgot_index.html")








@app.route('/forgot_password_post', methods=['POST'])
def forgot_password_post():

    email=request.form['textfield']

    qry="SELECT * FROM `login` WHERE `user_name`='"+email+"'"
    db=Db()
    res=db.selectOne(qry)

    import smtplib
    from email.message import EmailMessage

    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender, recipients, and subject of the email
    msg['From'] = 'tradechain4@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Tradechain Password'

    # Set the body of the email
    msg.set_content("This is your password:"+str(res['password']))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start the TLS encryption
        smtp.starttls()

        # Log in to your email account
        smtp.login('tradechain4@gmail.com', 'barulvmjpehkynls')

        # Send the email
        smtp.send_message(msg)

    return "<script>alert('password sent to your registered email address');window.location='/'</script>"












if __name__ == '__main__':
    app.run(debug=True,port=4000,host='0.0.0.0')
