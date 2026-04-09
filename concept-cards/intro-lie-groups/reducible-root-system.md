---
# === CORE IDENTIFICATION ===
concept: Reducible and Irreducible Root Systems
slug: reducible-root-system

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
pdf_page: 103
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "irreducible root system"
  - "decomposable root system"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
extends: []
related:
  - dynkin-diagram
  - reduced-root-system
contrasts_with:
  - reduced-root-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reducible root system?"
  - "What is an irreducible root system?"
  - "How does reducibility relate to the Dynkin diagram?"
---

# Quick Definition
A root system is reducible if it can be decomposed as $R = R_1 \sqcup R_2$ with $R_1 \perp R_2$; otherwise it is irreducible. Reducibility corresponds to a disconnected Dynkin diagram, and every root system decomposes uniquely into irreducible components.

# Core Definition
A root system $R$ is called reducible if it can be written as $R = R_1 \sqcup R_2$ with $R_1 \perp R_2$ (Definition 8.40, p. 103). Otherwise, $R$ is irreducible.

By Lemma 8.42 (p. 103): $R$ is reducible iff $\Pi = \Pi_1 \sqcup \Pi_2$ with $\Pi_1 \perp \Pi_2$.

By Theorem 8.48(1): the Dynkin diagram is connected iff $R$ is irreducible.

# Prerequisites
- **abstract-root-system** -- the object being decomposed

# Key Properties
1. $R$ is reducible iff $\Pi$ splits into mutually orthogonal subsets (Lemma 8.42)
2. $R$ is irreducible iff its Dynkin diagram is connected (Theorem 8.48(1))
3. Every root system decomposes uniquely as $R_1 \sqcup \cdots \sqcup R_n$ with $R_i$ irreducible and mutually orthogonal (p. 103)
4. If $R = R_1 \sqcup R_2$, then $W = W_1 \times W_2$ (Lemma 8.42)

# Construction / Recognition
Check whether the Dynkin diagram is connected. If yes, irreducible. If no, the connected components give the irreducible factors.

# Context & Application
The classification of root systems reduces to classifying irreducible ones (i.e., connected Dynkin diagrams). Every reducible root system is a direct sum of irreducible components.

**Remark 8.41** (p. 103): "Reducible" (decomposable into orthogonal parts) is completely unrelated to "reduced" (no proportional roots). The terminology is unfortunate but standard.

# Examples
**Example** (p. 103): $A_1 \times A_1$ (two orthogonal copies of $A_1$) is reducible. $A_2$, $B_2$, $G_2$ are irreducible.

# Relationships
## Builds Upon
- **abstract-root-system**

## Enables
- **classification-of-root-systems** -- reduces to irreducible case

## Related
- **dynkin-diagram** -- connected iff irreducible

## Contrasts With
- **reduced-root-system** -- completely different concept despite similar name (Remark 8.41)

# Common Errors
(none)

# Common Confusions
- **Confusion**: Confusing "reducible" with "reduced"
  **Clarification**: "Reduced" means no root is a nontrivial multiple of another (R4); "reducible" means decomposable into orthogonal parts. They are independent properties (Remark 8.41).

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 103--104. Definition 8.40, Remark 8.41, Lemma 8.42, Theorem 8.48(1).

# Verification Notes
- Definition source: Direct from Definition 8.40
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
