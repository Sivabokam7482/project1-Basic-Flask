from flask import Flask

AppIns=Flask(__name__)


@AppIns.route('/main')
def main():
    return 'This is Flask'


if __name__=='__main__':
    AppIns.run(debug=True)