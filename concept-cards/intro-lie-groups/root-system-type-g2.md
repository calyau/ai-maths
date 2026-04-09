---
# === CORE IDENTIFICATION ===
concept: Root System Type G2
slug: root-system-type-g2

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
  - "$G_2$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - rank-two-root-system-classification
extends: []
related:
  - root-system-type-b2
  - long-and-short-roots
  - exceptional-root-systems
contrasts_with:
  - root-system-type-a
  - root-system-type-b2

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the $G_2$ root system?"
---

# Quick Definition
$G_2$ is the rank two root system with 12 roots and two root lengths in ratio $\sqrt{3}$, with maximal angle $5\pi/6$ between roots. It is the largest rank two root system and one of the five exceptional types.

# Core Definition
$G_2$ is one of the four rank two reduced root systems (Theorem 8.10, p. 93). It has 12 roots: 6 long and 6 short, with length ratio $\sqrt{3}$. The maximal angle between a pair of non-proportional roots is $5\pi/6$. Its Dynkin diagram is two vertices connected by a triple edge with an arrow pointing to the short root.

# Prerequisites
- **abstract-root-system** -- $G_2$ is a root system
- **rank-two-root-system-classification** -- $G_2$ is one of the four rank two types

# Key Properties
1. 12 roots total: 6 long and 6 short
2. Length ratio: $|\alpha_{\text{long}}|/|\alpha_{\text{short}}| = \sqrt{3}$
3. Maximal angle: $5\pi/6$
4. $|W(G_2)| = 12$ (the dihedral group of order 12)
5. Dynkin diagram: triple edge with arrow
6. $G_2$ is an exceptional root system (not part of any infinite classical series)

# Construction / Recognition
$G_2$ can be recognized as the rank two root system with the most roots (12) or equivalently the smallest angular separation between adjacent roots ($\pi/6$).

# Context & Application
$G_2$ corresponds to the triple edge in a Dynkin diagram and to one of the five exceptional simple Lie algebras. It is the only exceptional type of rank 2 and appears in the classification as one of the two exceptional types with a multiple edge ($F_4$ being the other).

# Examples
**Example** (p. 93): $G_2$ is shown in Figure 8.1. The Weyl group has $m = 6$ for the braid relation (Exercise 8.8), reflecting the 12 Weyl chambers.

# Relationships
## Builds Upon
- **rank-two-root-system-classification**

## Enables
- **dynkin-diagram** -- the triple edge corresponds to $G_2$

## Related
- **exceptional-root-systems** -- $G_2$ is an exceptional type
- **long-and-short-roots** -- $G_2$ has the largest length ratio

## Contrasts With
- **root-system-type-a** -- simply laced, equal root lengths
- **root-system-type-b2** -- double edge, length ratio $\sqrt{2}$

# Common Errors
- **Error**: Confusing $G_2$ with the group $GL(2)$
  **Correction**: $G_2$ refers to the specific exceptional root system/Lie algebra

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.3, pages 93--94. Theorem 8.10, Figure 8.1.

# Verification Notes
- Definition source: Direct from Theorem 8.10
- Confidence rationale: HIGH -- explicit in classification
- Uncertainties: Explicit coordinates not given in this section (deferred to Appendix C)
- Cross-reference status: Verified
