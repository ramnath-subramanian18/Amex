import sys
from flask import Flask, jsonify,request
sys.path.append("./factory")
from bson import json_util
from factory.card_factory import CardFactory
import json
from database import find
from database import update
from flask_cors import cross_origin
from flask_cors import CORS



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
def get():
    return "working"
@app.route('/displayStatementTransaction', methods=['POST'])
def card():
    if 'file' not in request.files:
        return 'No file part in the request', 400
    
    file = request.files['file']
    file.save("upload_file.pdf")

    userid=request.form['userid']
    file_name=request.form['fileName']+'_'+userid

    file="upload_file.pdf"
    factory = CardFactory()
    card_type=factory.get_card_type(file)
    print(card_type)
    if card_type is not None:
        card = factory.get_card(card_type)
        if card is not None:
            print("Processing for Card type : %s " %(card.card_type()))
        else:
            print("Card type %s is not supported.", card.card_type())
            sys.exit(-1)
        card.extract_table(file,userid,file_name)
        final_data=find(file_name)
        #print(final_data)
        return json.loads(json_util.dumps(final_data))
        # return jsonify(final_data)

@cross_origin()
@app.route('/deleteStatementTransaction',methods=['PUT'])
def deleteStatementTransaction():
    print('into this')
    data=request.json
    update(data['_id'])
    # print(data)
    return {"response":"Success"}

@cross_origin()
@app.route('/displayTransaction',methods=['POST'])
def displayTransaction():
    data=request.json
    final_data=find(data['file_name'])
    print(final_data)
    return json.loads(json_util.dumps(final_data))

    

if __name__ == "__main__":
    app.run(debug=True)
    #csv_extract_table=factory.get_extract_table(file)

# import sys
# from flask import Flask, jsonify
# from factory.card_factory import CardFactory

# app = Flask(__name__)

# @app.route('/process_file', methods=['GET'])
# def process_file():
#     file = "/Users/ramnath/Desktop/projects/amex/Amex_Sep_14_-_Oct_13.pdf"

#     factory = CardFactory()
#     card_type = factory.get_card_type(file)
#     if card_type is None:
#         return jsonify({'error': 'Unsupported card type'})

#     card = factory.get_card(card_type)
#     if card is None:
#         return jsonify({'error': 'Unsupported card type'})

#     final_data = card.extract_table(file)
#     return jsonify({'final_data': final_data})

# if __name__ == "__main__":
#     app.run(debug=True)
