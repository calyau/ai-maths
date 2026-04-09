---
# === CORE IDENTIFICATION ===
concept: Integrality Number
slug: integrality-number

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 90
section: "8.1. Abstract root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$n_{\\alpha\\beta}$"
  - "Cartan integer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
extends: []
related:
  - coroot
  - cartan-matrix
  - root-angles-and-length-ratios
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is $n_{\\alpha\\beta}$?"
  - "What is the geometric meaning of the integrality number?"
---

# Quick Definition
The integrality number $n_{\alpha\beta} = 2(\alpha,\beta)/(\beta,\beta)$ is the integer measuring the projection of $\alpha$ onto $\beta$ in units of $\beta/2$. Axiom R2 requires it to be an integer for all root pairs.

# Core Definition
For roots $\alpha,\beta \in R$, the integrality number is (equation 8.1, p. 90):

$$n_{\alpha\beta} = \frac{2(\alpha,\beta)}{(\beta,\beta)}$$

By axiom R2, $n_{\alpha\beta} \in \mathbb{Z}$. Equivalently, $n_{\alpha\beta} = \langle\alpha,\beta^\vee\rangle$ (equation 8.5). Geometrically, the orthogonal projection of $\beta$ onto $\alpha$ satisfies $p_\alpha(\beta) = \frac{n_{\beta\alpha}}{2}\alpha$ (p. 91).

# Prerequisites
- **abstract-root-system** -- defined in the context of a root system

# Key Properties
1. $n_{\alpha\beta} \in \mathbb{Z}$ (axiom R2)
2. $n_{\alpha\alpha} = 2$ for all $\alpha$
3. $n_{\alpha\beta} = \langle\alpha,\beta^\vee\rangle$
4. $s_\alpha(\beta) = \beta - n_{\beta\alpha}\alpha$
5. $n_{\alpha\beta}n_{\beta\alpha} = 4\cos^2\varphi$ where $\varphi$ is the angle between $\alpha,\beta$
6. $n_{\alpha\beta}/n_{\beta\alpha} = |\alpha|^2/|\beta|^2$ when $(\alpha,\beta) \neq 0$
7. For simple roots: $a_{ij} = n_{\alpha_j\alpha_i} = \langle\alpha_i^\vee,\alpha_j\rangle$ (Cartan matrix entry)

# Construction / Recognition
Compute $n_{\alpha\beta} = 2(\alpha,\beta)/(\beta,\beta)$.

# Context & Application
The integrality numbers are the fundamental numerical invariants of a root system. They are preserved by root system isomorphisms (which need not preserve inner products) and determine the Cartan matrix when restricted to simple roots.

# Examples
**Example** (p. 91): For $A_{n-1}$ with $(\alpha,\alpha) = 2$ for all $\alpha$: $n_{\alpha\beta} = (\alpha,\beta)$. For adjacent simple roots $\alpha_i = e_i - e_{i+1}$ and $\alpha_{i+1} = e_{i+1} - e_{i+2}$: $n_{\alpha_i\alpha_{i+1}} = -1$.

# Relationships
## Builds Upon
- **abstract-root-system** -- integrality is axiom R2

## Enables
- **cartan-matrix** -- $a_{ij} = n_{\alpha_j\alpha_i}$
- **root-angles-and-length-ratios** -- $n_{\alpha\beta}n_{\beta\alpha} = 4\cos^2\varphi$
- **reflection-in-root-system** -- $s_\alpha(\beta) = \beta - n_{\beta\alpha}\alpha$

## Related
- **coroot** -- $n_{\alpha\beta} = \langle\alpha,\beta^\vee\rangle$

## Contrasts With
(none)

# Common Errors
- **Error**: Confusing $n_{\alpha\beta}$ and $n_{\beta\alpha}$
  **Correction**: $n_{\alpha\beta} = 2(\alpha,\beta)/(\beta,\beta)$ has $\beta$ in the denominator; $n_{\beta\alpha}$ has $\alpha$ in the denominator

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.1, pages 90--91. Equation (8.1), equation (8.5).

# Verification Notes
- Definition source: Direct from equation (8.1)
- Confidence rationale: HIGH -- explicit formula
- Uncertainties: None
- Cross-reference status: Verified
