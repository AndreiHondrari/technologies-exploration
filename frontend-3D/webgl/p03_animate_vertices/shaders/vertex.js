export default `
  attribute vec4 aVertexPosition;
  attribute vec4 aVertexColor;

  uniform mat4 uModelMatrix;

  varying vec4 vColor;

  void main() {
      gl_Position = uModelMatrix * aVertexPosition;
      vColor = aVertexColor;
  }
`;
