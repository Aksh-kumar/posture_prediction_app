"""Web Server Gateway Interface"""

##################
# FOR PRODUCTION
####################
import os
from src.app import app

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    #app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True, threaded=True)
