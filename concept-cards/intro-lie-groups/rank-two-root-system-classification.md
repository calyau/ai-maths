---
# === CORE IDENTIFICATION ===
concept: Rank Two Root System Classification
slug: rank-two-root-system-classification

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
pdf_page: 93
section: "8.3. Pairs of roots and rank two root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rank 2 root systems"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - root-angles-and-length-ratios
extends: []
related:
  - root-system-type-a
  - root-system-type-b2
  - root-system-type-g2
  - classification-of-root-systems
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all rank two reduced root systems?"
  - "How do the rank two root systems differ?"
---

# Quick Definition
Every rank two reduced root system is isomorphic to exactly one of $A_1 \times A_1$, $A_2$, $B_2$, or $G_2$. These four types are distinguished by the maximal angle between roots: $\pi/2$, $2\pi/3$, $3\pi/4$, $5\pi/6$ respectively.

# Core Definition
Theorem 8.10 (p. 93): (1) The sets $A_1 \times A_1$, $A_2$, $B_2$, $G_2$ shown in Figure 8.1 are rank two root systems. (2) Any rank two reduced root system is isomorphic to one of these four.

The proof selects two roots $\alpha,\beta$ with maximal angle $\varphi$ (which forces $\varphi \geq \pi/2$). The four cases of Theorem 8.9 with $\varphi \geq \pi/2$ yield exactly $A_1 \times A_1$, $A_2$, $B_2$, $G_2$.

# Prerequisites
- **abstract-root-system** -- the objects being classified
- **root-angles-and-length-ratios** -- constrains relative positions of root pairs

# Key Properties
1. $A_1 \times A_1$: 4 roots, $\varphi = \pi/2$, all equal length, reducible
2. $A_2$: 6 roots, $\varphi_{\max} = 2\pi/3$, all equal length, irreducible
3. $B_2$: 8 roots, $\varphi_{\max} = 3\pi/4$, two length classes with ratio $\sqrt{2}$, irreducible
4. $G_2$: 12 roots, $\varphi_{\max} = 5\pi/6$, two length classes with ratio $\sqrt{3}$, irreducible

# Construction / Recognition
## To identify a rank two root system
1. Count the roots: 4 ($A_1 \times A_1$), 6 ($A_2$), 8 ($B_2$), 12 ($G_2$)
2. Alternatively: find the maximal angle between roots

# Context & Application
The rank two classification is the base case for the full classification of root systems. Each rank two type corresponds to an edge type in a Dynkin diagram: no edge ($A_1 \times A_1$), single edge ($A_2$), double edge ($B_2$), triple edge ($G_2$).

# Examples
**Example** (p. 93): Figure 8.1 shows the four rank two root systems geometrically in $\mathbb{R}^2$, displaying the root vectors and their symmetry.

# Relationships
## Builds Upon
- **root-angles-and-length-ratios** -- the allowed angle/length pairs

## Enables
- **dynkin-diagram** -- edge types correspond to rank two subsystems
- **classification-of-root-systems** -- rank two is the base case

## Related
- **root-system-type-a** -- $A_2$ is the simplest irreducible case
- **root-system-type-b2** -- the first non-simply-laced case

## Contrasts With
(none)

# Common Errors
- **Error**: Forgetting $A_1 \times A_1$ (the reducible case)
  **Correction**: There are four rank two types, not three; the orthogonal case is reducible but still a valid root system

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.3, pages 93--94. Theorem 8.10, Figure 8.1.

# Verification Notes
- Definition source: Direct from Theorem 8.10
- Confidence rationale: HIGH -- complete classification with explicit proof
- Uncertainties: None
- Cross-reference status: Verified
