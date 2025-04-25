import React, { Suspense } from "react";
import "./Home.css"
import { Robot } from "../robot/Robot";
import { Environment } from '@react-three/drei';
import { Canvas } from '@react-three/fiber';

export const Home = () => {
    return<div className="main">
        <h1 className="eira">EIRA</h1>
        <div className="sub-container">
            <div className="connect">
                <button className="login">LOGIN</button>
                <button className="register">REGISTER</button>
            </div>
            <div className="robot">
            <Canvas style={{width:"100vw", height:"100vh", position:"absolute", top:"0", left:"0"}}>
                      <Suspense fallback={null}>
                        <Robot/>
                        <Environment preset="sunset"  />
                      </Suspense>
            </Canvas>
            </div>   
        </div>
    </div>
}