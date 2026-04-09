---
# === CORE IDENTIFICATION ===
concept: Classical Root Systems
slug: classical-root-systems

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 105
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "types A, B, C, D"
  - "classical types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-root-systems
  - dynkin-diagram
extends: []
related:
  - root-system-type-a
  - exceptional-root-systems
contrasts_with:
  - exceptional-root-systems

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the classical root systems?"
  - "Which Lie algebras correspond to classical root systems?"
---

# Quick Definition
The classical root systems are the four infinite families in the classification: $A_n$ ($n \geq 1$), $B_n$ ($n \geq 2$), $C_n$ ($n \geq 2$), and $D_n$ ($n \geq 4$). They correspond to the classical matrix Lie algebras $\mathfrak{sl}$, $\mathfrak{so}$, and $\mathfrak{sp}$.

# Core Definition
The classical types in Theorem 8.49 are (p. 105):

- **$A_n$** ($n \geq 1$): Dynkin diagram is a chain of $n$ vertices with single edges. Corresponds to $\mathfrak{sl}(n+1,\mathbb{C})$.
- **$B_n$** ($n \geq 2$): Chain with a double edge (with arrow) at one end. Corresponds to $\mathfrak{so}(2n+1,\mathbb{C})$.
- **$C_n$** ($n \geq 2$): Chain with a double edge (with arrow) at one end (reversed from $B_n$). Corresponds to $\mathfrak{sp}(2n,\mathbb{C})$.
- **$D_n$** ($n \geq 4$): Chain with a fork at one end. Corresponds to $\mathfrak{so}(2n,\mathbb{C})$.

# Prerequisites
- **classification-of-root-systems** -- classical types are part of the classification
- **dynkin-diagram** -- each type is specified by its diagram

# Key Properties
1. $A_n$ is simply laced (all roots equal length)
2. $B_n$ has two root lengths with ratio $\sqrt{2}$
3. $C_n$ has two root lengths with ratio $\sqrt{2}$ (same ratio as $B_n$ but reversed roles)
4. $D_n$ is simply laced
5. Low-rank coincidences: $B_1 = C_1 = A_1$, $B_2 = C_2$, $D_2 = A_1 \times A_1$, $D_3 = A_3$

# Construction / Recognition
Explicit constructions of all classical root systems are in Appendix C. The subscript always equals the rank.

# Context & Application
Classical root systems account for all but five of the irreducible root systems. They correspond to the "familiar" matrix Lie algebras and their representations are well-studied via classical linear algebra methods.

# Examples
**Example** (p. 106): $A_n$ corresponds to $\mathfrak{sl}(n+1,\mathbb{C})$. The $B_n$, $C_n$, $D_n$ series correspond to $\mathfrak{so}$ and $\mathfrak{sp}$ (detailed in Appendix C).

# Relationships
## Builds Upon
- **classification-of-root-systems**

## Enables
- Classical representation theory

## Related
- **root-system-type-a** -- the $A$ family

## Contrasts With
- **exceptional-root-systems** -- the five sporadic types

# Common Errors
- **Error**: Confusing $B_n$ and $C_n$ diagrams (the arrow direction differs)
  **Correction**: In $B_n$ the arrow points to the short root at the end; in $C_n$ the arrow points to the short root at the end, but the long/short assignment is reversed

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 105--106. Theorem 8.49, Remark 8.50.

# Verification Notes
- Definition source: Direct from Theorem 8.49
- Confidence rationale: HIGH -- explicit classification list
- Uncertainties: Detailed constructions deferred to Appendix C
- Cross-reference status: Verified
