---
# === CORE IDENTIFICATION ===
concept: Thomson's Principle
slug: thomsons-principle

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
pdf_page: 299
section: "IX.1 Electrical Networks Revisited"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - energy-in-electrical-network
extends: []
related:
  - dirichlets-principle
  - rayleighs-principle
  - monotonicity-principle
contrasts_with:
  - dirichlets-principle

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do electrical networks relate to random walks on graphs?"
---

# Quick Definition
Thomson's principle states that the electric currents in a network are distributed so as to minimize the total energy, among all flows satisfying Kirchhoff's current law with given sources and sinks.

# Core Definition
Given an electrical network $N = (G, r)$ with outlets $s_1, \ldots, s_k$ and prescribed currents $u_{s_i}$ entering at each outlet (with $\sum u_{s_i} = 0$), consider the energy function $E(u) = \sum_{xy \in E(G)} u_{xy}^2 r_{xy}$ over flows $u = (u_{xy})$ satisfying KCL. Thomson's principle (Theorem 2, p. 300) states there is a flow minimizing $E(u)$, and this flow satisfies KPL, making it the proper electric current. The minimum of $E(u)$ equals the total energy.

# Prerequisites
- **Energy in an electrical network** — Thomson's principle minimizes energy

# Key Properties
1. Among all flows satisfying KCL with given outlets, the proper current minimizes total energy
2. At the minimum, KPL is automatically satisfied
3. The proof uses compactness and differentiation with respect to cycle perturbations
4. Combined with Corollary 4, gives the expression for effective resistance (Corollary 6)

# Construction / Recognition
## To Apply Thomson's Principle
1. Fix source/sink currents satisfying $\sum u_{s_i} = 0$
2. Among all flows obeying KCL at non-outlet vertices, find the one minimizing $\sum u_{xy}^2 r_{xy}$
3. This minimizing flow is the actual electric current; it automatically satisfies KPL

# Context & Application
Thomson's principle is one of two energy-minimization approaches (the other being Dirichlet's principle). It is the "flow approach": fix KCL, minimize energy to get KPL. This is crucial for proving the monotonicity principle and for bounding effective resistances.

# Examples
**Example** (p. 300): For a unit current from $s$ to $t$, the effective resistance $R_{\text{eff}}(s,t) = \inf\{\sum u_{xy}^2 r_{xy}\}$ over all $s$-$t$ flows of size 1 (Corollary 6).

# Relationships
## Builds Upon
- **energy-in-electrical-network** — The quantity being minimized

## Enables
- **monotonicity-principle** — Follows from Thomson's principle
- **effective-resistance** — Expressed as minimum energy of unit flow

## Contrasts With
- **dirichlets-principle** — Minimizes over potentials rather than flows

# Common Errors
- **Error**: Applying Thomson's principle without fixing the source/sink currents.
  **Correction**: The outlet currents must be prescribed; the minimization is over flows with those fixed outlet values.

# Common Confusions
- **Confusion**: Confusing Thomson's principle with Dirichlet's principle.
  **Clarification**: Thomson's starts from KCL (flows) and recovers KPL; Dirichlet's starts from KPL (potentials) and recovers KCL.

# Source Reference
Chapter IX: Random Walks on Graphs, Section IX.1, Theorem 2, pages 299-300.

# Verification Notes
- Definition source: Direct from Theorem 2, p. 300
- Confidence rationale: Named theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
