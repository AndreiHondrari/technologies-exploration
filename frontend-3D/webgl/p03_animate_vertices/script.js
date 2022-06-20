"use strict";

import {
  drawScene,
  makeProgram,
  makeScene,
  makeSceneState,
} from "./drawing.js";

function main() {
  const canvas = document.querySelector("#canvas-1");

  const gl = canvas.getContext("webgl");

  if (gl === null) {
    alert("WebGL you shall not (problem?)");
    return;
  }

  const sceneState = makeSceneState();

  const programInfo = makeProgram(gl);
  const sceneInfo = makeScene(gl);

  const render = () => {
    const callDrawScene = () =>
      drawScene(gl, programInfo, sceneInfo, sceneState, render);

    requestAnimationFrame(callDrawScene);
  };

  requestAnimationFrame(render);
}

window.onload = main;
