---
# === CORE IDENTIFICATION ===
concept: Connected Shimura Variety
slug: connected-shimura-variety

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 411
section: "Shimura varieties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Shimura variety

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hermitian-symmetric-domain
  - congruence-subgroup
  - baily-borel-theorem
extends:
  - baily-borel-theorem
related:
  - arithmetic-subgroup
  - adelic-description-of-congruence-subgroups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Shimura variety?"
---

# Quick Definition

A connected Shimura variety is an algebraic variety of the form $\Gamma \backslash X$ where $X$ is a hermitian symmetric domain and $\Gamma$ is a congruence subgroup of a simply connected semisimple group over $\mathbb{Q}$. It has a canonical model over a specific number field.

# Core Definition

Theorem 16.4 (Milne, p. 411): Let $G$, $u$, and $X$ be as in Theorem 16.2. If $\Gamma$ is a congruence subgroup, then $\Gamma \backslash X$ has a canonical model over a specific finite extension $\mathbb{Q}_\Gamma$ of $\mathbb{Q}$.

"The varieties arising in this way are called *connected Shimura varieties*." (Milne, p. 411)

# Prerequisites

- **Hermitian symmetric domain** — the "upstairs" complex manifold $X$
- **Congruence subgroup** — the discrete group $\Gamma$ (must be congruence, not merely arithmetic)
- **Baily-Borel theorem** — provides the algebraic structure on $\Gamma \backslash X$

# Key Properties

1. Connected Shimura varieties are algebraic varieties over number fields
2. The canonical model is over a specific number field $\mathbb{Q}_\Gamma$ depending on $\Gamma$
3. The use of *congruence* subgroups (not just arithmetic) is essential for the canonical model
4. The adèlic formulation provides a natural framework for these varieties

# Construction / Recognition

## To Construct:
1. Choose $G$ simply connected semisimple over $\mathbb{Q}$, no compact simple factors at infinity
2. Choose $u: U_1 \to G^{\mathrm{ad}}(\mathbb{R})$ satisfying Shimura conditions
3. Form $X = G^{\mathrm{ad}}(\mathbb{R})^+/K$
4. Choose a congruence subgroup $\Gamma$ (torsion-free for smooth quotient)
5. $\Gamma \backslash X$ is a connected Shimura variety with canonical model over $\mathbb{Q}_\Gamma$

# Context & Application

Connected Shimura varieties are among the most important objects in modern number theory and algebraic geometry. They provide moduli spaces for abelian varieties with additional structure, and they are the geometric objects underlying the Langlands program. The connection to Fermat's Last Theorem (via modular curves) demonstrates their profound significance.

# Examples

**Example 1** (p. 411): For $G = \mathrm{SL}_2$ and $\Gamma_0(N) = \left\{\begin{pmatrix}a & b \\ c & d\end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z}) \mid N \mid c\right\}$: $\mathbb{Q}_{\Gamma_0(N)} = \mathbb{Q}$, so $Y_0(N) = \Gamma_0(N) \backslash \mathcal{H}$ has a canonical model over $\mathbb{Q}$.

**Example 2** (p. 411): For every elliptic curve $E$ over $\mathbb{Q}$, there exists a nonconstant map $Y_0(N) \to E$ for some $N$ (modularity theorem), and from this Fermat's Last Theorem follows.

# Relationships

## Builds Upon
- **Hermitian symmetric domain** — the analytic space being quotiented
- **Congruence subgroup** — the discrete group; congruence (not just arithmetic) is essential
- **Baily-Borel theorem** — provides the algebraic structure

## Related
- **Arithmetic subgroup** — arithmetic subgroups give algebraic varieties but not necessarily canonical models
- **Adèlic description of congruence subgroups** — the adèlic viewpoint is natural for Shimura varieties

# Common Errors

- **Error**: Using an arithmetic (non-congruence) subgroup and expecting a canonical model
  **Correction**: The canonical model requires $\Gamma$ to be a *congruence* subgroup

# Common Confusions

- **Confusion**: Thinking "Shimura variety" and "modular curve" are unrelated
  **Clarification**: Modular curves (like $Y_0(N)$) are the simplest Shimura varieties, arising from $G = \mathrm{SL}_2$

- **Confusion**: Thinking Shimura varieties are defined over $\mathbb{C}$
  **Clarification**: The key feature is that they have canonical models over number fields

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 16, pages 411-412. Theorems 16.2, 16.4.

# Verification Notes

- Definition source: Theorem 16.4 and surrounding text, p. 411
- Confidence: HIGH — explicit definition and important examples
- Uncertainties: Proof of canonical models references Milne 2005
- Cross-reference status: Verified
