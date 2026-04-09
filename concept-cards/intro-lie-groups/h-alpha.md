---
# === CORE IDENTIFICATION ===
concept: Element H_alpha
slug: h-alpha

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
  - "H_alpha"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - killing-form-on-h
  - root
extends: []
related:
  - coroot-of-lie-algebra
  - bracket-ef-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the element H_alpha associated to a root?"
---

# Quick Definition

For a root $\alpha$, the element $H_\alpha \in \mathfrak{h}$ is the image of $\alpha$ under the identification $\mathfrak{h}^* \cong \mathfrak{h}$ given by the Killing form. It satisfies $\langle H_\alpha, \beta \rangle = (\alpha, \beta)$ and appears in the bracket formula $[e, f] = (e, f) H_\alpha$.

# Core Definition

(Kirillov, p. 86): For $\alpha \in \mathfrak{h}^*$, denote by $H_\alpha$ the corresponding element of $\mathfrak{h}$ under the Killing form isomorphism. Then $(\alpha, \beta) = (H_\alpha, H_\beta) = \langle H_\alpha, \beta \rangle$.

**Lemma 7.18** (p. 86): For $e \in \mathfrak{g}_\alpha$, $f \in \mathfrak{g}_{-\alpha}$: $[e, f] = (e, f) H_\alpha$.

# Prerequisites

- **Killing form on $\mathfrak{h}$** — Provides the identification $\mathfrak{h}^* \cong \mathfrak{h}$
- **Root** — $H_\alpha$ is associated to a root

# Key Properties

1. $H_\alpha$ is characterized by $(H_\alpha, h) = \langle h, \alpha \rangle$ for all $h \in \mathfrak{h}$
2. $[e, f] = (e, f) H_\alpha$ for $e \in \mathfrak{g}_\alpha$, $f \in \mathfrak{g}_{-\alpha}$ (Lemma 7.18)
3. $(\alpha, \alpha) = (H_\alpha, H_\alpha) \neq 0$ (Lemma 7.19)
4. The coroot is $h_\alpha = \frac{2H_\alpha}{(\alpha, \alpha)}$

# Context & Application

$H_\alpha$ is the "natural" element of $\mathfrak{h}$ associated to a root. The normalized version $h_\alpha = 2H_\alpha/(\alpha, \alpha)$ is the coroot, which gives integer pairings with all roots.

# Examples

**Example**: For $\mathfrak{sl}(2, \mathbb{C})$ with root $\alpha$: $H_\alpha$ is proportional to $h = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, and the coroot $h_\alpha = h$.

# Relationships

## Enables
- **Coroot of Lie algebra** — $h_\alpha = 2H_\alpha/(\alpha, \alpha)$
- **Bracket formula** — $[e, f] = (e, f)H_\alpha$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 86-87. Lemma 7.18, Lemma 7.19.

# Verification Notes

- Definition source: Direct from p. 86
- Confidence rationale: Explicitly defined with key properties
- Uncertainties: None
- Cross-reference status: Verified
