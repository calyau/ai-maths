---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram of Type D_n
slug: dynkin-diagram-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 128
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-d
  - dynkin-diagram
extends: []
related:
  - cartan-matrix-type-d
contrasts_with:
  - dynkin-diagram-type-a
  - dynkin-diagram-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Dynkin diagram of type D_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The Dynkin diagram of $D_n$ is a chain of $n-2$ nodes followed by a fork: the $(n-2)$-th node connects to two terminal nodes. All edges are single (simply laced). The fork reflects that $\alpha_{n-1}$ and $\alpha_n$ are both adjacent to $\alpha_{n-2}$ but not to each other.

# Core Definition
(Kirillov, p. 128): The Dynkin diagram has $n$ nodes. Nodes $1$ through $n-2$ form a chain, and node $n-2$ connects to both node $n-1$ and node $n$ (which are not connected to each other).

# Prerequisites
- **Simple roots type D** -- nodes correspond to simple roots
- **Dynkin diagram** -- general concept

# Key Properties
1. All edges single (simply laced)
2. Fork at one end: node $n-2$ has degree 3
3. For $n = 4$ ($D_4$): the diagram has a central node connected to three others (triality)
4. $D_n$ diagram has a $\mathbb{Z}_2$ symmetry swapping $\alpha_{n-1} \leftrightarrow \alpha_n$

# Examples
**Example** (p. 128): $D_4$: star-shaped with one central node and three leaves (unique among Dynkin diagrams for having an $S_3$ symmetry group -- triality).

# Relationships
## Contrasts With
- **Dynkin diagram type A** -- linear chain, no fork
- **Dynkin diagram type B** -- double bond instead of fork

# Source Reference
Appendix C, Section C.4, p. 128.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Standard diagram
- Uncertainties: None
- Cross-reference status: Verified
