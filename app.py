from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load generic college data
with open("data/college_data.json", "r", encoding="utf-8") as f:
    college_data = json.load(f)

def get_answer(question):
    question = question.lower()

    # Hostel related
    if "hostel" in question:
        h = college_data["hostels"][0]
        return (
            f"{h['name']} offers rooms for {h['room_occupancy']}. "
            f"Facilities: {h['facilities']}. "
            f"Washroom: {h['washroom']}. "
            f"Fees: {h['fees']}."
        )

    # General FAQ
    for item in college_data["general"]:
        if any(word in question for word in item["question"].lower().split()):
            return item["answer"]

    return "Sorry, I don’t have information on that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    answer = get_answer(data.get("question", ""))
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
