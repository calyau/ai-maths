---
# === CORE IDENTIFICATION ===
concept: Reduction Theory
slug: reduction-theory

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
pdf_page: 406
section: "Reduction theory"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - siegel-set
  - arithmetic-subgroup
  - reductive-algebraic-group
extends: []
related:
  - finite-covolume-criterion
  - fundamental-domain-sl2
  - presentation-of-arithmetic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

Reduction theory studies the geometry of the quotient $\Gamma \backslash G(\mathbb{R})$ for an arithmetic subgroup $\Gamma$ of a reductive group $G$. Its main results show that Siegel sets serve as approximate fundamental domains and determine when the quotient has finite volume or is compact.

# Core Definition

The main theorem of reduction theory (Theorem 12.1, Milne, p. 406): Let $\Gamma$ be an arithmetic subgroup in $G(\mathbb{Q})$. Then:

(a) For some Siegel set $\mathfrak{S}$, there exists a finite subset $C$ of $G(\mathbb{Q})$ such that $G(\mathbb{R}) = \Gamma \cdot C \cdot \mathfrak{S}$.

(b) For any $g \in G(\mathbb{Q})$ and Siegel set $\mathfrak{S}$, the set $\{\gamma \in \Gamma \mid g\mathfrak{S} \cap \gamma\mathfrak{S} \neq \emptyset\}$ is finite.

This holds for $\mathrm{GL}_n$ and extends to arbitrary reductive groups over $\mathbb{Q}$ (Borel 1969a, 13.1, 15.4).

# Prerequisites

- **Siegel set** — the approximate fundamental domains used in reduction theory
- **Arithmetic subgroup** — the discrete group whose quotient is studied
- **Reductive algebraic group** — reduction theory applies to reductive groups

# Key Properties

1. Finitely many $\Gamma$-translates of a Siegel set cover $G(\mathbb{R})$
2. Each Siegel set meets only finitely many of its $\Gamma$-translates
3. If $G$ has no nontrivial $\mathbb{Q}$-character, Siegel sets have finite measure (Theorem 12.3)
4. $\Gamma \backslash G(\mathbb{R})$ has finite volume iff $G$ has no nontrivial $\mathbb{Q}$-character (Theorem 12.4a)
5. $\Gamma \backslash G(\mathbb{R})$ is compact iff additionally $G(\mathbb{Q})$ has no unipotent $\neq 1$ (Theorem 12.4b)

# Construction / Recognition

## The Reduction Algorithm (for $\mathrm{GL}_n$):
1. Decompose $G(\mathbb{R}) = N \cdot A \cdot K$ (Iwasawa)
2. Define Siegel sets $\mathfrak{S}_{t,\omega}$
3. Show $G(\mathbb{R}) = \Gamma \cdot C \cdot \mathfrak{S}$ for finite $C$
4. Show finiteness of $\{\gamma \mid g\mathfrak{S} \cap \gamma\mathfrak{S} \neq \emptyset\}$

# Context & Application

Reduction theory originated with Gauss's work on binary quadratic forms and was developed by Minkowski, Siegel, and Borel. It provides the technical foundation for proving that arithmetic subgroups are lattices, that they are finitely presented, and for computing the geometry of locally symmetric spaces.

# Examples

**Example 1** (p. 407): For $\mathrm{SL}_2$, the Siegel sets in $\mathcal{H}$ are $\{z \mid \Im(z) \geq t, |\Re(z)| \leq u\}$.

**Example 2** (p. 407): For $G = \mathrm{SO}(q)$ with $q$ a nondegenerate quadratic form over $\mathbb{Q}$, $G(\mathbb{Z}) \backslash G(\mathbb{R})$ is compact iff $q$ does not represent zero in $\mathbb{Q}$ (Example 12.6).

**Example 3** (p. 407): For $B$ a quaternion division algebra with $B \otimes \mathbb{R} \simeq M_2(\mathbb{R})$, the associated group has compact quotient (Example 12.5b).

# Relationships

## Builds Upon
- **Siegel set** — the main technical tool
- **Arithmetic subgroup** — the objects being studied

## Enables
- **Finite covolume criterion** — a consequence of reduction theory
- **Presentation of arithmetic group** — finite generation follows from Theorem 12.1
- **Shimura varieties** — reduction theory ensures finite volume

## Related
- **Fundamental domain for SL₂** — the simplest case of reduction theory

# Common Errors

- **Error**: Thinking reduction theory gives a strict fundamental domain
  **Correction**: It gives an approximate fundamental domain (finitely many translates needed)

# Common Confusions

- **Confusion**: Thinking reduction theory only applies to $\mathrm{SL}_n$ or $\mathrm{GL}_n$
  **Clarification**: The theory applies to all reductive groups over $\mathbb{Q}$, using relative root systems and maximal split tori

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 12, pages 406-408. Theorems 12.1, 12.3, 12.4. Reference: Borel 1969a.

# Verification Notes

- Definition source: Theorem 12.1 directly from p. 406
- Confidence: HIGH — main theorems explicitly stated
- Uncertainties: Proofs reference Borel 1969a
- Cross-reference status: Verified
