---
concept: Finite Energy Flow Criterion for Transience
slug: finite-energy-flow-criterion
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
  - "Theorem 13"
prerequisites:
  - transient-random-walk
  - recurrent-random-walk
  - effective-resistance-to-infinity
extends: []
related:
  - polyas-theorem-lattice-walks
  - monotonicity-principle
contrasts_with: []
answers_questions:
  - "What distinguishes recurrent from transient random walks?"
---

# Quick Definition
Theorem 13 gives a practical criterion: the RW is transient iff there exists a flow of finite energy in which positive current enters at some vertex; it is recurrent iff for every $\varepsilon > 0$ there exists a finitely-supported potential function with value $\geq 1$ at some vertex and total energy $< \varepsilon$.

# Core Definition
Theorem 13 (p. 308): The RW is transient iff there is a flow $(u_{xy})$ with finite energy $\sum u_{xy}^2 r_{xy}$ where no current leaves at any vertex but positive current enters at some vertex. Recurrent iff for every $\varepsilon > 0$, there is $(V_x)$ with $V_s \geq 1$ for some $s$, $V_x = 0$ for all but finitely many $x$, and $\sum (V_x - V_y)^2 c_{xy} < \varepsilon$.

# Prerequisites
- **Transient random walk**, **recurrent random walk**, **effective-resistance-to-infinity**

# Key Properties
1. Transience: construct a finite-energy unit flow to infinity
2. Recurrence: construct potentials with arbitrarily small energy
3. Monotonicity corollary: in proving transience, cut edges; in proving recurrence, short vertices

# Relationships
## Builds Upon
- **transient-random-walk**, **recurrent-random-walk**, **effective-resistance-to-infinity**

## Enables
- **polyas-theorem-lattice-walks** — Key tool in the proof

# Source Reference
Chapter IX, Section IX.2, Theorem 13, pages 307-308.

# Verification Notes
- Definition source: Direct from Theorem 13
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
