---
# === CORE IDENTIFICATION ===
concept: Long and Short Roots
slug: long-and-short-roots

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 106
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-root-systems
extends: []
related:
  - simply-laced-root-system
  - dynkin-diagram
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are long and short roots?"
  - "Which root systems have two root lengths?"
---

# Quick Definition
In a non-simply-laced irreducible root system, roots come in exactly two lengths. The roots with the larger length are called long roots; the others are short roots. The length ratio is $\sqrt{2}$ for types $B$, $C$, $F_4$ and $\sqrt{3}$ for $G_2$.

# Core Definition
By Corollary 8.51 (p. 106), in a reduced irreducible root system, $(\alpha,\alpha)$ takes at most two values. The ratio $m = \max(\alpha,\alpha)/\min(\alpha,\alpha)$ equals the maximal edge multiplicity in the Dynkin diagram. For non-simply-laced systems, roots with larger $(\alpha,\alpha)$ are called long roots; the rest are called short roots.

# Prerequisites
- **classification-of-root-systems** -- the concept applies to classified types

# Key Properties
1. $m = 1$: all roots have equal length (simply laced: $A, D, E$)
2. $m = 2$: long/short ratio $\sqrt{2}$ (types $B, C, F_4$)
3. $m = 3$: long/short ratio $\sqrt{3}$ (type $G_2$ only)
4. In the Dynkin diagram, the arrow on a multiple edge points toward the shorter root
5. Each set of roots of a given length forms a single $W$-orbit (for irreducible $R$)

# Construction / Recognition
For a root $\alpha$ in a non-simply-laced irreducible root system: compute $(\alpha,\alpha)$ and compare with the maximum value. If $(\alpha,\alpha)$ is maximal, $\alpha$ is long; otherwise short.

# Context & Application
The distinction between long and short roots affects the Cartan matrix (since $a_{ij} = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$ depends on which root is in the denominator), the structure of the root lattice vs. weight lattice, and the representation theory.

# Examples
**Example**: In $B_2$, the 4 roots $\pm e_1 \pm e_2$ are long (length $\sqrt{2}$) and the 4 roots $\pm e_1, \pm e_2$ are short (length 1).

**Example**: In $G_2$, there are 6 long roots and 6 short roots with ratio $\sqrt{3}$.

# Relationships
## Builds Upon
- **classification-of-root-systems**

## Enables
- Understanding Cartan matrix asymmetry

## Related
- **simply-laced-root-system** -- has no distinction between long and short
- **dynkin-diagram** -- arrows indicate short roots

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking the arrow in a Dynkin diagram points to the long root
  **Correction**: The arrow points to the shorter root

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.8, page 106. Corollary 8.51.

# Verification Notes
- Definition source: Direct from Corollary 8.51
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
