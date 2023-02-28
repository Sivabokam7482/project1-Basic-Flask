#Create Application Instance
# Application instance(AppIns) is an Object of Flask Class
# So Import Flask Class
# Flask class will take one arguement that is Name of current Module
# standard way to represent current module name is __name__.

from flask import Flask

AppIns=Flask(__name__)

# create one view function and decorate it with route method of AppIns

@AppIns.route('/siva')
def siva():
    return 'This is Flask'


if __name__=='__main__':
    AppIns.run(debug=True)
