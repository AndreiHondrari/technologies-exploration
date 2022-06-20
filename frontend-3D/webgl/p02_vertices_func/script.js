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

class Color {
  constructor(r, g, b, alpha = 1.0) {
    this.r = r;
    this.g = g;
    this.b = b;
    this.alpha = alpha;
  }
}

class Vertex {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
  }
}

function getVertices() {
  const RED = new Color(1.0, 0.0, 0.0);
  const GREEN = new Color(0.0, 1.0, 0.0);
  const BLUE = new Color(0.0, 0.0, 1.0);
  const WHITE = new Color(1.0, 1.0, 1.0);

  const VERTEX_OFFSET = 0.7;
  const vertices = [
    new Vertex(VERTEX_OFFSET, VERTEX_OFFSET, RED),
    new Vertex(-VERTEX_OFFSET, VERTEX_OFFSET, GREEN),
    new Vertex(VERTEX_OFFSET, -VERTEX_OFFSET, BLUE),
    new Vertex(-VERTEX_OFFSET, -VERTEX_OFFSET, WHITE),
  ];

  return vertices;
}

function verticesToPositions(vertices) {
  const positions = [];

  for (const vertex of vertices) {
    positions.push(vertex.x);
    positions.push(vertex.y);
  }

  return positions;
}

function verticesToColors(vertices) {
  const colors = [];
  for (const vertex of vertices) {
    colors.push(vertex.color.r);
    colors.push(vertex.color.g);
    colors.push(vertex.color.b);
    colors.push(vertex.color.alpha);
  }

  return colors;
}

function initBuffers(gl, positions, colors) {
  const positionBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
  gl.bufferData(
    gl.ARRAY_BUFFER,
    new Float32Array(positions),
    gl.STATIC_DRAW,
  );

  const colorBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
  gl.bufferData(
    gl.ARRAY_BUFFER,
    new Float32Array(colors),
    gl.STATIC_DRAW,
  );

  return {
    position: positionBuffer,
    color: colorBuffer,
  };
}

function drawScene(gl, programInfo, buffers, positions) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(gl.COLOR_BUFFER_BIT);

  gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
  // vertex position attrib to buffer bind
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

  gl.bindBuffer(gl.ARRAY_BUFFER, buffers.color);
  // vertex color attrib to buffer bind
  {
    const numComponents = 4;
    const bufferType = gl.FLOAT;
    const normalize = false;
    const stride = 0;
    const offset = 0;

    gl.vertexAttribPointer(
      programInfo.attribLocations.vertexColor,
      numComponents,
      bufferType,
      normalize,
      stride,
      offset,
    );

    gl.enableVertexAttribArray(
      programInfo.attribLocations.vertexColor,
    );
  }

  // program
  gl.useProgram(programInfo.program);

  // draw
  {
    const offset = 0;
    const vertexCount = Math.round(positions.length / 2);
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
    attribute vec4 aVertexColor;

    varying vec4 vColor;

    void main() {
        gl_Position = aVertexPosition;
        vColor = aVertexColor;
    }
  `;

  const FS_SOURCE = `
    precision mediump float;
    varying vec4 vColor;

    void main() {
      gl_FragColor = vColor;
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
      vertexColor: gl.getAttribLocation(
        shaderProgram,
        "aVertexColor",
      ),
    },
  };

  const vertices = getVertices();
  const positions = verticesToPositions(vertices);
  const colors = verticesToColors(vertices);

  if (positions.length % 2 != 0) {
    console.error("Number of vertices is not an exact multiple of 2");
    return;
  }

  const buffers = initBuffers(gl, positions, colors);

  drawScene(gl, programInfo, buffers, positions);
}

window.onload = main;
