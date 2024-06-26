import sys
from flask import Flask, jsonify,request
sys.path.append("./factory")
from bson import json_util
from factory.card_factory import CardFactory
import json
#from database import find
#from database import update
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
@app.route('/bankTransaction', methods=['POST'])
def card():
    if 'file' not in request.files:
        return 'No file part in the request', 400
    
    file = request.files['file']
    if not file.filename.lower().endswith('.pdf'):
        return 'File is not a PDF', 400

    file.save("upload_file.pdf")

    userid=request.form['userid']
    file_name=request.form['fileName']+'_'+userid

    file="upload_file.pdf"
    factory = CardFactory()
    card_type=factory.get_card_type(file)
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
        print(card.extract_table(file,userid,file_name))
        #final_data=find(file_name)
        return json.loads(json_util.dumps(card.extract_table(file,userid,file_name)))
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



if __name__ == "__main__":
    app.run(debug=True)