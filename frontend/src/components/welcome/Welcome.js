import React, { useState } from "react";
//import axios from "axios";
import hamburger from './../../assets/hamburger.png';
import newChat from './../../assets/edit.png';
import logout from './../../assets/log-out.png'
import send from './../../assets/send.png'
import "./Welcome.css"


export const Welcome = () => {
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
            <div className="chat">
                <div className="logout">
                    <button className="logout-btn">
                        <div className="logout-section">
                            <img src={logout} alt="logout" />
                            <h3>Logout</h3>
                        </div>
                    </button>
                </div>
                <div className="welcome-section">
                    <div className="welcome">
                        <div className="welcome-text">
                            <h1 className="morning">Good Morning!</h1>
                            <h2 className="name">Talel Ayed</h2>
                        </div>
                        <div className="help">
                            <h1 className="ask">How can I help you?</h1>
                        </div>
                    </div>
                    <div className="keyboard">
                        <input type="text" className="input" placeholder="Ask Anything..."></input>
                            <button className="send">
                                <img src={send} alt="send" />
                            </button>
                    </div>
                </div>
            </div>
        </div>)
}