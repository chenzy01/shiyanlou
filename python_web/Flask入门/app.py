from flask import Flask,render_template,redirect,url_for,request,make_response

app=Flask(__name__)

@app.route('/')
def index():
    default=request.cookies.get('username')
    return redirect(url_for('user_index',username=default))

@app.route('/user/<username>')
def user_index(username):
    resp=make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    return resp

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run()
