"use strict";

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

export { Color, Vertex, verticesToColors, verticesToPositions };
