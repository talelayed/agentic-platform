import React from "react";
import "./App.css"
import { Chatbot } from "./components/chatbot/Chatbot";
import { Welcome } from "./components/welcome/Welcome";
import { Home } from "./components/home/Home";
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/welcome" element={<Welcome/>}/>
        <Route path="/chatbot" element={<Chatbot/>}/>
      </Routes>
    </Router>
  );
}

export default App;
