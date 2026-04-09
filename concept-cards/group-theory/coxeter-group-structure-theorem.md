---
# === CORE IDENTIFICATION ===
concept: Structure Theorem for Coxeter Groups
slug: coxeter-group-structure-theorem

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: coxeter-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 39
section: "Coxeter groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Theorem 2.16

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coxeter-system
  - coxeter-group
  - reflection
extends: []
related:
  - coxeter-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Do the generators in a Coxeter system have the expected orders?"
  - "Is the natural map from S to a Coxeter group injective?"
---

# Quick Definition

In any Coxeter system $(G, S)$ defined by $m: S \times S \to \mathbb{N} \cup \{\infty\}$: (a) the map $S \to G$ is injective, (b) each $s \in S$ has order 2, and (c) each $st$ has order $m(s,t)$.

# Core Definition

"Let $(G, S)$ be the Coxeter system defined by a map $m$. (a) The natural map $S \to G$ is injective. (b) Each $s \in S$ has order 2 in $G$. (c) For each $s \neq t$ in $S$, $st$ has order $m(s,t)$ in $G$." (Milne, Theorem 2.16, p. 39)

# Prerequisites

- **Coxeter system** — the theorem describes properties of Coxeter systems
- **Coxeter group** — the theorem ensures the group has the expected structure
- **Reflection** — the proof constructs a reflection representation

# Key Properties

1. Generators remain distinct (no unexpected collapses)
2. Each generator has order exactly 2 (not 1)
3. Each product $st$ has order exactly $m(s,t)$ (not a proper divisor)
4. In other words, the relations in the Coxeter presentation are "tight" -- no unexpected additional relations hold

# Construction / Recognition

## Proof Strategy:
1. Part (b): define $\varepsilon: S \to \{\pm 1\}$ by $\varepsilon(s) = -1$; this extends to a homomorphism $G \to \{\pm 1\}$ (by 2.8), showing each $s$ has order 2
2. Parts (a,c): construct a vector space $V$ with basis $(e_s)_{s \in S}$ and a bilinear form $B$ with $B(e_s, e_t) = -\cos(\pi/m(s,t))$
3. Define "reflections" $\sigma_s(v) = v - 2B(v, e_s)e_s$
4. Show $\sigma_s\sigma_t$ has order $m(s,t)$ via the geometry of the bilinear form (Lemmas 2.17-2.18)
5. The map $s \mapsto \sigma_s$ extends to a homomorphism $G \to \mathrm{GL}(V)$, proving (a) and (c)

# Context & Application

This theorem is crucial: it guarantees that a Coxeter presentation actually produces a group with the intended structure. Without it, one might worry that the generators collapse or that products have smaller-than-expected orders.

# Examples

**Example 1** (p. 40): For $m(s,t) = n$ (rank 2): the reflections $\sigma_s, \sigma_t$ in a Euclidean plane with angle $\pi/n$ between their fixed lines generate $D_n$, and $\sigma_s\sigma_t$ is rotation by $2\pi/n$ (order $n$).

**Example 2** (p. 40): For $m(s,t) = \infty$: $\sigma_s\sigma_t$ has infinite order (computed explicitly via matrix powers).

# Relationships

## Builds Upon
- **coxeter-system**, **coxeter-group**, **reflection**

## Related
- **coxeter-matrix** — the theorem validates the matrix as determining the group

# Common Errors

- **Error**: Assuming generators might collapse in a Coxeter group
  **Correction**: Theorem 2.16 guarantees injectivity of $S \to G$ and correct orders

# Source Reference

Chapter 2, Theorem 2.16, Lemmas 2.17-2.18, Remark 2.19, pages 39-41.

# Verification Notes

- Definition source: Direct from Theorem 2.16
- Confidence: HIGH — explicit theorem with complete proof
- Uncertainties: None
