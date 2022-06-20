"use strict";

import "./vendor/glMatrix/gl-matrix.js";

import { initShaderProgram } from "./utils/shaders.js";

import {
  Color,
  verticesToColors,
  verticesToPositions,
} from "./utils/vertices.js";

import { bindBufferToAttrib, BufferAttribBindArgs } from "./utils/buffers.js";

import { makeBox, makeCircle, makeTriangle } from "./utils/primitives.js";

import VS_SOURCE from "./shaders/vertex.js";
import FS_SOURCE from "./shaders/fragment.js";

const SCREEN_SCALE = 100;

const RED = new Color(1.0, 0.0, 0.0);
const GREEN = new Color(0.0, 1.0, 0.0);
const BLUE = new Color(0.0, 0.0, 1.0);
const WHITE = new Color(1.0, 1.0, 1.0);
const CYAN = new Color(0.0, 1.0, 1.0);

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
      viewMatrix: gl.getUniformLocation(shaderProgram, "uViewMatrix"),
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

const BOX1_OFFSET = 20;
const BOX1_CENTER = [40, 0];

const CIRCLE_RADIUS = 20;

const TRIANGLE1_SPREAD = 15;
const TRIANGLE1_CENTER = [0, 0];

function getVertices() {
  const vertices = [];

  vertices.push(...makeBox(
    glMatrix.vec2.fromValues(
      BOX1_CENTER[0] - BOX1_OFFSET,
      BOX1_CENTER[1] - BOX1_OFFSET,
    ),
    glMatrix.vec2.fromValues(
      BOX1_CENTER[0] + BOX1_OFFSET,
      BOX1_CENTER[1] + BOX1_OFFSET,
    ),
    GREEN,
  ));

  vertices.push(...makeCircle(
    glMatrix.vec2.fromValues(-40, 0),
    CIRCLE_RADIUS,
    RED,
  ));

  vertices.push(...makeCircle(
    glMatrix.vec2.fromValues(0, 40),
    CIRCLE_RADIUS,
    BLUE,
  ));

  vertices.push(...makeCircle(
    glMatrix.vec2.fromValues(0, -40),
    CIRCLE_RADIUS,
    WHITE,
  ));

  vertices.push(...makeTriangle(
    TRIANGLE1_CENTER,
    TRIANGLE1_SPREAD,
    CYAN,
  ));

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
    rotationAngle: 0,
  };
  return sceneState;
}

const ROTATION_AMOUNT_DEG = 3;
const ROTATION_AMOUNT_RAD = Math.PI * (ROTATION_AMOUNT_DEG / 180);

function updateModel(sceneState) {
  const TRANS_AMOUNT = 20;
  const ADVANCE_AMOUNT = 0.50;

  // translate frame
  if (
    (sceneState.modelTranslationVec[0]) >= TRANS_AMOUNT |
    (sceneState.modelTranslationVec[0]) >= TRANS_AMOUNT
  ) {
    sceneState.forward = false;
  }

  if (
    (sceneState.modelTranslationVec[0]) <= -TRANS_AMOUNT |
    (sceneState.modelTranslationVec[0]) <= -TRANS_AMOUNT
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

  // rotate frame
  sceneState.rotationAngle += ROTATION_AMOUNT_RAD;

  if (sceneState.rotationAngle >= (Math.PI * 2)) {
    sceneState.rotationAngle = 0;
  }
}

function drawScene(gl, programInfo, sceneInfo, sceneState, callback) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(WebGLRenderingContext.COLOR_BUFFER_BIT);

  // declare a view matrix to alter the way the world is viewed
  const viewMatrix = glMatrix.mat4.create();
  const SCALE_FACTOR = 1 / SCREEN_SCALE;
  glMatrix.mat4.scale(viewMatrix, viewMatrix, [
    SCALE_FACTOR,
    SCALE_FACTOR,
    SCALE_FACTOR,
  ]);
  // console.log(viewMatrix);

  // declare a model matrix to alter the objects in the world
  const modelMatrix = glMatrix.mat4.create();
  updateModel(sceneState);
  glMatrix.mat4.translate(
    modelMatrix,
    modelMatrix,
    sceneState.modelTranslationVec,
  );
  glMatrix.mat4.rotate(
    modelMatrix,
    modelMatrix,
    sceneState.rotationAngle,
    [0, 0, 1],
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

  // bind the view matrix to the shader view matrix uniform
  gl.uniformMatrix4fv(
    programInfo.uniformLocations.viewMatrix,
    false,
    viewMatrix,
  );

  // bind the model matrix to the shader model matrix uniform
  gl.uniformMatrix4fv(
    programInfo.uniformLocations.modelMatrix,
    false,
    modelMatrix,
  );

  // draw
  {
    const offset = 0;
    const vertexCount = Math.round(sceneInfo.positions.length / 2);
    gl.drawArrays(WebGLRenderingContext.TRIANGLES, offset, vertexCount);
  }

  callback();
}

export { drawScene, makeProgram, makeScene, makeSceneState };
