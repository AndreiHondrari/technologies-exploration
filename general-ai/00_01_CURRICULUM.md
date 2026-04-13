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

## Part 2: Classical Machine Learning (AI without "Deep" Layers)
*Goal: Prove that learning data patterns does not actually require neurons.*
* **Decision Trees & Random Forests:** Having code autonomously build highly optimal `if/else` logic flowcharts based on data entropy.
* **KNN & SVMs (Supervised Classification):** Making predictions simply based on geometric proximity to other known data points on a graph.
* **K-Means Clustering (Unsupervised):** Throwing raw, unlabelled data at an algorithm and watching it autonomously find the centers of mass to group segments.
* **Good Old-Fashioned AI (GOFAI):** The bedrock of early AI: Pathfinding (A*), Genetic Algorithms, and Search (Minimax for chess).

## Part 3: The Deep Learning Engine (Neural Networks)
*Goal: Master the fully differentiable pipeline.*
* **Neural Networks as Pipelines:** A neuron is a function that multiplies inputs by weights, adds a bias, and clamps the output.
* **Backpropagation:** "Blame assignment." The network works backwards using continuous gradients to figure out exactly which hidden weight caused the error.
* **Coordinate-Based ML:** Using a network as a continuous math function to map raw coordinates ($x, y$) directly to colors.
* **The Variation Taxonomy:** Systematically scaling architectures (Single Neuron $\to$ Chained $\to$ Dynamic N-Layers) to concretely prove how folding non-linear math solves complex multi-dimensional grids.

## Part 4: Data Architectures (Space and Time)
*Goal: Specializing the engine to handle Geometry and Sequence.*
* **CNNs (Computer Vision & Space):** Standard neural networks fail if an object moves 1 pixel. CNNs solve this by dragging a "Convolutional Window" (magnifying glass) over the grid to detect local features identically anywhere.
* **RNNs (Memory & Time):** Normal networks are 100% stateless. RNNs solve time-sequences via a `while` loop that hands its current "state" to the next sequential iteration.
* **SSMs (State Space Models):** Linear time sequence models for infinite context windows with constant memory.

## Part 5: Natural Language & The Transformer
*Goal: Making the abstract leap from numerical models to semantic word models.*
* **Tokenization:** Mapping words to integers (Text $\to$ Integer IDs).
* **Embeddings:** Throwing the Integer into a massive lookup table to get a Float Array. Using distance calculations to prove "Bank" is mathematically closer to "Money" than "Dog".
* **Self-Attention (The Transformer):** Replacing the sequential scanning of older models with a massive, parallel "Fuzzy Dictionary" lookup that calculates dynamic context scores for everything at once.

## Part 6: The Model Taxonomy (Right-Sizing the Brain)
*Goal: Understand the physical classes of modern AI models.*
* **Vectorizers / Embedding Models:** Tiny models used as "Semantic Hash Functions" for RAG.
* **LLMs (Large Language Models):** Massive monoliths for open-ended reasoning via API.
* **SLMs (Small Language Models):** Local binaries (like `Phi-3`). Perfect for fast, stateless extraction.
* **Knowledge Distillation:** Extracting the "brain" of a massive LLM into a smaller architecture.

## Part 7: Advanced Retrieval & Structure (RAG Internals)
*Goal: Master vector databases.*
* **Vector Search Algorithms:** HNSW (skip-lists for vectors), Binary Quantization (rounding floats for bitwise XOR).
* **Advanced RAG Patterns:** Hybrid Retrieval (Vector + Keyword) and GraphRAG.

## Part 8: Local Systems Engineering (The Rust Stack)
*Goal: Run AI fast and lean.*
* **Quantization & Compression:** Casting a 16-bit float to a 4-bit integer to save massive RAM.
* **Structured Generation (GBNF):** Forcing SLMs to output strictly valid JSON by physically blocking invalid characters.
* **System Optimizations:** Using zero-copy deserialization (`rkyv` in Rust) to memory-map gigabytes of vectors instantly.

## Part 9: Agentic AI (Reacting to Patterns)
*Goal: Treat AI as a `while` loop that can use tools.*
* **The ReAct Pattern (Reason + Act):** Give an SLM a prompt with tools. The model outputs a JSON command, your code executes it, and feeds the result back.
* **Practical Project:** Give a local `Phi-3` model access to your file system to count `.rs` files and return the result.

## Part 10: Reinforcement Learning (RL)
*Goal: Train a system to learn by trial and error.*
* **Q-Learning & Reward Functions:** A giant lookup table mapping a `State` to an `Action`. Reward good actions, punish bad ones.
* **Practical Project:** Build a Python grid where a bot wanders randomly until it learns the perfect path to a target.

## Part 11: AI Systems Architecture & Hardware
*Goal: Scale to production and understand the physical future of AI.*
* **The Orchestrator Pattern:** API Gateways that route simple questions to tools and complex questions to LLMs.
* **Continuous Batching & KV Caching:** Handling many users simultaneously by caching attention states in memory.
* **Hardware Futures:** Analog Computing, Memristors, and Neuromorphic chips.

## Part 12: The Senses (Multimodal AI)
*Goal: The practical culmination—teaching your code to see and hear using pre-trained models.*
* **Computer Vision (Object Detection):** An image is just a 3D array. Models draw bounding boxes over arrays matching specific math patterns.
* **Audio Processing (Hearing):** Converting soundwaves into **Spectrograms**, then using Vision techniques to "look" at the sound.
* **Practical Project:** Use a local `Whisper.cpp` model to transcribe a `.wav` file into text, or use `ort` in Rust to feed a webcam frame into YOLOv8 to detect objects.