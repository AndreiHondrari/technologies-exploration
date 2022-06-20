"use strict";

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

export { bindBufferToAttrib, BufferAttribBindArgs };
