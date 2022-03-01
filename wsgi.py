"""Web Server Gateway Interface"""

##################
# FOR PRODUCTION
####################
from src.app import app

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    #app.run(host='0.0.0.0', debug=True)
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
