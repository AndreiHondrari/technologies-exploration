# AI Curriculum Coverage (Todo List)

## Part 1: The Mechanics of Learning
- [x] **Theory:** Understand dot product, cost functions (MSE), gradient descent (`01_00_theory_overview.md`).
- [x] **Practice:** Annotate and run existing scripts (`01_01_auto_synapse_training.py`, `01_02_practice_cost_function.py`, `01_03_sigmoid_graph.py`).
- [x] **Project:** Build a linear regression engine using pure code that updates weights via loop.

## Part 2: Classical Machine Learning
- [x] **Theory:** Understand data patterns without neurons (Decision Trees, KNN, K-Means) (`02_00_theory_overview.md`).
- [x] **Practice (Unsupervised):** Build a K-Means clustering algorithm from scratch (`02_01_01_k_means_clustering.py`).
- [x] **Practice (Supervised Geometry):** Build a K-Nearest Neighbors (KNN) classifier (`02_01_02_knn_classifier.py`).
- [x] **Practice (Entropy Logic):** Build an autonomous Decision Tree builder (`02_01_03_decision_tree.py`).
- [x] **Practice (Ensembling):** Evolve the tree into a Random Forest voting system (`02_01_04_random_forest.py`).
- [x] **Practice (GOFAI):** Implement an A* Pathfinding graph search algorithm (`02_01_05_astar_pathfinding.py`).
- [ ] **Project:** Compare the speed and accuracy of a classical supervised learner to a deep learning pipeline.

## Part 3: The Deep Learning Engine (Neural Networks)
- [x] **Theory:** Neural networks as math pipelines and Backpropagation (`03_00_theory_overview.md`).
- [x] **Practice:** Build single & chained neurons, and calculate N-to-1 networks (`03_01_01` to `03_01_04`).
- [x] **Practice (Linearity):** Train a single neuron to solve a linear problem like the OR Logic Gate (`03_01_05_neuron_net.py`).
- [x] **Practice (Non-Linearity):** Prove a single neuron fails the XOR problem (`03_01_06_neuron_net_nonlinear.py`), then fix it using chained Hidden Layers.
- [ ] **Project:** Refactor the hardcoded layers into a dynamic N-to-M architecture Engine (`03_01_07_dynamic_n_to_m.py`).

## Part 4: Data Architectures (Space and Time)
- [ ] **Theory:** CNNs for vision, RNNs for sequence/memory.
- [ ] **Practice:** Build a 36-input flat classification network (one neuron per cell) to prove it fails without spatial awareness (`04_01_01_neuron_per_cell.py`).
- [ ] **Project:** Write a basic Convolution logic script (passing a sliding window over a 2D array).

## Part 5: Natural Language & The Transformer
- [ ] **Theory:** Tokenization, Embeddings, and the Self-Attention mechanism.
- [ ] **Practice:** Build a basic Tokenization Dictionary mapping (`05_01_tokenization.py`).
- [ ] **Practice:** Generate arrays of floats (embeddings) from integers and measure distance (`05_02_embeddings.py`).
- [x] **Project:** Code a mini Transformer "Self-Attention" mechanism (Fuzzy Dictionary) from scratch (`05_03_self_attention.py`).

## Part 6: The Model Taxonomy
- [ ] **Theory:** Differences between Embedding Models, SLMs, and LLMs.
- [ ] **Project:** Spin up a local SLM (e.g., `Phi-3`) and communicate with it using a basic Python wrapper.

## Part 7: Advanced Retrieval & Structure (RAG)
- [ ] **Theory:** Vector Search Algorithms (HNSW, Binary Quantization).
- [ ] **Practice:** Write a rudimentary vector database lookup engine in memory.
- [ ] **Project:** Implement an Advanced Hybrid Retrieval RAG flow combining Vectors and Keyword matching.

## Part 8: Local Systems Engineering (Rust)
- [ ] **Theory:** Quantization and structured generation formatting (GBNF).
- [ ] **Practice:** Run a grammar constraint on an SLM to logically force it to output valid JSON.
- [ ] **Project:** Implement system optimizations using zero-copy deserialization (`rkyv` in Rust) for vectors.

## Part 9: Agentic AI
- [ ] **Theory:** The ReAct Pattern logic flow.
- [ ] **Practice:** Parse tool-call JSON commands from an SLM and trigger local Python functions.
- [ ] **Project:** Give a local `Phi-3` model access to your file system to count `.rs` files and return the result.

## Part 10: Reinforcement Learning (RL)
- [ ] **Theory:** Q-Learning mapping & Reward Functions.
- [ ] **Practice:** Build a basic state-action Reward Matrix update loop.
- [ ] **Project:** Build a Python grid map where a bot wanders randomly until it autonomously learns the perfect path.

## Part 11: AI Systems Architecture & Hardware
- [ ] **Theory:** Continuous Batching, Orchestrators, and API Gateways.
- [ ] **Practice:** Program a mock API Gateway to route simple vs complex queries to different "models".
- [ ] **Project:** Program a mock Batching queue to group multiple incoming queries.

## Part 12: The Senses (Multimodal AI)
- [ ] **Theory:** 3D array detection and Audio Spectrogram processing.
- [ ] **Practice:** Convert a small soundwave into an array and visualize its spectrogram mapping.
- [ ] **Project:** Use a local `Whisper.cpp` model to transcribe `.wav` into text, or use YOLOv8 frame detection.
