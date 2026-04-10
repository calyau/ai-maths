---
concept: "Pólya's Theorem on Lattice Walks"
slug: polyas-theorem-lattice-walks
category: random-walks
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 307
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "Pólya's recurrence theorem"
prerequisites:
  - transient-random-walk
  - recurrent-random-walk
  - monotonicity-principle
extends: []
related:
  - effective-resistance
contrasts_with: []
answers_questions:
  - "What distinguishes recurrent from transient random walks?"
---

# Quick Definition
Pólya's theorem states that the simple random walk on the $d$-dimensional lattice $\mathbb{Z}^d$ is recurrent for $d = 1, 2$ and transient for $d \geq 3$.

# Core Definition
Theorem 14 (p. 307): "The simple random walk on the $d$-dimensional lattice $\mathbb{Z}^d$ is recurrent for $d = 1, 2$ and transient for $d \geq 3$." The proof uses the monotonicity principle: by the monotonicity principle, it suffices to show recurrence for $d = 2$ and transience for $d = 3$.

# Prerequisites
- **Transient random walk** — $\mathbb{Z}^d$ for $d \geq 3$
- **Recurrent random walk** — $\mathbb{Z}^d$ for $d \leq 2$
- **Monotonicity principle** — The key tool enabling the proof

# Key Properties
1. $\mathbb{Z}^1$ and $\mathbb{Z}^2$: recurrent (walk always returns)
2. $\mathbb{Z}^d$ for $d \geq 3$: transient (positive probability of never returning)
3. The dimension $d = 2$ is the critical case
4. Originally proved by Pólya in 1921; the electrical network proof is more elegant

# Construction / Recognition
## Proof Sketch (pp. 307-308)
**Recurrence of $\mathbb{Z}^2$**: Short all vertices at $\ell^\infty$-distance $n$ from the origin. The resulting network is a one-way path with resistance $1/(8n+4)$ at step $n$. Since $\sum 1/(8n+4) = \infty$, the resistance to infinity is infinite, so the walk is recurrent.

**Transience of $\mathbb{Z}^3$**: Construct a flow of size 1 from the origin in the positive octant with finite total energy (at most 1). By Theorem 13, the walk is transient.

# Context & Application
Pólya's theorem is "a striking application of Theorem 13" and "a classical theorem on random walks on lattices." The electrical network proof, based on the connection established in Section 2, is more elegant than Pólya's original 1921 proof. It illustrates the power of the monotonicity principle.

# Examples
**Example** (p. 308): For transience of $\mathbb{Z}^3$, define a flow in the positive octant: at vertex $(x_1, x_2, x_3)$ with $x_i \geq 0$ and $\sum x_i = n$, send current $2(x_i+1)/((n+1)(n+2)(n+3))$ to $(x_1, \ldots, x_i+1, \ldots, x_3)$. Total energy $\leq 1$.

# Relationships
## Builds Upon
- **transient-random-walk**, **recurrent-random-walk**, **monotonicity-principle**

## Enables
Understanding of random walks on more general graphs by comparison with lattices

# Common Errors
- **Error**: Thinking $d = 2$ is transient because the plane is "big."
  **Correction**: Despite the plane being infinite, the walk always returns in $\mathbb{Z}^2$. The critical threshold is $d = 3$.

# Source Reference
Chapter IX, Section IX.2, Theorem 14, pages 307-308.

# Verification Notes
- Definition source: Direct from Theorem 14
- Confidence rationale: Named classical theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
