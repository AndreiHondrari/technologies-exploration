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

function initBuffers(gl) {
  const positionBuffer = gl.createBuffer();

  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);

  const positions = [
    // top right
    0.1,
    0.1,

    //
    -0.2,
    0.2,

    //
    0.1,
    -0.1,

    //
    -0.1,
    -0.1,
  ];

  gl.bufferData(
    gl.ARRAY_BUFFER,
    new Float32Array(positions),
    gl.STATIC_DRAW,
  );

  return {
    position: positionBuffer,
  };
}

function drawScene(gl, programInfo, buffers) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clearDepth(1.0);
  gl.enable(gl.DEPTH_TEST);
  gl.depthFunc(gl.LEQUAL);
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

  gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);

  // scope
  {
    const numComponents = 2;
    const bufferType = gl.FLOAT;
    const normalize = false;
    const stride = 0;
    const offset = 0;

    gl.vertexAttribPointer(
      programInfo.attribLocations.vertexPosition,
      numComponents,
      bufferType,
      normalize,
      stride,
      offset,
    );

    gl.enableVertexAttribArray(
      programInfo.attribLocations.vertexPosition,
    );
  }

  // program
  gl.useProgram(programInfo.program);

  // scope
  {
    const offset = 0;
    const vertexCount = 4;
    gl.drawArrays(gl.TRIANGLE_STRIP, offset, vertexCount);
  }
}

function main() {
  const canvas = document.querySelector("#canvas-1");

  const gl = canvas.getContext("webgl");

  if (gl === null) {
    alert("WebGL you shall not (problem?)");
    return;
  }

  const VS_SOURCE = `
    attribute vec4 aVertexPosition;

    void main() {
        gl_Position = aVertexPosition;
    }
  `;

  const FS_SOURCE = `
    void main() {
      gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    }
  `;
  const shaderProgram = initShaderProgram(gl, VS_SOURCE, FS_SOURCE);
  const programInfo = {
    program: shaderProgram,
    attribLocations: {
      vertexPosition: gl.getAttribLocation(
        shaderProgram,
        "aVertexPosition",
      ),
    },
  };

  const buffers = initBuffers(gl);

  drawScene(gl, programInfo, buffers);
}

window.onload = main;
