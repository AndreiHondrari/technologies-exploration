"use strict";

function loadShader(gl, shaderType, shaderSource) {
  const shader = gl.createShader(shaderType);
  gl.shaderSource(shader, shaderSource);
  gl.compileShader(shader);

  // check if shader compiled successfully
  if (!gl.getShaderParameter(shader, WebGLRenderingContext.COMPILE_STATUS)) {
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
    WebGLRenderingContext.VERTEX_SHADER,
    vsSource,
  );

  const fragmentShader = loadShader(
    gl,
    WebGLRenderingContext.FRAGMENT_SHADER,
    fsSource,
  );

  // create the shader program
  const shaderProgram = gl.createProgram();

  gl.attachShader(shaderProgram, vertexShader);
  gl.attachShader(shaderProgram, fragmentShader);

  gl.linkProgram(shaderProgram);

  if (
    !gl.getProgramParameter(shaderProgram, WebGLRenderingContext.LINK_STATUS)
  ) {
    const programInfoLog = gl.getProgramInfoLog(shaderProgram);
    alert(`Unable to link program | ${programInfoLog}`);
    return null;
  }

  return shaderProgram;
}

function initBuffers(gl) {
  const positionBuffer = gl.createBuffer();

  gl.bindBuffer(WebGLRenderingContext.ARRAY_BUFFER, positionBuffer);

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
    WebGLRenderingContext.ARRAY_BUFFER,
    new Float32Array(positions),
    WebGLRenderingContext.STATIC_DRAW,
  );

  return {
    position: positionBuffer,
  };
}

class BufferAttribBindArgs {
  constructor(
    {
      numComponents,
      bufferType = WebGLRenderingContext.FLOAT,
      normalize = false,
      stride = 0,
      offset = 0,
    },
  ) {
    this.numComponents = numComponents;
    this.bufferType = bufferType;
    this.normalize = normalize;
    this.stride = stride;
    this.offset = offset;
  }
}

function bindBufferToAttrib(gl, target, buffer, attribPosition, bindArgs) {
  gl.bindBuffer(target, buffer);

  gl.vertexAttribPointer(
    attribPosition,
    bindArgs.numComponents,
    bindArgs.bufferType,
    bindArgs.normalize,
    bindArgs.stride,
    bindArgs.offset,
  );

  gl.enableVertexAttribArray(attribPosition);
}

function drawScene(gl, programInfo, buffers) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(WebGLRenderingContext.COLOR_BUFFER_BIT);

  bindBufferToAttrib(
    gl,
    WebGLRenderingContext.ARRAY_BUFFER,
    buffers.position,
    programInfo.attribLocations.vertexPosition,
    new BufferAttribBindArgs({ numComponents: 2 }),
  );

  // program
  gl.useProgram(programInfo.program);

  // scope
  {
    const offset = 0;
    const vertexCount = 4;
    gl.drawArrays(WebGLRenderingContext.TRIANGLE_STRIP, offset, vertexCount);
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
