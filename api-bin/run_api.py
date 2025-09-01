import os
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
base_dir = os.path.abspath(os.path.dirname(__file__))

import logging
logging.basicConfig(filename=os.path.join(base_dir, "api-bin.log"), level=logging.DEBUG, format=f'%(asctime)s - %(levelname)s - %(name)s : %(message)s')

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

try:
    # Configure SQLite
    SQLITE_DB_DIR = os.path.join(base_dir, "database")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "data_bin.sqlite3")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)

    # Model for storing incoming JSON data
    class RequestData(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        data = db.Column(db.JSON, nullable=False)
        timestamp = db.Column(db.DateTime)

    # Create the database
    with app.app_context():
        db.create_all()

    # API index route
    @app.route("/", methods=["POST", "GET", "DELETE", "PUT", "PATCH"])
    def index():
        return jsonify({
            "message": "Welcome to API-Bin! Please use the following API endpoints - ",
            "p1": " /api_bin_data -> (POST, GET, DELETE)",
            "p2": " /api_bin_data/{{id}} -> (GET, DELETE, PUT)"
        }), 200

    # Create and Read All and Delete All data entry
    @app.route("/api_bin_data", methods=["POST", "GET", "DELETE"])
    def handle_all_data():
        if request.method == "POST":
            if not request.is_json:
                return jsonify({"error": "Only JSON data allowed"}), 400
            
            json_data = request.get_json()
            entry = RequestData(data=json_data, timestamp=datetime.now())
            db.session.add(entry)
            db.session.commit()
            
            return jsonify({
                "message": "Data stored successfully",
                "id": entry.id,
                "data": json_data
            }), 201

        elif request.method == "GET":
            entries = RequestData.query.all()
            if len(entries) < 1:
                return jsonify(
                {
                    "message": "Empty entries",
                }), 200
            else:
                return jsonify([
                    {
                        "id": e.id,
                        "data": e.data,
                        "timestamp": e.timestamp.isoformat()
                    }
                    for e in entries
                ]), 200

        elif request.method == "DELETE":
            entry = RequestData.query.all()
            if entry == None:
                return jsonify(
                {
                    "error": "Entries not found",
                }
            ), 404

            entry_id = [e.id for e in entry]
            data = [e.data for e in entry]
            time = [e.timestamp.isoformat() for e in entry]
            deleted_count = RequestData.query.delete()
            db.session.commit()
            return jsonify({
                "deleted":[
                    {      
                        "id": entry_id[i],
                        "data": data[i],
                        "entry-timestamp": time[i]
                    } 
                for i in range(len(entry_id))],
                "message": f"{deleted_count} data entry deleted successfully",
            }), 200

        else:
            return jsonify({
                "error": "<!> Bad Request",
            }), 400


    # Read and Update and Delete a single data entry
    @app.route("/api_bin_data/<int:entry_id>", methods=["GET", "DELETE", "PUT"])
    def handle_single_data(entry_id):
        if request.method == "GET":
            entry = RequestData.query.filter_by(id=entry_id).first()
            if entry == None:
                return jsonify({"error": "Entry not found"}), 404
            return jsonify({
                "id": entry.id,
                "data": entry.data,
                "timestamp": entry.timestamp.isoformat()
            }), 200
        
        elif request.method == "DELETE":
            entry = RequestData.query.filter_by(id=entry_id).first()
            if entry == None:
                return jsonify(
                {
                    "error": "Entry not found",
                }
            ), 404

            data = entry.data
            time = entry.timestamp.isoformat()
            db.session.delete(entry)
            db.session.commit()
            return jsonify(
                {
                    "message": "Data deleted successfully",
                    "id": entry_id,
                    "data": data,
                    "entry-timestamp": time
                }
            ), 200
        
        elif request.method == "PUT":
            entry = RequestData.query.filter_by(id=entry_id).first()
            if entry == None:
                return jsonify({"error": "Entry not found"}), 404

            if not request.is_json:
                return jsonify({"error": "Only JSON data allowed"}), 400

            json_data = request.get_json()
            entry.data = json_data
            entry.timestamp = datetime.now()
            db.session.commit()

            return jsonify({
                "message": f"Entry {entry_id} updated successfully",
                "id": entry.id,
                "data": entry.data,
                "timestamp": entry.timestamp.isoformat()
            }), 200

        else:
            return jsonify({
                "error": "<!> Bad Request",
            }), 400

    if __name__ == "__main__":
        print("\n#>> A simple CRUD api for testing api calls from a frontend\n\n > Endpoint1 : /api_bin_data -> (POST, GET, DELETE)\n > Endpoint2 : /api_bin_data/{{id}} -> (GET, DELETE, PUT)")
        print("\n  #>> API-Bin running at : http://127.0.0.1:6788\n (ctrl + c - to stop the API)\n")
        app.run(debug=False, port=6788)

except Exception as e:
    app.logger.error(e)