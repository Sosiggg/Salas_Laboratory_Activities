import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {useEffect, useState} from 'react'

function App() {

  const [post, setPosts] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/v1/api/rental/').then(response =>{
      setPosts(response.data)
    })
  }

  )
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      {
        post.map((obj, index)=><div key={index}>{obj.title}</div>)
      }
    </div>
  );
}

export default App;
