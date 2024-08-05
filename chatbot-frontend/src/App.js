import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Create a CSS file for styling

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://127.0.0.1:5000/get_response', { message });
    setResponse(res.data.response);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Iron Man Chatbot</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask me anything..."
          />
          <button type="submit">Send</button>
        </form>
        <div className="response">
          {response && <p>{response}</p>}
        </div>
      </header>
    </div>
  );
}

export default App;

