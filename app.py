from flask import Flask, render_template, request, redirect

app = Flask(__name__)

student = [
    {'name': 'John', 'age': '25', 'course': 'Python'},
    {'name': 'Mary', 'age': '22', 'course': 'Java'},
    {'name': 'Peter', 'age': '30', 'course': 'C++'},
]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    # return  需要实现的页面
    # request 对象可以拿到浏览器传递给服务器的所有数据
    # request.form 拿到表单数据
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print("从服务器拿到的数据:", username, password)
        return redirect('/admin')

    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', students=student)


@app.route('/append', methods=['GET', 'POST'])
def append():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        print(name, age, course)
        student.append({'name': name, 'age': age, 'course': course})
        return redirect('/admin')
    return render_template('append.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        name = request.args.get('name')
        print(name)
        for i in student:
            if i['name'] == name:
                student.remove(i)
                break
        return redirect('/admin')
    return render_template('admin.html')


@app.route('/change', methods=['GET', 'POST'])
def change():
    if request.method == 'GET':
        name = request.args.get('name')
        print(name)
        for i in student:
            if i['name'] == name:
                return render_template('change.html', students=i)
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        print(name, age, course)
        for i in student:
            if i['name'] == name:
                i['age'] = age
                i['course'] = course
                break
        return render_template('admin.html', students=student)



if __name__ == '__main__':
    app.run()
