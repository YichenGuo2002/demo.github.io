import { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import api from './api';

function App() {
  const [data, setData] = useState(null);  // to hold the API response
  const [error, setError] = useState(null);

  useEffect(() => {
    // Call the api() function on component mount
    const fetchData = async () => {
      try {
        const result = await api();
        console.log(result)
        setData(result);
      } catch (err) {
        console.error("API call failed:", err);
        setError("Failed to load data");
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Edit <code>src/App.js</code> and save to reload.</p>

        <div style={{ marginTop: '20px' }}>
          <h2>🔌 API Response:</h2>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          {data ? (
            <pre>{JSON.stringify(data, null, 2)}</pre>
          ) : (
            <p>Loading...</p>
          )}
        </div>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;