import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import reportWebVitals from './reportWebVitals';


const routing = (
  <Router>
    <React.StrictMode>
      <Header/>
      <Routes>
        <Route exact path="/" element={<App/>}/>
      </Routes>
      <Footer/>
    </React.StrictMode>
  </Router>
)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  routing
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
