# Domain Taxonomy for Modern Graph Theory (Bollobás, 1998)

## Categories

- **graph-fundamentals**: Basic definitions, graph types, degree sequences, basic graph operations
- **paths-and-cycles**: Paths, walks, cycles, trees, forests, Euler/Hamilton structures
- **planar-graphs**: Planarity, Euler's formula, Kuratowski's theorem, graphs on surfaces
- **electrical-networks**: Ohm's law, Kirchhoff's laws, resistance, conductance, network equivalence
- **linear-algebra-of-graphs**: Incidence/adjacency/Laplacian matrices, cycle/cut spaces, matrix-tree theorem
- **network-flows**: Directed graphs, flows, capacities, max-flow min-cut, augmenting paths
- **connectivity**: Vertex/edge connectivity, Menger's theorem, blocks, cutvertices, bridges
- **matchings**: Matchings, perfect matchings, Hall's theorem, König's theorem, Tutte's theorem, stable matchings
- **extremal-graph-theory**: Forbidden subgraphs, Turán theory, extremal functions, density results
- **regularity-method**: Szemerédi's regularity lemma, epsilon-regular pairs, regularity applications
- **vertex-coloring**: Chromatic number, Brooks' theorem, chromatic polynomial, greedy coloring
- **edge-coloring**: Chromatic index, Vizing's theorem, edge coloring of bipartite graphs
- **list-coloring**: List-chromatic number, choosability
- **perfect-graphs**: Perfect graphs, Perfect Graph Theorem, Berge's conjecture
- **ramsey-theory**: Ramsey numbers, Ramsey's theorem, canonical Ramsey, van der Waerden, Hales-Jewett
- **random-graphs**: G(n,p) and G(n,M) models, threshold functions, phase transitions, giant component
- **probabilistic-method**: Expectation, variance, concentration inequalities, existence proofs
- **algebraic-graph-theory**: Cayley/Schreier diagrams, group presentations, automorphisms
- **spectral-graph-theory**: Adjacency/Laplacian eigenvalues, spectral properties, strongly regular graphs
- **graph-enumeration**: Pólya's theorem, Burnside's lemma, cycle index, counting labeled/unlabeled graphs
- **random-walks**: Simple random walks, Markov chains, hitting/commute times, mixing, stationary distributions
- **conductance-and-mixing**: Conductance, rapid mixing, spectral gap, expansion
- **tutte-polynomial**: Tutte polynomial, rank-generating polynomial, deletion-contraction, special values
- **statistical-mechanics**: Ising/Potts models, partition functions, random cluster model
- **knot-theory**: Jones/Kauffman polynomials, knot diagrams, Reidemeister moves, link polynomials

## Tiers

- **foundational**: Basic graph definitions, fundamental structures (Ch I core concepts)
- **intermediate**: Requires foundational concepts; classical theorems and methods (Ch I advanced, Ch II-V core)
- **advanced**: Requires intermediate concepts; deep structural results (Ch IV-X specialized topics)

## Notation Conventions

### Graph Notation
- G = (V, E) for a graph with vertex set V and edge set E
- |V(G)| = n (order), |E(G)| = e(G) or m (size)
- d(v) or deg(v) for degree of vertex v
- δ(G) for minimum degree, Δ(G) for maximum degree
- K_n for complete graph, K_{r,s} for complete bipartite graph
- C_n for cycle, P_n for path

### Standard Functions
- χ(G) for chromatic number
- χ'(G) for chromatic index
- ω(G) for clique number
- α(G) for independence number
- κ(G) for vertex connectivity
- λ(G) for edge connectivity
- ex(n; F) for extremal function
- R(s,t) for Ramsey number
- T(G; x,y) for Tutte polynomial
- P(G; k) for chromatic polynomial

### Probability Notation
- G(n,p) for binomial random graph
- G(n,M) for uniform random graph
- a.s. for "almost surely" (with probability tending to 1)
