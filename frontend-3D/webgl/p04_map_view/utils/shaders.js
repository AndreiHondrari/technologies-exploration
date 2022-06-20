"use strict";

function loadShader(gl, shaderType, shaderSource) {
  const shader = gl.createShader(shaderType);
  gl.shaderSource(shader, shaderSource);
  gl.compileShader(shader);

  // check if shader compiled successfully
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    const shaderInfoLog = gl.getShaderInfoLog(shader);
    alert(
      `Could not compile shader ${shaderSource} | ${shaderInfoLog}`,
    );
    gl.deleteShader(shader);
    return null;
  }

  return shader;
}

function initShaderProgram(gl, vsSource, fsSource) {
  // load our shaders
  const vertexShader = loadShader(
    gl,
    gl.VERTEX_SHADER,
    vsSource,
  );

  const fragmentShader = loadShader(
    gl,
    gl.FRAGMENT_SHADER,
    fsSource,
  );

  // create the shader program
  const shaderProgram = gl.createProgram();

  gl.attachShader(shaderProgram, vertexShader);
  gl.attachShader(shaderProgram, fragmentShader);

  gl.linkProgram(shaderProgram);

  if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
    const programInfoLog = gl.getProgramInfoLog(shaderProgram);
    alert(`Unable to link program | ${programInfoLog}`);
    return null;
  }

  return shaderProgram;
}

export { initShaderProgram };
