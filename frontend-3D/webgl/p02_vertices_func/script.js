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
  gl.bindBuffer(WebGLRenderingContext.ARRAY_BUFFER, positionBuffer);
  gl.bufferData(
    WebGLRenderingContext.ARRAY_BUFFER,
    new Float32Array(positions),
    WebGLRenderingContext.STATIC_DRAW,
  );

  const colorBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
  gl.bufferData(
    WebGLRenderingContext.ARRAY_BUFFER,
    new Float32Array(colors),
    WebGLRenderingContext.STATIC_DRAW,
  );

  return {
    position: positionBuffer,
    color: colorBuffer,
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

function drawScene(gl, programInfo, buffers, positions) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(WebGLRenderingContext.COLOR_BUFFER_BIT);

  bindBufferToAttrib(
    gl,
    WebGLRenderingContext.ARRAY_BUFFER,
    buffers.position,
    programInfo.attribLocations.vertexPosition,
    new BufferAttribBindArgs({ numComponents: 2 }),
  );

  bindBufferToAttrib(
    gl,
    WebGLRenderingContext.ARRAY_BUFFER,
    buffers.color,
    programInfo.attribLocations.vertexColor,
    new BufferAttribBindArgs({ numComponents: 4 }),
  );

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
