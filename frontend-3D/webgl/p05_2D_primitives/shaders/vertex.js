export default `
  attribute vec4 aVertexPosition;
  attribute vec4 aVertexColor;

  uniform mat4 uModelMatrix;
  uniform mat4 uViewMatrix;

  varying vec4 vColor;

  void main() {
      gl_Position = uViewMatrix * uModelMatrix * aVertexPosition;
      vColor = aVertexColor;
  }
`;
