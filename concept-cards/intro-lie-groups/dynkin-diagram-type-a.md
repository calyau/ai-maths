---
# === CORE IDENTIFICATION ===
concept: Dynkin Diagram of Type A_n
slug: dynkin-diagram-type-a

# === CLASSIFICATION ===
category: classification
subcategory: type-a
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 123
section: "C.1 A_n = sl(n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-a
  - dynkin-diagram
extends: []
related:
  - cartan-matrix-type-a
contrasts_with:
  - dynkin-diagram-type-b
  - dynkin-diagram-type-c
  - dynkin-diagram-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Dynkin diagram of type A_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The Dynkin diagram of $A_n$ is a chain of $n$ nodes connected by single edges: $\circ - \circ - \circ - \cdots - \circ$. All edges are single (no double or triple bonds), reflecting that $A_n$ is simply laced.

# Core Definition
(Kirillov, p. 123): The Dynkin diagram of $A_n$ consists of $n$ nodes in a line, each connected to its neighbors by a single edge.

# Prerequisites
- **Simple roots type A** -- the nodes correspond to simple roots
- **Dynkin diagram** -- general concept

# Key Properties
1. $n$ nodes, $n-1$ edges
2. All edges are single (simply laced -- all roots have equal length)
3. Linear (chain) shape -- no branching
4. Symmetry: the diagram has a $\mathbb{Z}_2$ automorphism ($\alpha_i \leftrightarrow \alpha_{n+1-i}$), corresponding to the outer automorphism of $\mathfrak{sl}(n+1, \mathbb{C})$

# Context & Application
The $A_n$ Dynkin diagram is the simplest among classical types. Its linear, simply-laced structure reflects the uniform nature of the root system where all roots have equal length. The diagram automorphism corresponds to the transpose-inverse outer automorphism of $\mathfrak{sl}(n+1, \mathbb{C})$.

# Examples
**Example** (p. 123): $A_1$: $\circ$ (single node). $A_2$: $\circ - \circ$. $A_3$: $\circ - \circ - \circ$.

# Relationships
## Contrasts With
- **Dynkin diagram type B** -- has a double edge at one end (with arrow)
- **Dynkin diagram type C** -- has a double edge at one end (with arrow in opposite direction)
- **Dynkin diagram type D** -- has a fork (branching) at one end

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Direct from p. 123 (diagram described)
- Confidence rationale: Standard diagram, explicitly given
- Uncertainties: None
- Cross-reference status: Verified
