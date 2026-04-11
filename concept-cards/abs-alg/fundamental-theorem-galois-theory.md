---
concept: Fundamental Theorem of Galois Theory
slug: fundamental-theorem-galois-theory
category: galois-theory
subcategory: fundamental-theorem
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 574
section: "14.2 The Fundamental Theorem of Galois Theory"
extraction_confidence: high
aliases:
  - "FTGT"
  - "Galois correspondence"
prerequisites:
  - galois-extension
  - galois-group
  - fixed-field
extends: []
related:
  - galois-correspondence
  - normal-extension
contrasts_with: []
answers_questions:
  - "How does the Fundamental Theorem of Galois Theory connect subgroups and intermediate fields?"
---

# Quick Definition
The Fundamental Theorem establishes an inclusion-reversing bijection between intermediate fields of a Galois extension K/F and subgroups of $\text{Gal}(K/F)$: subfield $E \leftrightarrow \text{Gal}(K/E)$. Normal subgroups correspond to Galois intermediate extensions.

# Core Definition
(Theorem, pp. 574-577) Let K/F be a Galois extension with Galois group $G = \text{Gal}(K/F)$. Then:
1. There is an inclusion-reversing bijection $\{$intermediate fields $F \subseteq E \subseteq K\} \leftrightarrow \{$subgroups $H \leq G\}$ given by $E \mapsto \text{Gal}(K/E)$ and $H \mapsto K^H$ (fixed field of H).
2. $[K:E] = |\text{Gal}(K/E)|$ and $[E:F] = [G:\text{Gal}(K/E)]$.
3. $E/F$ is normal (hence Galois) $\iff$ $\text{Gal}(K/E) \trianglelefteq G$, and then $\text{Gal}(E/F) \cong G/\text{Gal}(K/E)$.
(Dummit & Foote, pp. 574-577)

# Prerequisites
- **galois-extension** — The theorem applies to Galois extensions
- **galois-group** — Subgroups of the Galois group correspond to intermediate fields
- **fixed-field** — The fixed field of a subgroup is an intermediate field

# Key Properties
1. The correspondence is inclusion-reversing: bigger subgroup $\leftrightarrow$ smaller field
2. Index of subgroup = degree of corresponding field over F
3. Normal subgroups $\leftrightarrow$ normal (Galois) extensions of F
4. The quotient group gives the Galois group of the intermediate extension
5. Lattice of subgroups is isomorphic to the (upside-down) lattice of intermediate fields

# Construction / Recognition
## To Apply:
1. Verify K/F is Galois (splitting field of a separable polynomial)
2. Compute $G = \text{Gal}(K/F)$
3. Find all subgroups of G
4. Each subgroup H gives an intermediate field $K^H$
5. Compute $K^H$ by finding elements of K fixed by all $\sigma \in H$

# Context & Application
This is one of the most beautiful theorems in mathematics, reducing questions about field extensions to questions about group theory. It is the key tool for analyzing solvability by radicals and constructibility.

# Examples
**Example** (p. 578): For $K = \mathbb{Q}(\sqrt{2}, \sqrt{3})$ over $\mathbb{Q}$, $\text{Gal}(K/\mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ with three non-trivial intermediate fields $\mathbb{Q}(\sqrt{2}), \mathbb{Q}(\sqrt{3}), \mathbb{Q}(\sqrt{6})$ corresponding to the three subgroups of order 2.

# Relationships
## Builds Upon
- **galois-extension**, **galois-group**, **fixed-field**

## Enables
- Analysis of solvability by radicals
- Classification of constructible numbers
- Computation of Galois groups

# Source Reference
Chapter 14, Section 14.2, pp. 574-580.

# Verification Notes
- Confidence: HIGH — the central theorem of the chapter with full proof
