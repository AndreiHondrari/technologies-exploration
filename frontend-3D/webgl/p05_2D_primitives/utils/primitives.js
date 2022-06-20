"use strict";

import { Vertex } from "./vertices.js";

function makeBox(
  lowerLeftVec,
  upperRightVec,
  color,
) {
  const vertices = [
    new Vertex(lowerLeftVec[0], lowerLeftVec[1], color),
    new Vertex(lowerLeftVec[0], upperRightVec[1], color),
    new Vertex(upperRightVec[0], upperRightVec[1], color),

    new Vertex(upperRightVec[0], upperRightVec[1], color),
    new Vertex(upperRightVec[0], lowerLeftVec[1], color),
    new Vertex(lowerLeftVec[0], lowerLeftVec[1], color),
  ];

  return vertices;
}

function makeCircle(
  centerVec,
  radius,
  color,
  opts = {
    resolution: 30,
  },
) {
  const vertices = [];

  const RADS_PER_SLICE = (Math.PI * 2) / opts.resolution;

  function makeCircleVertex(centerVec, angle) {
    let x = centerVec[0] + Math.sin(angle) * radius;
    let y = centerVec[1] + Math.cos(angle) * radius;
    return new Vertex(x, y, color);
  }

  for (let i = 0; i < opts.resolution; ++i) {
    // center
    vertices.push(new Vertex(centerVec[0], centerVec[1], color));

    // first point
    let angle = RADS_PER_SLICE * i;
    vertices.push(makeCircleVertex(centerVec, angle));

    // second point
    angle = RADS_PER_SLICE * (i + 1);
    vertices.push(makeCircleVertex(centerVec, angle));
  }

  return vertices;
}

function makeTriangle(
  centerVec,
  spread,
  color,
) {
  const THIRD = Math.PI * (120 / 180);
  return [
    new Vertex(
      centerVec[0],
      centerVec[1] + spread,
      color,
    ),
    new Vertex(
      centerVec[0] + Math.sin(THIRD) * spread,
      centerVec[1] + Math.cos(THIRD) * spread,
      color,
    ),
    new Vertex(
      centerVec[0] + Math.sin(THIRD * 2) * spread,
      centerVec[1] + Math.cos(THIRD * 2) * spread,
      color,
    ),
  ];
}

export { makeBox, makeCircle, makeTriangle };
