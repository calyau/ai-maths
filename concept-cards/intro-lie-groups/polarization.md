---
# === CORE IDENTIFICATION ===
concept: Polarization of Root System
slug: polarization

# === CLASSIFICATION ===
category: root-systems
subcategory: simple-positive-roots
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 94
section: "8.4. Positive roots and simple roots"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "choice of positive roots"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
extends: []
related:
  - positive-roots
  - simple-roots
  - weyl-chamber
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a polarization of a root system?"
  - "How do different polarizations relate?"
---

# Quick Definition
A polarization of a root system $R$ is a decomposition $R = R_+ \sqcup R_-$ into positive and negative roots, determined by a regular element $t \in E$ (one with $(t,\alpha) \neq 0$ for all $\alpha \in R$).

# Core Definition
Let $t \in E$ be such that $(t,\alpha) \neq 0$ for every root $\alpha$ (such $t$ are called regular). Then the decomposition $R = R_+ \sqcup R_-$ where $R_+ = \{\alpha \in R \mid (\alpha,t) > 0\}$ and $R_- = \{\alpha \in R \mid (\alpha,t) < 0\}$ is called a polarization of $R$ (equation 8.6, p. 94).

The polarization depends on the choice of $t$ but is constant within each connected component of the complement to root hyperplanes (i.e., within each Weyl chamber). Different polarizations yield Weyl-conjugate sets of simple roots (Corollary 8.29).

# Prerequisites
- **abstract-root-system** -- the root system being decomposed

# Key Properties
1. $R_- = -R_+$ (if $\alpha \in R_+$ then $-\alpha \in R_-$)
2. The polarization depends only on which Weyl chamber $t$ lies in (Lemma 8.24)
3. There is a bijection between polarizations and Weyl chambers (Lemma 8.24)
4. Different polarizations give Weyl-conjugate simple root systems (Corollary 8.29)

# Construction / Recognition
1. Choose any $t \in E$ with $(t,\alpha) \neq 0$ for all $\alpha \in R$
2. Define $R_+ = \{\alpha \in R \mid (\alpha,t) > 0\}$, $R_- = \{\alpha \mid (\alpha,t) < 0\}$

# Context & Application
Polarization is the first step in extracting a "generating set" (simple roots) from a root system. While the choice is not canonical, all choices are equivalent up to the Weyl group action, so the classification does not depend on it.

# Examples
**Example 8.19** (p. 96): For $A_{n-1}$, choosing $t$ so that $(t,e_1) > (t,e_2) > \cdots > (t,e_n)$ gives $R_+ = \{e_i - e_j \mid i < j\}$.

# Relationships
## Builds Upon
- **abstract-root-system**

## Enables
- **positive-roots** -- defined by the polarization
- **simple-roots** -- the indecomposable positive roots
- **weyl-chamber** -- each chamber determines a polarization

## Related
(none)

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking the polarization is unique
  **Correction**: There are $|W|$ polarizations (one per Weyl chamber), all related by $W$

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.4, page 94. Equation (8.6).

# Verification Notes
- Definition source: Direct from equation (8.6), p. 94
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
