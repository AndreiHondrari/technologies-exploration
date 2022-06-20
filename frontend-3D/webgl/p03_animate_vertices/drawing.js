"use strict";

import "./vendor/glMatrix/gl-matrix.js";

import { initShaderProgram } from "./utils/shaders.js";

import {
  Color,
  Vertex,
  verticesToColors,
  verticesToPositions,
} from "./utils/vertices.js";

import { bindBufferToAttrib, BufferAttribBindArgs } from "./utils/buffers.js";

import VS_SOURCE from "./shaders/vertex.js";
import FS_SOURCE from "./shaders/fragment.js";

function makeProgram(gl) {
  const shaderProgram = initShaderProgram(
    gl,
    VS_SOURCE,
    FS_SOURCE,
  );
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

    uniformLocations: {
      modelMatrix: gl.getUniformLocation(shaderProgram, "uModelMatrix"),
    },
  };

  return programInfo;
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
  gl.bindBuffer(WebGLRenderingContext.ARRAY_BUFFER, colorBuffer);
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

const VERTEX_OFFSET = 0.2;

function getVertices() {
  const RED = new Color(1.0, 0.0, 0.0);
  const GREEN = new Color(0.0, 1.0, 0.0);
  const BLUE = new Color(0.0, 0.0, 1.0);
  const WHITE = new Color(1.0, 1.0, 1.0);

  const vertices = [
    new Vertex(VERTEX_OFFSET, VERTEX_OFFSET, RED),
    new Vertex(-VERTEX_OFFSET, VERTEX_OFFSET, GREEN),
    new Vertex(VERTEX_OFFSET, -VERTEX_OFFSET, BLUE),
    new Vertex(-VERTEX_OFFSET, -VERTEX_OFFSET, WHITE),
  ];

  return vertices;
}

function makeScene(gl) {
  const vertices = getVertices();
  const positions = verticesToPositions(vertices);
  const colors = verticesToColors(vertices);

  if (positions.length % 2 != 0) {
    console.error("Number of vertices is not an exact multiple of 2");
    return;
  }

  const buffers = initBuffers(gl, positions, colors);

  return {
    vertices,
    positions,
    colors,
    buffers,
  };
}

function makeSceneState() {
  const sceneState = {
    modelTranslationVec: glMatrix.vec3.create(),
    forward: true,
  };
  return sceneState;
}

const ADVANCE_AMOUNT = 0.005;

function updateModel(sceneState) {
  if (
    (sceneState.modelTranslationVec[0] + VERTEX_OFFSET) >= 1 |
    (sceneState.modelTranslationVec[0] + VERTEX_OFFSET) >= 1
  ) {
    sceneState.forward = false;
  }

  if (
    (sceneState.modelTranslationVec[0] - VERTEX_OFFSET) <= -1 |
    (sceneState.modelTranslationVec[0] - VERTEX_OFFSET) <= -1
  ) {
    sceneState.forward = true;
  }

  if (sceneState.forward) {
    glMatrix.vec3.add(
      sceneState.modelTranslationVec,
      sceneState.modelTranslationVec,
      [ADVANCE_AMOUNT, ADVANCE_AMOUNT, 0],
    );
  } else {
    glMatrix.vec3.add(
      sceneState.modelTranslationVec,
      sceneState.modelTranslationVec,
      [-ADVANCE_AMOUNT, -ADVANCE_AMOUNT, 0],
    );
  }

  return sceneState.modelTranslationVec;
}

function drawScene(gl, programInfo, sceneInfo, sceneState, callback) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(WebGLRenderingContext.COLOR_BUFFER_BIT);

  // declare a model matrix to alter the objects in the world
  const modelMatrix = glMatrix.mat4.create();
  updateModel(sceneState);
  glMatrix.mat4.translate(
    modelMatrix,
    modelMatrix,
    sceneState.modelTranslationVec,
  );

  // bind the model matrix to the shader model matrix uniform
  gl.uniformMatrix4fv(
    programInfo.uniformLocations.modelMatrix,
    false,
    modelMatrix,
  );

  // bind position array to the shader attribute
  bindBufferToAttrib(
    gl,
    WebGLRenderingContext.ARRAY_BUFFER,
    sceneInfo.buffers.position,
    programInfo.attribLocations.vertexPosition,
    new BufferAttribBindArgs({ numComponents: 2 }),
  );

  // bind color array to the shader attribute
  bindBufferToAttrib(
    gl,
    WebGLRenderingContext.ARRAY_BUFFER,
    sceneInfo.buffers.color,
    programInfo.attribLocations.vertexColor,
    new BufferAttribBindArgs({ numComponents: 4 }),
  );

  // program
  gl.useProgram(programInfo.program);

  // draw
  {
    const offset = 0;
    const vertexCount = Math.round(sceneInfo.positions.length / 2);
    gl.drawArrays(WebGLRenderingContext.TRIANGLE_STRIP, offset, vertexCount);
  }

  callback();
}

export { drawScene, makeProgram, makeScene, makeSceneState };
