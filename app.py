import sys
from flask import Flask, jsonify,request
from datetime import datetime
sys.path.append("./factory")
from bson import json_util
from factory.card_factory import CardFactory
import json
from flask_cors import cross_origin
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os
import csv
from send_log_to_loggly import send_log_to_loggly
import pdfplumber
# Load environment variables from .env file
load_dotenv(dotenv_path='/Users/ramnath/Desktop/projects/amex/.env')
gpt_api_key = os.getenv('gpt_api_key')
log_token = os.getenv('log_token')

# record={ "title": "MongoDB and Python"} 
  
# # inserting the data in the database 
# rec = collection.insert_one(record) 
# print(rec)
# print("Inserted document ID:", rec.inserted_id)

# query = {"public_id": data_key}
# current_user = collection.find_one(query)

app = Flask(__name__)
CORS(app)
@app.route('/')
@cross_origin()
def get():
    return "working"
@cross_origin()
@app.route('/bankTransaction', methods=['POST'])
def card():
    try:
        if 'file' not in request.files:
            return 'No file part in the request', 400
        
        file = request.files['file']
        if not file.filename.lower().endswith('.pdf'):
            return 'File is not a PDF', 400

        #file.save("upload_file.pdf")

        userid=request.form['userid']
        file_name=request.form['fileName']+'_'+userid
        with pdfplumber.open(file) as pdf_file:
            first_page=(pdf_file.pages[0].extract_text())
        #file="upload_file.pdf"
        factory = CardFactory()
        card_type=factory.get_card_type(first_page)
        # if(card_type == 'discover' or card_type == 'amex' or card_type == 'apple'):
        
        print("card_type",card_type)
        if card_type is not None:
            card = factory.get_card(card_type)
            if card is not None:
                print("Processing for Card type : %s " %(card.card_type()))
            else:
                print("Card type %s is not supported.", card.card_type())
                sys.exit(-1)
            card.extract_table(file,userid,file_name)
            #final_data=find(file_name)
            return json.loads(json_util.dumps(card.extract_table(file,userid,file_name)))
    except Exception as e:
        log_message = {
            "timestamp": datetime.now().isoformat(),
            "level": "ERROR",
            "message": str(e),
            "exception": repr(e)  # This gives a detailed description of the exception
        }
        send_log_to_loggly(log_token,log_message)
        return jsonify({'error': str(e)}), 500
    # else:
    #     return 'Unknown card', 400
        # return jsonify(final_data)

# @cross_origin()
# @app.route('/bankTransaction',methods=['PUT'])
# def deleteStatementTransaction():
#     data=request.json
#     update(data['_id'])
#     # print(data)
#     return {"response":"Success"}

# @cross_origin()
# @app.route('/bankTransaction/<path:file_path>', methods=['GET'])
# def displayTransaction(file_path):
#     print("into the get call")
#     print("file_path",file_path)
#     final_data = find(file_path)
#     print(final_data)
#     return json.loads(json_util.dumps(final_data))

@cross_origin()
@app.route('/classify', methods=['POST'])
def classify():
    try:
        data = request.get_json()
        input_text = data.get('text', '')
        openai.api_key = gpt_api_key
        prompt = '''classify:'''+ input_text+'''\nCategories: housing, transportation, dining, health, others'''
        print(prompt)
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([input_text, 'House'])

        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "user", "content": prompt}
        #     ]
        # )

        # answer = response.choices[0].message['content']
        # print(answer)
        return jsonify({'classification': 'House'})
    except Exception as e:
        log_message = {
            "timestamp": datetime.now().isoformat(),
            "level": "ERROR",
            "message": str(e),
            "exception": repr(e)  # This gives a detailed description of the exception
        }
        send_log_to_loggly(log_token,log_message)
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)