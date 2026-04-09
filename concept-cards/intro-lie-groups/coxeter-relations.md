---
# === CORE IDENTIFICATION ===
concept: Coxeter Relations
slug: coxeter-relations

# === CLASSIFICATION ===
category: root-systems
subcategory: weyl-group
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 109
section: "8.7. Simple reflections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "braid relations"
  - "Coxeter presentation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-reflections
  - weyl-group
  - root-angles-and-length-ratios
extends: []
related:
  - reduced-expression
  - dynkin-diagram
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the Coxeter relations for the Weyl group?"
  - "What are the braid relations?"
---

# Quick Definition
The Coxeter relations are the defining relations for the Weyl group in terms of simple reflections: $s_i^2 = 1$ and $(s_i s_j)^{m_{ij}} = 1$, where $m_{ij}$ is determined by the angle between $\alpha_i$ and $\alpha_j$.

# Core Definition
The Coxeter relations (Exercise 8.8, equation 8.32, p. 109) are:

$$s_i^2 = 1, \qquad (s_is_j)^{m_{ij}} = 1$$

where $m_{ij}$ depends on the angle $\varphi$ between $\alpha_i$ and $\alpha_j$: $\varphi = \pi - \pi/m_{ij}$. Explicitly:
- $m = 2$ for $A_1 \times A_1$ (orthogonal, no edge): $s_i s_j = s_j s_i$
- $m = 3$ for $A_2$ (single edge): $s_i s_j s_i = s_j s_i s_j$
- $m = 4$ for $B_2$ (double edge): $s_i s_j s_i s_j = s_j s_i s_j s_i$
- $m = 6$ for $G_2$ (triple edge): $(s_i s_j)^6 = 1$

These form a complete set of defining relations for $W$.

# Prerequisites
- **simple-reflections** -- the generators
- **weyl-group** -- the group being presented
- **root-angles-and-length-ratios** -- determine $m_{ij}$

# Key Properties
1. $s_i^2 = 1$ (reflections are involutions)
2. $m_{ij} = m_{ji}$ (the relation is symmetric)
3. $m_{ij}$ is read from the Dynkin diagram: no edge gives $m=2$, single edge $m=3$, double edge $m=4$, triple edge $m=6$
4. The Coxeter relations form a complete set of defining relations for $W$
5. The braid relation is $(s_is_j)^{m_{ij}} = 1$, equivalently $\underbrace{s_is_js_i\cdots}_{m_{ij}} = \underbrace{s_js_is_j\cdots}_{m_{ij}}$

# Construction / Recognition
Read $m_{ij}$ from the Dynkin diagram: the number of edges between vertices $i$ and $j$ determines $m_{ij}$ via $0 \to 2$, $1 \to 3$, $2 \to 4$, $3 \to 6$.

# Context & Application
The Coxeter presentation makes the Weyl group a Coxeter group, connecting root system theory to the theory of reflection groups. Braid relations are also the defining relations of the braid group (without $s_i^2 = 1$), which appears in knot theory and quantum groups.

# Examples
**Exercise 8.8** (p. 109): For rank two systems, the longest element is $w_0 = s_1s_2s_1\cdots = s_2s_1s_2\cdots$ ($m$ factors each), which encapsulates the braid relation.

# Relationships
## Builds Upon
- **simple-reflections** -- the generators
- **root-angles-and-length-ratios** -- determines $m_{ij}$

## Enables
- Complete algebraic description of $W$

## Related
- **dynkin-diagram** -- encodes the $m_{ij}$ values
- **reduced-expression** -- different reduced expressions related by Coxeter moves

## Contrasts With
(none)

# Common Errors
- **Error**: Using $m = 1$ for orthogonal roots (should be $m = 2$)
  **Correction**: Orthogonal simple roots give commuting reflections: $(s_is_j)^2 = 1$

# Common Confusions
- **Confusion**: Conflating Coxeter relations with Serre relations
  **Clarification**: Coxeter relations present the Weyl group; Serre relations present the Lie algebra

# Source Reference
Chapter 8: Root Systems, Section 8.7, page 109. Exercise 8.8, equation (8.32).

# Verification Notes
- Definition source: Direct from Exercise 8.8, equation (8.32)
- Confidence rationale: HIGH -- explicit formula with complete description
- Uncertainties: The source states (without proof) that these are a complete set of defining relations
- Cross-reference status: Verified
