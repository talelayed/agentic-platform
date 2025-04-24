import React, { useState } from "react";
//import axios from "axios";
import hamburger from './../assets/hamburger.png';
import newChat from './../assets/edit.png';
import "./Chatbot.css"


export const Chatbot = () => {
 return (<div className="container">
            <div className="chat-history">
                <div className="flex">
                    <h1 className="logo">EIRA</h1>
                    <img className="hamburger" src={hamburger} alt="hamburger"/>
                </div>
                <h3>Chat history</h3>
                <h2>What is Generative AI ?</h2>
                <button className="new-chat-btn">
                    <div className="new-chat">
                        <img src={newChat} alt="new chat" />
                        <h2>New chat</h2>
                    </div>
                </button>
            </div>
            <div></div>
        </div>)
}