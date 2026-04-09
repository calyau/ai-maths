---
# === CORE IDENTIFICATION ===
concept: Bracket Formula for Root Vectors
slug: bracket-ef-formula

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 86
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "[e,f] = (e,f)H_alpha"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - h-alpha
  - root-subspace
  - killing-form
extends: []
related:
  - sl2-subalgebra-of-root
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the bracket of root vectors in opposite root spaces?"
---

# Quick Definition

For $e \in \mathfrak{g}_\alpha$ and $f \in \mathfrak{g}_{-\alpha}$, the bracket $[e, f] = (e, f) H_\alpha$ lies in $\mathfrak{h}$ and is proportional to $H_\alpha$, with coefficient given by the Killing form pairing.

# Core Definition

**Lemma 7.18** (Kirillov, p. 86): Let $e \in \mathfrak{g}_\alpha$, $f \in \mathfrak{g}_{-\alpha}$. Then $[e, f] = (e, f) H_\alpha$.

# Prerequisites

- **$H_\alpha$** — The element of $\mathfrak{h}$ corresponding to $\alpha$
- **Root subspace** — $e$ and $f$ live in opposite root spaces
- **Killing form** — Provides the coefficient $(e, f)$

# Key Properties

1. Proved using invariance of the Killing form: $([e,f], h) = (e, [f,h]) = \langle h, \alpha \rangle (e, f) = (e, f)(h, H_\alpha)$
2. Non-degeneracy of $K|_\mathfrak{h}$ gives $[e, f] = (e, f) H_\alpha$
3. Since $K$ pairs $\mathfrak{g}_\alpha$ and $\mathfrak{g}_{-\alpha}$ non-degenerately, one can always find $e, f$ with $(e, f) \neq 0$

# Context & Application

This formula is the key computation connecting the Killing form geometry to the bracket structure. It shows that bracketing opposite root vectors always lands in $\mathfrak{h}$, with the result determined by the Killing form.

# Relationships

## Enables
- **sl(2) subalgebra of a root** — Choosing $(e, f) = 2/(\alpha, \alpha)$ gives $[e, f] = h_\alpha$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 86. Lemma 7.18.

# Verification Notes

- Definition source: Direct from Lemma 7.18
- Confidence rationale: Explicit lemma with short proof
- Uncertainties: None
- Cross-reference status: Verified
