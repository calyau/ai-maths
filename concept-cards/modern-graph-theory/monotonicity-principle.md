---
concept: Monotonicity Principle
slug: monotonicity-principle
category: electrical-networks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 301
section: "IX.1 Electrical Networks Revisited"
extraction_confidence: high
aliases:
  - "Rayleigh's monotonicity law"
prerequisites:
  - effective-resistance
  - thomsons-principle
  - dirichlets-principle
extends: []
related:
  - recurrent-random-walk
  - transient-random-walk
  - polyas-theorem-lattice-walks
contrasts_with: []
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
The monotonicity principle states that increasing the resistance of any wire (or cutting it) does not decrease the effective resistance between any two vertices, and shorting two vertices does not increase the effective resistance.

# Core Definition
Corollary 7 (p. 301): "If the resistance of a wire is increased then the effective resistance (between two vertices) does not decrease. In particular, if a wire is cut, the effective resistance does not decrease, and if two vertices are shorted, the effective resistance does not increase."

# Prerequisites
- **Effective resistance** — The quantity that is monotone
- **Thomson's principle** — One way to prove the monotonicity principle
- **Dirichlet's principle** — Alternative proof route

# Key Properties
1. Cutting an edge: $R_{\text{eff}}$ does not decrease
2. Shorting two vertices: $R_{\text{eff}}$ does not increase
3. Increasing any edge resistance: $R_{\text{eff}}$ does not decrease
4. For random walks: cutting edges helps prove transience; shorting vertices helps prove recurrence

# Construction / Recognition
## To Apply the Monotonicity Principle
1. To show $R_{\text{eff}}$ is large (recurrence): short vertices to simplify the network, then compute
2. To show $R_{\text{eff}}$ is small (transience): cut edges to simplify, then compute
3. Both operations can only move $R_{\text{eff}}$ in the indicated direction

# Context & Application
The monotonicity principle is "the Holy Grail of this section" (p. 301). It is used crucially in Pólya's theorem on lattice walks: shorting vertices of $\mathbb{Z}^2$ proves recurrence, while cutting edges of $\mathbb{Z}^3$ proves transience. It provides the key technique for comparing random walks on different graphs.

# Examples
**Example** (p. 307-308): To prove the SRW on $\mathbb{Z}^2$ is recurrent, short all vertices at distance $n$ from the origin. The resulting network is a one-way infinite path with resistance $1/(8n+4)$ at step $n$; since $\sum 1/(8n+4) = \infty$, the effective resistance to $\infty$ is infinite.

# Relationships
## Builds Upon
- **effective-resistance**, **thomsons-principle**, **dirichlets-principle**

## Enables
- **polyas-theorem-lattice-walks** — Key tool in the proof
- **transient-random-walk** — Cutting edges to prove transience
- **recurrent-random-walk** — Shorting vertices to prove recurrence

# Common Errors
- **Error**: Applying monotonicity in the wrong direction (e.g., claiming cutting decreases resistance).
  **Correction**: Cutting (increasing resistance to $\infty$) always increases or preserves effective resistance.

# Common Confusions
- **Confusion**: Thinking the monotonicity principle is physically obvious and needs no proof.
  **Clarification**: As Bollobás notes, "from Kirchhoff's theorem it is not easy to show that if a wire is cut then the total resistance does not decrease" (p. 297). The energy-minimization approach is needed.

# Source Reference
Chapter IX, Section IX.1, Corollary 7, page 301.

# Verification Notes
- Definition source: Direct quote from Corollary 7, p. 301
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
