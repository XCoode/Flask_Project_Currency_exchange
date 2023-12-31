from flask import Flask ,render_template, request
from flask_cors import CORS,cross_origin
import requests
import json

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/convert',methods=['GET', 'POST'])
def exchange_currency():
  if request.method=='POST':
    try:
      url = "URL_FOR_API_CONNECTION"

      querystring = {"from":request.form.get("fromCurrency"),"to":request.form.get("toCurrency"),"q":request.form.get("amount")}

      headers = {
	       "API-Key": "Paste_your_api_key",
	     "API-Host": "Paste_your_host_url"
       }
    except Exception:
       return Exception
       
    check_value=request.form.get("amount")
    if float(check_value)>0:
      
      response = requests.get(url, headers=headers, params=querystring)
      data = response.json()
  
     #Stroing the data.
      with open("data.json",'w')as f:
       f.write(str(data)+'\n')
       f.close()

     # Open the file in read mode ('r')
      with open("data.json", 'r') as file:
     # Read the content of the file
        json_data = file.read()


    # Parse the JSON data (it's a single value, not a dictionary)
      float_value = json.loads(json_data)
 
    # Calculating the currency value.  
      Amount=request.form.get("amount")
      tocurrency_name=request.form.get("toCurrency")
      fromcurrency_name=request.form.get("fromCurrency")
      currency_value=float_value*float(Amount)
      converted_value=Amount+' '+fromcurrency_name+" = "+(str("{:.3f}".format(currency_value)))+" "+tocurrency_name
      return render_template('result.html', converted_value=converted_value)
    else:
       error_message = "Seem you are trying to enter zero or negative value."
       return render_template('error.html', error_message=error_message)
      
  else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True) 
