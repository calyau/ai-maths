---
# === CORE IDENTIFICATION ===
concept: Half-Sum of Positive Roots
slug: half-sum-of-positive-roots

# === CLASSIFICATION ===
category: root-systems
subcategory: weyl-group
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 101
section: "8.7. Simple reflections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\rho$"
  - "Weyl vector"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-roots
  - fundamental-weights
extends: []
related:
  - simple-reflections
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is $\\rho$ (the half-sum of positive roots)?"
  - "Why is $\\rho$ equal to the sum of fundamental weights?"
---

# Quick Definition
The half-sum of positive roots $\rho = \frac{1}{2}\sum_{\alpha \in R_+}\alpha$ satisfies $\langle\rho,\alpha_i^\vee\rangle = 1$ for every simple root $\alpha_i$, and therefore $\rho = \sum_{i=1}^r \omega_i$ (the sum of all fundamental weights).

# Core Definition
Define (Lemma 8.36, p. 101):

$$\rho = \frac{1}{2}\sum_{\alpha \in R_+}\alpha$$

**Lemma 8.36**: $\langle\rho,\alpha_i^\vee\rangle = \frac{2(\rho,\alpha_i)}{(\alpha_i,\alpha_i)} = 1$ for each simple root $\alpha_i$.

Since $\langle\omega_j,\alpha_i^\vee\rangle = \delta_{ij}$, this gives $\rho = \omega_1 + \cdots + \omega_r$.

# Prerequisites
- **positive-roots** -- $\rho$ is defined as their half-sum
- **fundamental-weights** -- $\rho$ equals their sum

# Key Properties
1. $\rho = \frac{1}{2}\sum_{\alpha \in R_+}\alpha$
2. $\langle\rho,\alpha_i^\vee\rangle = 1$ for all simple $\alpha_i$ (Lemma 8.36)
3. $\rho = \sum_{i=1}^r \omega_i$
4. $s_i(\rho) = \rho - \alpha_i$ (from the proof of Lemma 8.36)

# Construction / Recognition
1. Sum all positive roots and divide by 2, or
2. Sum all fundamental weights

# Context & Application
$\rho$ is ubiquitous in representation theory. It appears in the Weyl character formula, the Weyl dimension formula, and the "shifted action" $w \cdot \lambda = w(\lambda + \rho) - \rho$ of the Weyl group.

# Examples
**Example**: For $A_1$, $R_+ = \{\alpha\}$, so $\rho = \alpha/2 = \omega$.

**Example**: For $A_2$, $R_+ = \{\alpha_1, \alpha_2, \alpha_1+\alpha_2\}$, so $\rho = \alpha_1 + \alpha_2 = \omega_1 + \omega_2$.

# Relationships
## Builds Upon
- **positive-roots**, **fundamental-weights**

## Enables
- Weyl character formula (Chapter 9)

## Related
- **simple-reflections** -- $s_i(\rho) = \rho - \alpha_i$

## Contrasts With
(none)

# Common Errors
- **Error**: Forgetting the factor of $1/2$
  **Correction**: $\rho$ is the half-sum, not the full sum

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.7, page 101. Lemma 8.36.

# Verification Notes
- Definition source: Direct from Lemma 8.36
- Confidence rationale: HIGH -- explicit definition and lemma
- Uncertainties: None
- Cross-reference status: Verified
