---
# === CORE IDENTIFICATION ===
concept: Harmonic Function on a Graph
slug: harmonic-function-on-graph

# === CLASSIFICATION ===
category: electrical-networks
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 302
section: "IX.2 Electrical Networks and Random Walks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "discrete harmonic function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-walk-on-graph
extends: []
related:
  - effective-resistance
  - escape-probability
  - absolute-potential
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
  - "What connects potentials in electrical networks to random walk probabilities?"
---

# Quick Definition
A function $f: V(G) \to \mathbb{R}$ is harmonic on $G$ with boundary $S \subset V(G)$ if, for every $x \notin S$ with $d(x) \geq 1$, the value $f(x)$ equals the average of $f$ over the neighbours of $x$.

# Core Definition
Given a pair $(G, S)$ where $G$ is a simple graph and $S \subset V(G)$, a function $f: V(G) \to \mathbb{R}$ is harmonic on $G$ with boundary $S$ if $f(x) = \frac{1}{d(x)} \sum_{y \in \Gamma(x)} f(y)$ whenever $x \in V(G) \setminus S$ and $d(x) \geq 1$ (Bollobás, p. 302). "Harmonic functions are of central importance in the theory of electrical networks" and arise naturally in random walks.

# Prerequisites
- **Random walk on a graph** — Harmonic functions arise as expected values of random walk quantities

# Key Properties
1. The averaging property: $f(x)$ is the mean of $f$ over neighbours of $x$, for $x \notin S$
2. Absolute potentials in an electrical network with outlets $s_1, \ldots, s_k$ form a harmonic function with boundary $\{s_1, \ldots, s_k\}$
3. Expected gains in a random walk game yield harmonic functions
4. Maximum modulus principle: the maximum of a non-constant harmonic function is attained on the boundary $S$
5. Superposition principle: linear combinations of harmonic functions are harmonic
6. Uniqueness: for given boundary values, the harmonic function is unique

# Construction / Recognition
## To Construct a Harmonic Function
1. Fix boundary set $S$ and boundary values $g: S \to \mathbb{R}$
2. For each $x \in V(G)$, run a random walk from $x$, stopping at $S$
3. Set $f(x) = \mathbb{E}_x(g(X_{\tau_S}))$, the expected boundary value upon stopping
4. Verify: $f(x) = g(x)$ for $x \in S$ and $f$ satisfies the averaging property elsewhere

# Context & Application
Harmonic functions are the key bridge between electrical networks and random walks. The absolute potential $V_x$ in an electrical network satisfies the same averaging property as the expected hitting probability in a random walk. This "intimate connection greatly benefits both areas" (p. 300): electrical network results yield random walk theorems, and vice versa.

# Examples
**Example** (p. 303): Let $V_x = \mathbb{P}(\text{starting at } x, \text{ we get to } s \text{ before } t)$. Then $V_s = 1$, $V_t = 0$, and $V_x$ is harmonic with boundary $\{s, t\}$. This is precisely the distribution of absolute potentials when $s$ is set at 1 and $t$ at 0.

# Relationships
## Builds Upon
- **random-walk-on-graph** — Expected values under random walks produce harmonic functions

## Enables
- **escape-probability** — Expressed via harmonic functions
- **effective-resistance** — Connected through harmonic functions/potentials

## Related
- **absolute-potential** — Potentials in electrical networks are harmonic

# Common Errors
- **Error**: Forgetting that the harmonic property holds only at non-boundary vertices.
  **Correction**: At boundary vertices $x \in S$, the function value is prescribed, not averaged.

# Common Confusions
- **Confusion**: Thinking discrete harmonic functions are unrelated to classical harmonic functions.
  **Clarification**: The discrete averaging property is the exact analogue of the mean value property of classical harmonic functions, and the connection extends to Dirichlet problems and potential theory.

# Source Reference
Chapter IX: Random Walks on Graphs, Section IX.2, pages 302-303. See also Exercise 7.

# Verification Notes
- Definition source: Direct from p. 302, equation (8)
- Confidence rationale: Explicit definition with equation number
- Uncertainties: None
- Cross-reference status: Verified
