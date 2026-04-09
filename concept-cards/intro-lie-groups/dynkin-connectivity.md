---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram Connectivity
slug: dynkin-connectivity

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
pdf_page: 104
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "connected Dynkin diagram"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - dynkin-diagram
  - reducible-root-system
extends: []
related:
  - classification-of-root-systems
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a Dynkin diagram connected?"
  - "What does connectivity of the Dynkin diagram mean for the root system?"
---

# Quick Definition
A Dynkin diagram is connected if and only if the root system is irreducible. Disconnected components correspond to mutually orthogonal irreducible factors of the root system.

# Core Definition
**Theorem 8.48(1)** (p. 104): The Dynkin diagram is connected if and only if $R$ is irreducible.

If $R = R_1 \sqcup R_2$ with $R_1 \perp R_2$, then $\Pi = \Pi_1 \sqcup \Pi_2$ with $\Pi_1 \perp \Pi_2$ (Lemma 8.42), and the Dynkin diagram is the disjoint union of the diagrams for $\Pi_1$ and $\Pi_2$. The converse holds as well.

# Prerequisites
- **dynkin-diagram** -- the graph being analyzed
- **reducible-root-system** -- the algebraic property corresponding to disconnectedness

# Key Properties
1. Connected diagram $\Leftrightarrow$ irreducible root system
2. Components of a disconnected diagram correspond to irreducible factors
3. This reduces classification to connected diagrams

# Construction / Recognition
Check graph connectivity of the Dynkin diagram.

# Context & Application
This result reduces the classification of all root systems to classifying connected Dynkin diagrams, since every root system decomposes uniquely into irreducible components.

# Examples
**Example**: $A_1 \times A_1$ has two disconnected vertices (reducible). $A_2$ has two vertices connected by an edge (irreducible).

# Relationships
## Builds Upon
- **dynkin-diagram**, **reducible-root-system**

## Enables
- **classification-of-root-systems** -- reduces to connected diagrams

## Related
(none)

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 103--105. Theorem 8.48(1), Lemma 8.42.

# Verification Notes
- Definition source: Direct from Theorem 8.48(1)
- Confidence rationale: HIGH -- explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
