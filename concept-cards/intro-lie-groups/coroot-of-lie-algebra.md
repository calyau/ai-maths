---
# === CORE IDENTIFICATION ===
concept: Coroot of a Lie Algebra Root
slug: coroot-of-lie-algebra

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 87
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "h_alpha"
  - "coroot element"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - h-alpha
  - root
extends:
  - h-alpha
related:
  - sl2-subalgebra-of-root
  - coroot
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the coroot h_alpha?"
  - "Why is the coroot normalization important?"
---

# Quick Definition

The coroot $h_\alpha = \frac{2H_\alpha}{(\alpha, \alpha)} \in \mathfrak{h}$ is the normalized version of $H_\alpha$ that satisfies $\langle h_\alpha, \alpha \rangle = 2$. Together with suitable $e \in \mathfrak{g}_\alpha$ and $f \in \mathfrak{g}_{-\alpha}$, it generates an $\mathfrak{sl}(2, \mathbb{C})$ subalgebra.

# Core Definition

**Lemma 7.19** (Kirillov, p. 87): Let $\alpha \in R$. Then $(\alpha, \alpha) \neq 0$. Define

$$h_\alpha = \frac{2H_\alpha}{(\alpha, \alpha)}.$$

Then $\langle h_\alpha, \alpha \rangle = 2$.

# Prerequisites

- **$H_\alpha$** — The un-normalized element
- **Root** — The root being "corooted"

# Key Properties

1. $\langle h_\alpha, \alpha \rangle = 2$
2. $\langle h_\alpha, \beta \rangle = \frac{2(\alpha, \beta)}{(\alpha, \alpha)} \in \mathbb{Z}$ for all $\beta \in R$ (Theorem 7.21)
3. Elements $h_\alpha$ span $\mathfrak{h}$ (Theorem 7.21)
4. The numbers $\langle h_\alpha, \beta \rangle$ are the entries of the Cartan matrix

# Context & Application

The coroot normalization $h_\alpha$ is chosen precisely so that $e, f, h_\alpha$ generate an $\mathfrak{sl}(2, \mathbb{C})$ subalgebra. This allows applying the complete theory of $\mathfrak{sl}(2)$ representations to study the structure of $\mathfrak{g}$.

# Examples

**Example**: For $\mathfrak{sl}(n, \mathbb{C})$ with root $\alpha = e_i - e_j$: $h_\alpha = E_{ii} - E_{jj}$.

# Relationships

## Builds Upon
- **$H_\alpha$** — Normalized version

## Enables
- **$\mathfrak{sl}(2)$ subalgebra of a root** — $e, f, h_\alpha$ generate $\mathfrak{sl}(2, \mathbb{C})_\alpha$

## Related
- **Coroot** — Abstract root system version

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 87. Lemma 7.19, equation (7.4).

# Verification Notes

- Definition source: Direct from Lemma 7.19
- Confidence rationale: Explicitly defined with key identity
- Uncertainties: None
- Cross-reference status: Verified
