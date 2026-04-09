---
# === CORE IDENTIFICATION ===
concept: Character of a Representation
slug: character-of-representation

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 116
section: "9.5 Characters and Weyl character formula"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "formal character"
  - "ch(V)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-decomposition-theorem
  - weight-set
extends: []
related:
  - weyl-character-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character of a representation?"
  - "What must I know before understanding the Weyl character formula?"
---

# Quick Definition
The character of a finite-dimensional representation $V$ is the formal sum $\mathrm{ch}(V) = \sum_{\lambda \in P(V)} (\dim V[\lambda]) e^\lambda$, recording the weight multiplicities as a formal exponential sum in the group ring of the weight lattice.

# Core Definition
(Kirillov, p. 116, Section 9.5): The character is defined as:

$$\mathrm{ch}(V) = \sum_{\lambda \in P(V)} (\dim V[\lambda]) \, e^\lambda$$

This is an element of the group ring $\mathbb{Z}[P]$ of the weight lattice. The notation $e^\lambda$ is a formal exponential satisfying $e^\lambda \cdot e^\mu = e^{\lambda + \mu}$.

# Prerequisites
- **Weight decomposition theorem** -- the character records the weight multiplicities
- **Weight set** -- determines which terms appear

# Key Properties
1. Characters are additive: $\mathrm{ch}(V \oplus W) = \mathrm{ch}(V) + \mathrm{ch}(W)$
2. Characters are multiplicative: $\mathrm{ch}(V \otimes W) = \mathrm{ch}(V) \cdot \mathrm{ch}(W)$
3. Two representations are isomorphic iff they have the same character (for semisimple algebras)
4. $\mathrm{ch}(V)$ is Weyl-group invariant for finite-dimensional $V$
5. For a Verma module: $\mathrm{ch}(M_\lambda) = e^\lambda / \prod_{\alpha \in R_+} (1 - e^{-\alpha})$

# Context & Application
The character encodes all weight-level information about a representation. It is the key invariant used in the Weyl character formula, which provides a closed-form expression for $\mathrm{ch}(L_\lambda)$.

# Examples
**Example**: For $\mathfrak{sl}(2, \mathbb{C})$ and $V = L_2$ (the 3-dimensional irreducible), $\mathrm{ch}(L_2) = e^2 + e^0 + e^{-2}$.

# Relationships
## Builds Upon
- **Weight decomposition theorem** -- provides the data for the character

## Enables
- **Weyl character formula** -- gives an explicit formula for $\mathrm{ch}(L_\lambda)$

# Common Confusions
- **Confusion**: Confusing the formal character with the character of a group representation (trace function)
  **Clarification**: The formal character is an element of $\mathbb{Z}[P]$; the group character $\chi_V(g) = \mathrm{tr}(g|_V)$ is a class function. They are related but not identical.

# Source Reference
Chapter 9, Section 9.5 "Characters and Weyl character formula," p. 116.

# Verification Notes
- Definition source: Synthesized from section heading and standard definition; Section 9.5 content is truncated in the source markdown
- Confidence rationale: Medium -- section listed but content not fully present in converted markdown
- Uncertainties: Exact presentation in source is uncertain due to truncation
- Cross-reference status: Verified
