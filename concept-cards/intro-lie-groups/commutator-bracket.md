---
# === CORE IDENTIFICATION ===
concept: Commutator Bracket
slug: commutator-bracket

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 23
section: "3.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lie bracket"
  - "$[x, y]$"
  - "commutator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exponential-map
  - lie-group
extends: []
related:
  - lie-algebra
  - jacobi-identity
  - ad-map
contrasts_with:
  - group-commutator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The commutator bracket $[x, y]$ on $\mathfrak{g} = T_1G$ is the skew-symmetric bilinear map defined as the lowest non-trivial term of the group law in logarithmic coordinates: $\exp(x)\exp(y) = \exp(x + y + \frac{1}{2}[x, y] + \cdots)$.

# Core Definition

**Equation (3.2)** (Kirillov): $\exp(x)\exp(y) = \exp(x + y + \frac{1}{2}[x, y] + \cdots)$ for some bilinear skew-symmetric map $[\,,\,]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$. This map is called the commutator.

**Lemma 3.11**: The Taylor series for the group law $\mu(x, y)$ in logarithmic coordinates is $\mu(x, y) = x + y + \lambda(x, y) + \cdots$ where $\lambda$ is bilinear and skew-symmetric, and $[x, y] = 2\lambda(x, y)$.

# Prerequisites

- **Exponential map** — used to define logarithmic coordinates
- **Lie group** — the group whose multiplication gives rise to the bracket

# Key Properties

1. $[x, y]$ is bilinear and skew-symmetric: $[x, y] = -[y, x]$.
2. $\exp(x)\exp(y)\exp(-x)\exp(-y) = \exp([x, y] + \cdots)$ (Proposition 3.12 part 3).
3. Any morphism of Lie groups preserves the commutator: $\varphi_*[x, y] = [\varphi_* x, \varphi_* y]$ (Proposition 3.12 part 1).
4. The adjoint action preserves the commutator: $\mathrm{Ad}\, g([x, y]) = [\mathrm{Ad}\, g . x, \mathrm{Ad}\, g . y]$ (Proposition 3.12 part 2).
5. For matrix groups: $[x, y] = xy - yx$ (Example 3.13).

# Construction / Recognition

## To Construct/Create:
1. For matrix groups: compute $[x, y] = xy - yx$.
2. For general groups: use the Taylor expansion of $\exp(x)\exp(y)$ in logarithmic coordinates.

## To Identify/Recognize:
1. The bilinear skew-symmetric map appearing in the second-order term of $\mu(x, y)$.

# Context & Application

The commutator bracket is what gives $\mathfrak{g} = T_1G$ the structure of a Lie algebra. It encodes the non-commutativity of the group multiplication at the infinitesimal level. If $G$ is abelian, then $[x, y] = 0$ for all $x, y$.

# Examples

**Example 3.13** (p. 23): For $G \subset \mathrm{GL}(n)$: $[x, y] = xy - yx$. Proof: $(1+x+\cdots)(1+y+\cdots)(1-x+\cdots)(1-y+\cdots) = 1 + (xy - yx) + \cdots$.

**Example** (p. 23): If $G$ is commutative, then $[x, y] = 0$ (abelian Lie algebra).

# Relationships

## Builds Upon
- **Exponential map** — the bracket is extracted from the group law via exp

## Enables
- **Lie algebra** — the bracket makes $\mathfrak{g}$ into a Lie algebra
- **Jacobi identity** — the bracket satisfies this identity
- **ad map** — $\mathrm{ad}\, x . y = [x, y]$

## Related
- **Campbell-Hausdorff formula** — expresses the full group law using iterated brackets

## Contrasts With
- **Group commutator** — $ghg^{-1}h^{-1}$ in the group; related by $\exp([x,y] + \cdots) = \exp(x)\exp(y)\exp(-x)\exp(-y)$

# Common Errors

- **Error**: Assuming $[x, y] = 0$ implies $\exp(x)$ and $\exp(y)$ commute.
  **Correction**: $[x, y] = 0$ does imply they commute (Theorem 3.33), but this is non-trivial.

# Common Confusions

- **Confusion**: Whether the bracket $[x, y] = xy - yx$ applies to all Lie groups.
  **Clarification**: Only for matrix groups. For general Lie groups, there is no matrix product $xy$; the bracket is defined via the group law in logarithmic coordinates.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.2, equation (3.2), Lemma 3.11, Proposition 3.12, pages 22-23.

# Verification Notes

- Definition source: Direct from equation (3.2) and Lemma 3.11
- Confidence rationale: Explicit definition with proof
- Uncertainties: None
- Cross-reference status: Verified with Example 3.13, Proposition 3.12
