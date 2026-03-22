# AI Curriculum Coverage (Todo List)

## 01-mechanics-of-learning
- [x] **Theory:** Understand dot product, cost functions (MSE), gradient descent (`01_00_theory_overview.md`).
- [x] **Practice:** Annotate and run existing scripts (`01_01_auto_synapse_training.py`, `01_02_practice_cost_function.py`, `01_03_sigmoid_graph.py`).
- [x] **Project:** Build a linear regression engine ($y = mx + b$) using pure code that updates its weights using a custom loop.

## 02-the-engine
- [ ] **Theory:** Neural networks as pipelines, backpropagation, and tokenization.
- [ ] **Practice:** Build a simple forward-pass neuron pipeline and calculate errors.
- [ ] **Project:** Code a mini Transformer "Self-Attention" mechanism (Fuzzy Dictionary) from scratch.

## 03-model-taxonomy
- [ ] **Theory:** Vectorizers, Embeddings, LLMs vs SLMs vs Edge models.
- [ ] **Practice:** Generate raw text embeddings out of strings and measure their mathematical distance.
- [ ] **Project:** Spin up a local SLM (e.g., `Phi-3`) and communicate with it using a basic Python wrapper.

## 04-architectures-and-variations
- [ ] **Theory:** CNNs for vision, RNNs for memory, SSMs for infinite context.
- [ ] **Practice:** Write a basic image convolution script (passing a sliding window/filter over a 2D array).
- [ ] **Project:** Knowledge Distillation experiment (training a tiny model to mimic a larger model's outputs).

## 05-advanced-retrieval-and-structure
- [ ] **Theory:** Vector Search Algorithms (HNSW, Binary Quantization) and RAG.
- [ ] **Practice:** Write a rudimentary vector database lookup engine in memory.
- [ ] **Project:** Implement an Advanced RAG Pattern (Hybrid Retrieval combining Vector DB with BM25).

## 06-local-systems-engineering
- [ ] **Theory:** Quantization, structured outputs, and raw memory efficiency.
- [ ] **Practice:** Run a GBNF grammar constraint on an SLM to physically force it to output valid JSON.
- [ ] **Project:** Implement system optimizations using zero-copy deserialization (`rkyv` in Rust) for vectors.

## 07-agentic-ai
- [ ] **Theory:** The ReAct Pattern (Reason + Act).
- [ ] **Practice:** Parse tool-call JSON commands from an SLM and trigger local Python functions.
- [ ] **Project:** Give a local `Phi-3` model access to your file system to count `.rs` files and return the result autonomously.

## 08-reinforcement-learning
- [ ] **Theory:** Q-Learning mapping & Reward Functions mapping.
- [ ] **Practice:** Build a basic state-action Reward Matrix update loop.
- [ ] **Project:** Build a Python grid where a bot wanders randomly until it learns the perfect path to a target.

## 09-systems-architecture
- [ ] **Theory:** Orchestrators, Gateways, Batching, Analog Computing (Memristors).
- [ ] **Practice:** Program a mock API Gateway to route simple vs complex queries to different "models".
- [ ] **Project:** Program a mock Continuous Batching queue to handle multiple concurrent queries efficiently.

## 10-multimodal-ai
- [ ] **Theory:** Computer Vision arrays and Audio Processing Spectrograms.
- [ ] **Practice:** Convert a small soundwave into an array and visualize its spectrogram.
- [ ] **Project:** Use a local `Whisper.cpp` model to transcribe a 10-second `.wav` file into text, and/or `ort` in Rust for YOLOv8 object detection.
