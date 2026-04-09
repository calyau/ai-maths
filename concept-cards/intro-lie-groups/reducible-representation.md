---
# === CORE IDENTIFICATION ===
concept: Reducible Representation
slug: reducible-representation

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 41
section: "4.3 Irreducible representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subrepresentation
extends: []
related:
  - completely-reducible-representation
contrasts_with:
  - irreducible-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reducible representation?"
---

# Quick Definition

A representation $V$ is reducible if it has a non-trivial subrepresentation (i.e., a subrepresentation $W$ with $0 \neq W \neq V$). A reducible representation may or may not be completely reducible.

# Core Definition

**Definition 4.15** (Kirillov, p. 41): If a representation is not irreducible, it is called reducible.

A reducible representation $V$ has a non-trivial subrepresentation $W$, yielding a short exact sequence $0 \to W \to V \to V/W \to 0$. The question is whether this sequence splits.

# Prerequisites

- **Subrepresentation** — A reducible representation has a proper non-zero subrepresentation

# Key Properties

1. A reducible representation contains a proper non-zero invariant subspace
2. It may or may not decompose as a direct sum (it is completely reducible iff it does)
3. For compact groups and finite groups: reducible implies completely reducible

# Examples

**Example 4.18** (p. 42): The representation of $\mathbb{R}$ given by $t \mapsto \exp(tA)$ where $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is reducible (the span of $e_1$ is invariant) but not completely reducible (there is no complementary invariant subspace).

# Relationships

## Contrasts With
- **Irreducible representation** — Has no non-trivial subrepresentation

## Related
- **Completely reducible representation** — A reducible representation that splits as a direct sum

# Source Reference

Chapter 4, Section 4.3, Definition 4.15, Example 4.18, pp. 41-42.

# Verification Notes

- Definition source: Direct from Definition 4.15
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
