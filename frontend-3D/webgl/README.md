# WebGL

## Basic program overview

### Taxonomy

- **shType** : shader type
- **src** : shader source
- **sh** : shader
- **gl** : WebGL canvas
- **vs** : Vertex Shader
- **fs** : Fragment Shader

### Load shader sequence diagram

Described:

- instantiate a shader object for a WebGL canvas
- attach a shader source code to the shader object
- compile the shader
- return the cooked shader

```mermaid
sequenceDiagram
    actor user
    participant loadShader
    participant glCanvas
    participant shader

    # call loadShader
    activate glCanvas
    user ->> loadShader : loadShader(gl, shType, src)
    activate loadShader

    # create shader instance
    loadShader ->> glCanvas : createShader(shType)
    glCanvas ->> shader : instantiate
    activate shader
    shader -->> glCanvas : sh instance

    glCanvas -->> loadShader : shader / sh

    # attach shader source to new shader instance
    loadShader ->> glCanvas : shaderSource(sh, src)
    glCanvas ->> shader : attach src

    # compile
    loadShader ->> glCanvas : compileShader(sh)

    # finally
    loadShader -->> user : shader

    deactivate shader
    deactivate loadShader
    deactivate glCanvas
```

### Shader program initialization sequence diagram

Described:

- load vertex shader
- load fragment shader
- create a shader program instance
- attach vertex shader to program
- attach fragment shader to program
- link the program
- retrieve the program

```mermaid
sequenceDiagram
    actor user
    participant loadShader
    participant initShaderProgram
    participant glCanvas
    participant shaderProgram

    user ->> initShaderProgram : (gl, vsSrc, fsSrc)
    activate initShaderProgram

    # load shaders (vertex and fragment)
    initShaderProgram ->> loadShader : (VERTEX_SHADER, vsSrc)
    loadShader -->> initShaderProgram : vs / vertex shader

    initShaderProgram ->> loadShader : (FRAGMENT_SHADER, fsSrc)
    loadShader -->> initShaderProgram : fs / fragment shader

    # create the program
    initShaderProgram ->> glCanvas : createProgram()
    glCanvas ->> shaderProgram : instantiate
    activate shaderProgram
    shaderProgram -->> glCanvas : program
    glCanvas -->> initShaderProgram : program

    # attach shaders to the program
    initShaderProgram ->> glCanvas : attachShader(program, vs)
    initShaderProgram ->> glCanvas : attachShader(program, fs)
    initShaderProgram ->> glCanvas : linkProgram(program)

    # finally
    initShaderProgram -->> user : shader program

    deactivate initShaderProgram
    deactivate shaderProgram
```

### Buffer initialization sequence diagram

Described:

- create a buffer
- bind the buffer to the canvas
- initialize the buffer data with an array
- retrieve the buffer

Taxonomy:

- target : can be ARRAY_BUFFER or ELEMENT_ARRAY_BUFFER
- obj : the actual array with vertices or colors
- usage : STATIC_DRAW, DYNAMIC_DRAW, STREAM_DRAW

```mermaid
sequenceDiagram
    actor user
    participant glCanvas
    participant buffer

    activate glCanvas

    # create buffer
    user ->> glCanvas : createBuffer()
    glCanvas ->> buffer : instantiate
    activate buffer
    buffer -->> glCanvas : instance
    glCanvas ->> user : buffer

    # bind buffer
    user ->> glCanvas : bindBuffer(ARRAY_BUFFER, buffer)
    glCanvas ->> glCanvas : internal bind

    # init buffer
    user ->> glCanvas : bufferData(target, obj, usage)
    glCanvas ->> buffer : put data

    deactivate buffer
    deactivate glCanvas
```

### Overall sequence diagram

Described:

- init shader program
- retrieve attribute location for shader
- populate some positions and colors
- init buffers
- draw scene (example)
  - define a preset clear color (usually black)
  - define the depth presets (example)
    - clearDepth
    - enable DEPTH_TEST
    - declare depth function (for example LEQUAL)
  - actually clear buffers like color and depth buffers
  - bind buffers to shader attributes
  - enable the shader attributes
  - use the program
  - draw the arrays in a given mode (like TRIANGLE_STRIP)

```mermaid
sequenceDiagram
    actor main
    participant utils
    participant drawScene
    participant glCanvas

    # get GL canvas context
    main ->> main : Get GL canv. ctx
    glCanvas -->> main : Retrieve GL can. ctx.
    activate glCanvas

    # init shader program
    main ->>+ utils : initShaderProgram(gl, positions, colors)
    utils -->>- main : shader program

    # retrieve attrib location for shader
    main ->> glCanvas : getAttribLocation(program, "someAttrib")
    glCanvas -->> main : attrib location

    # positions and colors
    main ->> main : make positions
    main ->> main : make colors

    # init buffers
    main ->> main : initBuffers(gl, pos, col)

    # draw scene
    main ->> drawScene : (gl, pInfo, pos, col)
    activate drawScene

    ## define presets
    drawScene ->> glCanvas : clearColor(black)

    ## clear
    drawScene ->> glCanvas : clear(COLOR_BUFFER_BIT)

    ## bind buffers to shader attributes
    drawScene ->> glCanvas : vertexAttribPointer(attribPos, ...args)

    ## enable shader attributes
    drawScene ->> glCanvas : enableVertexAttribArray(attribPos)

    ## use shader program
    drawScene ->> glCanvas : useProgram(program)

    ## draw arrays
    drawScene ->> glCanvas : drawArrays(mode, ...args)

    deactivate drawScene

    deactivate glCanvas
```

## Observations

- `bindBuffer` must every time come before operating on that specific buffer in
  a WebGL Context
