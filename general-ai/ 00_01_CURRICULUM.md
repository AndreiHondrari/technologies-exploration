# The "Code-First" AI Engineering Curriculum

## The Prime Directive: "Code is your Math"
* **If you see $\Sigma$ (Sigma):** It’s just a `for` loop that sums things up.
* **If you see a Matrix ($X$):** It’s just a 2D array or a list of lists.
* **If you see a Dot Product ($A \cdot B$):** It’s just multiplying two arrays item-by-item and adding up the results.
* **If you see a Derivative ($\partial$):** It’s just tweaking a variable by a tiny amount (`0.001`) to see if the error goes up or down.

---

## Part 1: The Mechanics of Learning (De-Blackboxing ML)
*Goal: Understand how models correct their own mistakes.*
* **The "Dot Product" Intuition:** AI doesn't "think"—it just measures distances between arrays of numbers.
* **The "Blame Game" (Calculus made simple):**
    * **Cost Functions (MSE):** Writing a function to calculate exactly how wrong the model is.
    * **Gradient Descent:** A loop: "If I increase the weight by 0.01, does my error go down? If yes, keep going."
* **Practical Project:** Build a linear regression engine ($y = mx + b$) using pure code that updates its weights using a custom loop.

## Part 2: The Engine (Deep Learning & Transformers)
*Goal: Understand neural networks through software architecture analogies.*
* **Neural Networks as Pipelines:** A neuron is a function that multiplies inputs by weights, adds a bias, and clamps the output.
* **Backpropagation:** "Blame assignment." The network works backwards to figure out which neuron caused the error.
* **Tokenization:** Treating words like a massive `Enum` mapping.
* **The Transformer (Attention Mechanism):** "Self-Attention" as a **Fuzzy Dictionary**. When reading "Bank", it looks at surrounding words to adjust the meaning.

## Part 3: The Model Taxonomy (Right-Sizing the Brain)
*Goal: Understand the classes of models.*
* **Vectorizers / Embedding Models:** Tiny models used as "Semantic Hash Functions" to map text to float arrays for search.
* **LLMs (Large Language Models):** Massive monoliths for open-ended reasoning via API.
* **SLMs (Small Language Models):** Local binaries (like `Phi-3`). Perfect for stateless logic and structured JSON extraction.
* **Embedded / Edge Models:** Microscopic models. Act like interrupt handlers on an RTOS to do one specific job locally.

## Part 4: Architectures & Variations (Beyond Text)
*Goal: Understand specialized models based on their data flow.*
* **CNNs (Vision):** Passing a magnifying glass over an image to find edges, then shapes.
* **RNNs (Memory):** A `while` loop that passes a "state" variable to the next iteration.
* **SSMs (State Space Models):** Linear time sequence models for infinite context windows with constant memory.
* **Knowledge Distillation:** Training an SLM by having it copy the outputs of a massive LLM.

## Part 5: Advanced Retrieval & Structure (RAG Internals)
*Goal: Master vector databases.*
* **Vector Search Algorithms:**
    * **HNSW:** A multi-layered skip-list for floating-point arrays.
    * **Binary Quantization:** Rounding floats to `0` or `1` for bitwise `XOR` operations.
* **Advanced RAG Patterns:**
    * **Hybrid Retrieval:** Combining a Vector DB with BM25 (exact keyword matching).
    * **GraphRAG:** Parsing text into JSON objects to traverse relationships logically.

## Part 6: Local Systems Engineering (The Rust Stack)
*Goal: Run AI fast and lean.*
* **Quantization & Compression:** Casting a 16-bit float to a 4-bit integer to save RAM.
* **Structured Generation (GBNF):** Forcing SLMs to output strictly valid JSON by physically blocking invalid characters.
* **System Optimizations:** Using zero-copy deserialization (`rkyv` in Rust) to memory-map gigabytes of vectors instantly.

## Part 7: Agentic AI (Reacting to Patterns)
*Goal: Treat AI as a `while` loop that can use tools.*
* **The ReAct Pattern (Reason + Act):** Give an SLM a prompt with tools. The model outputs a JSON command, your code executes it, and feeds the result back.
* **Practical Project:** Give a local `Phi-3` model access to your file system to count `.rs` files and return the result.

## Part 8: Reinforcement Learning (RL)
*Goal: Train a system to learn by trial and error.*
* **Q-Learning & Reward Functions:** A giant lookup table mapping a `State` to an `Action`. Reward good actions, punish bad ones.
* **Practical Project:** Build a Python grid where a bot wanders randomly until it learns the perfect path to a target.

## Part 9: AI Systems Architecture & Hardware
*Goal: Scale to production and understand the physical future of AI.*
* **The Orchestrator Pattern:** API Gateways that route simple questions to tools and complex questions to LLMs.
* **Continuous Batching & KV Caching:** Handling many users simultaneously by caching attention states in memory.
* **Edge AI & Embedded Inferencing:** Putting quantized models directly on IoT sensors to process signal noise locally.
* **Analog & Neuromorphic Computing:**
    * **Memristors:** Physical resistors calculating matrix math at the speed of electricity.
    * **Neuromorphic:** Chips that physically mimic brain spikes to save battery life.

## Part 10: The Senses (Multimodal AI)
*Goal: The practical culmination—teaching your code to see and hear using pre-trained models.*
* **Computer Vision (Object Detection):** An image is just a 3D array. Models draw bounding boxes over arrays matching specific math patterns.
* **Audio Processing (Hearing):** Converting soundwaves into **Spectrograms**, then using Vision techniques to "look" at the sound.
* **Practical Project:** Use a local `Whisper.cpp` model to transcribe a 10-second `.wav` file into text, or use `ort` in Rust to feed a webcam frame into YOLOv8 to detect objects.