
from geminiapi import error_detector, executor
import markdown
import os
from dotenv import load_dotenv
load_dotenv()
chat_sessions = {}
error_detector_model = error_detector()
executor_model = executor()
import markdown
import os

@app.route('/codepage')
def codepage():
 return render_template('codepage.html')
@app.route('/analyze', methods=['POST'])
def analyze_code():
 code = request.json.get("code", "")
 session_id = request.json.get("session_id", "default")
 if not code.strip():
 return jsonify({"error": "Please enter code for analysis."})
 try:
 # Create or get chat session
 if session_id not in chat_sessions:
 chat_sessions[session_id] = {
 "error_detector": error_detector_model.start_chat(),
 "executor": executor_model.start_chat(),
 }
 # Send message to error detector
 response = chat_sessions[session_id]["error_detector"].send_message(code)
 # Convert markdown to HTML with extensions
 html_response = markdown.markdown(
 response.text,
 extensions=[
 "fenced_code", # For code blocks
 "tables", # For tables
 "nl2br", # For converting newlines to line breaks
 "sane_lists", # For cleaner lists
 ],
 )
 return jsonify({"text": response.text, "html": html_response})
 except Exception as e:
 return jsonify({"error": f"Error during analysis: {str(e)}"})
@app.route("/execute", methods=["POST"])
def execute_code():
 code = request.json.get("code", "")
 session_id = request.json.get("session_id", "default")
 if not code.strip():
 return jsonify({"error": "Please enter code for execution."})
 try:
 # Create or get chat session
 if session_id not in chat_sessions:
 chat_sessions[session_id] = {
 "error_detector": error_detector_model.start_chat(),
 "executor": executor_model.start_chat(),
 }
 # Send message to executor
 response = chat_sessions[session_id]["executor"].send_message(code)
 # Convert markdown to HTML with extensions
 html_response = markdown.markdown(
 response.text,
 extensions=[
 "fenced_code", # For code blocks
 "tables", # For tables
 "nl2br", # For converting newlines to line breaks
 "sane_lists", # For cleaner lists
 ],
 )
 return jsonify({"text": response.text, "html": html_response})
 except Exception as e:
 return jsonify({"error": f"Error during execution: {str(e)}"})
@app.route("/clear", methods=["POST"])
def clear_history():
 session_id = request.json.get("session_id", "default")
 # Reset the chat sessions
 if session_id in chat_sessions:
 chat_sessions[session_id] = {
 "error_detector": error_detector_model.start_chat(),
 "executor": executor_model.start_chat(),
 }
 return jsonify({"message": "History cleared successfully"})

  
         
        