from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
from xhs.request.AsyncRequestFramework import AsyncRequestFramework
from xhs.request.note import Notes
import json
app = Flask(__name__)
CORS(app)
arf = AsyncRequestFramework()
note = Notes(arf)

@app.route('/xhs_search', methods=['POST'])
def xhs_search():
    data = request.get_json() 
    if not data: return jsonify({"error": "Invalid JSON data"}), 400
    note_num = 100 if data.get('note_num') is None else int(data.get('note_num'))
    like_threshold = 100 if data.get('like_threshold') is None else int(data.get('like_threshold'))    
    items = []
    page=1
    while len(items)<note_num:
        response = asyncio.run(note.search_notes(keyword=data.get('keyWord'),page=page))
        page+=1
        if response["success"]=="false" or response["data"]["has_more"]=="false" or "items" not in response["data"]: break
        for item in response["data"]["items"]:
            try: 
                if int(item["note_card"]["interact_info"]["liked_count"]) >= like_threshold: items.append(item)
            except Exception as e: continue
    sorted_items_desc = sorted(items, key=lambda item: int(item["note_card"]["interact_info"]["liked_count"]), reverse=True)
    response = {"items": sorted_items_desc}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=19900, debug=True)
