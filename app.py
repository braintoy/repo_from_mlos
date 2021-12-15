   
#!/usr/bin/env python3
#+-----------------------------------------------------------------------------------------------+
#| @ Author : Padma Polash Paul[change name] @ Created on June 2015                              |
#| @ Manage Orgs on mlOS Custom APP @ API: v.1                                                   |
#| @ -- mlOS - DEPLOY MODEL                                                                      |
#| Once deployed, app will be protected by mlOS Access Tokern and API key                        |
#+-----------------------------------------------------------------------------------------------+

from flask import Flask, jsonify, request,current_app
app = Flask(__name__)

# POST API END POINT
@app.route("/postinfo", methods=['POST'])
def getinfo():
    rq = request.json.get("rq") 
    result=request.json # returning input
    # ==================================================================================
    #  Your custom api end point 
    #  if you want to return more info from this apiendpoint, you can use add additional attribute to result,
    #  result["more_custom_info_1"] = your_variable_1_here
    #  result["more_custom_info_1"] = your_variable_2_here 
    # ==================================================================================
    return jsonify(result), 200 # DO NOT MODITY THIS LINE
# POST API END GET
@app.route("/getinfo", methods=['GET'])
def getinfo():
    result={
        "key":"value"
    } # returning input
    # ==================================================================================
    #  Your custom api end point 
    #  if you want to return more info from this apiendpoint, you can use add additional attribute to result,
    #  result["more_custom_info_1"] = your_variable_1_here
    #  result["more_custom_info_1"] = your_variable_2_here 
    # ==================================================================================
    return jsonify(result), 200 # DO NOT MODITY THIS LINE

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # for mlCluser
    # app.run( port=5002, debug=True) # for Localhost
                        